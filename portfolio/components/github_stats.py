"""Visual components for GitHub stats."""
from typing import Dict, List

import streamlit as st


def _repo_badges(repo: Dict) -> str:
    langs = repo.get("languages") or ["Python"]
    badges = "".join(f"<span class='badge'>{lang}</span>" for lang in langs)
    topics = repo.get("topics") or []
    chips = "".join(f"<span class='chip'>{topic}</span>" for topic in topics)
    return badges + chips


def render_github_stats(summary: Dict, repos: List[Dict] | None = None) -> None:
    if not summary:
        st.warning("GitHub stats are temporarily unavailable.")
        return

    chart_url = summary.get("contribution_graph")
    if chart_url:
        st.markdown(
    f"""
    <div style="display:flex; justify-content:center; align-items:center; flex-direction:column;">
        <img src="{chart_url}" 
             alt="GitHub contribution heatmap" 
             loading="lazy"
             style="max-width:100%; height:auto;" />
        <figcaption style="margin-top:8px; color: #9CA3AF;">
            365-day Streak Heatmap
        </figcaption>
    </div>
    """,
    unsafe_allow_html=True
)


    if repos:
        st.markdown("<div class='repo-spotlight-shell'>", unsafe_allow_html=True)
        names = [repo.get("name", "") for repo in repos]
        selected = st.selectbox(
            "Repo spotlight",
            names,
            key="github-spotlight",
            label_visibility="collapsed",
        )
        chosen = next((repo for repo in repos if repo.get("name") == selected), None)
        if chosen:
            st.markdown(
                f"""
                <div class='repo-spotlight'>
                    <div class='spotlight-header'>
                        <p class='eyebrow'>{chosen.get('category', 'Applied AI')}</p>
                        <h4>{chosen.get('name')}</h4>
                    </div>
                    <p class='card-copy'>{chosen.get('description')}</p>
                    <div class='badge-row'>{_repo_badges(chosen)}</div>
                    <div class='stats-row'>
                        <span class='stat-pill'>⭐ {chosen.get('stars', 0)}</span>
                        <span class='stat-pill'>🍴 {chosen.get('forks', 0)}</span>
                        <span class='stat-pill'>Updated {chosen.get('updated')}</span>
                    </div>
                    <div class='card-actions'>
                        <a class='ghost-btn' href='{chosen.get('html_url')}' target='_blank' rel='noopener'>GitHub</a>
                        {f"<a class='solid-btn' href='{chosen.get('homepage')}' target='_blank' rel='noopener'>Live</a>" if chosen.get('homepage') else ''}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
