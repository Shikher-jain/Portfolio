"""GitHub data access layer with caching and graceful degradation."""
from __future__ import annotations

import os
from datetime import datetime
from functools import lru_cache
from typing import Dict, List

import requests
import streamlit as st

API_BASE = "https://api.github.com"
TIMEOUT = 15


def _build_headers() -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github.mercy-preview+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _safe_request(url: str, params: Dict | None = None) -> Dict | List | None:
    try:
        response = requests.get(url, headers=_build_headers(), params=params, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:  # pragma: no cover - network failure path
        st.warning(f"GitHub API request failed: {exc}")
        return None


@lru_cache(maxsize=128)
def _fetch_languages(url: str) -> List[str]:
    payload = _safe_request(url)
    if not payload:
        return []
    sorted_langs = sorted(payload.items(), key=lambda item: item[1], reverse=True)
    return [name for name, _ in sorted_langs[:5]]


def _infer_category(topics: List[str]) -> str:
    canonical = {
        "nlp": "NLP",
        "ml": "Machine Learning",
        "ai": "Artificial Intelligence",
        "vision": "Computer Vision",
        "data-engineering": "Data Engineering",
    }
    for topic in topics:
        if topic.lower() in canonical:
            return canonical[topic.lower()]
    return "Applied AI"


def _format_timestamp(ts: str) -> str:
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%d %b %Y")
    except ValueError:  # pragma: no cover - inconsistent timestamp
        return ts


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_portfolio_repositories(username: str, topic: str = "portfolio") -> List[Dict]:
    """Search repositories by topic and enrich them with language metadata."""
    params = {
        "q": f"user:{username} topic:{topic}",
        "sort": "updated",
        "order": "desc",
        "per_page": 20,
    }
    payload = _safe_request(f"{API_BASE}/search/repositories", params=params)
    if not payload:
        return []

    projects: List[Dict] = []
    for repo in payload.get("items", []):
        languages = _fetch_languages(repo.get("languages_url", ""))
        topics = repo.get("topics", [])
        projects.append(
            {
                "name": repo.get("name"),
                "full_name": repo.get("full_name"),
                "description": repo.get("description") or "Production-ready AI asset.",
                "languages": languages,
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "updated": _format_timestamp(repo.get("updated_at", "")),
                "html_url": repo.get("html_url"),
                "homepage": repo.get("homepage") or "",
                "topics": topics,
                "category": _infer_category(topics),
                "default_branch": repo.get("default_branch", "main"),
            }
        )
    return projects


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_github_summary(username: str, repos: List[Dict] | None = None) -> Dict:
    """Aggregate lightweight stats for the hero + stats widgets."""
    profile = _safe_request(f"{API_BASE}/users/{username}") or {}
    repos = repos or []
    total_stars = sum(item.get("stars", 0) for item in repos)
    latest_repo = repos[0]["name"] if repos else ""
    return {
        "followers": profile.get("followers", 0),
        "public_repos": profile.get("public_repos", 0),
        "following": profile.get("following", 0),
        "total_stars": total_stars,
        "profile_url": profile.get("html_url", f"https://github.com/{username}"),
        "avatar_url": profile.get("avatar_url", ""),
        "latest_repo": latest_repo,
        "contribution_graph": f"https://ghchart.rshah.org/{username}",
    }
