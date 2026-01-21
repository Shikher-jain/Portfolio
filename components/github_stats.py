"""Visual components for GitHub stats."""
from typing import Dict, List
import streamlit as st

CONTRIBUTION_GRAPH_URL = "https://github-readme-activity-graph.vercel.app/graph?username=Shikher-jain&theme=tokyo-night&hide_border=true"
GRAPH_WRAPPER_STYLE = "display:flex; justify-content:center;"
GRAPH_CANVAS_STYLE = "max-width:960px; width:100%;"
GRAPH_IMG_STYLE = "width:100%; height:auto; display:block;"


def _repo_badges(repo: Dict) -> str:
    langs = repo.get("languages") or ["Python"]
    badges = "".join(f"<span class='badge'>{lang}</span>" for lang in langs)
    topics = repo.get("topics") or []
    chips = "".join(f"<span class='chip'>{topic}</span>" for topic in topics)
    return badges + chips


def render_github_stats(summary: Dict, repos: List[Dict] | None = None) -> None:
    has_summary = bool(summary)
    if not has_summary:
        st.warning("GitHub stats are temporarily unavailable. Showing latest public graph instead.")

    chart_url = summary.get("contribution_graph") if has_summary else None
    if chart_url:
        st.markdown(
            f"""
        <section class='section-shell'>
            <div style="{GRAPH_WRAPPER_STYLE}">
                <figure style="{GRAPH_CANVAS_STYLE}">
                    <img src="{chart_url}" 
                         alt="GitHub contribution heatmap" 
                         loading="lazy"
                         style="{GRAPH_IMG_STYLE}" />
                    <figcaption style="margin-top:8px; color:#9CA3AF; text-align:center;">
                        365-day Streak Heatmap
                    </figcaption>
                </figure>
            </div>
        
        <div style="{GRAPH_WRAPPER_STYLE}">
            <figure style="{GRAPH_CANVAS_STYLE}">
                <img src="{CONTRIBUTION_GRAPH_URL}" 
                     alt="GitHub contribution graph"
                     loading="lazy" 
                     style="{GRAPH_IMG_STYLE}" />
                <figcaption style="margin-top:8px; color:#9CA3AF; text-align:center;">
                    365-day GitHub Contribution Graph
                </figcaption>
            </figure>
        </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

'''
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
                        <span class='stat-pill'>⭐ {chosen.get('stars', 2)}</span>
                        <span class='stat-pill'>🍴 {chosen.get('forks', 1)}</span>
                    </div>
                    <div class='card-actions'>
                        <a class='ghost-btn' href='{chosen.get('html_url')}' target='_blank' rel='noopener'>GitHub</a>
                        {f"<a class='solid-btn' href='{chosen.get('homepage')}' target='_blank' rel='noopener'>Live</a>" if chosen.get('homepage') else ''}
                """,
                unsafe_allow_html=True,
            )
'''