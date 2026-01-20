"""3D flip-card renderer for GitHub projects."""
from __future__ import annotations

from html import escape
from textwrap import dedent
from typing import Dict, List
import uuid

import streamlit as st


def _build_card(project: Dict) -> str:
    card_id = f"card-{uuid.uuid4().hex}"
    languages = project.get("languages") or ["Python"]
    description = project.get("description") or "Production-grade AI workflow."
    tech_badges = "".join(
        f"<span class='badge'>{escape(lang)}</span>" for lang in languages
    )
    topics = project.get("topics") or []
    topic_label = project.get("category", "Applied AI")
    topic_html = f"<span class='topic-chip'>{escape(topic_label)}</span>"
    back_description = escape(description)
    details = (
        f"<p class='card-copy'>{back_description}</p>"
        f"<p class='card-meta'>Updated {escape(project.get('updated', ''))}</p>"
    )
    stats = (
        f"<div class='stat-pill'>⭐ {project.get('stars', 0)}</div>"
        f"<div class='stat-pill'>🍴 {project.get('forks', 0)}</div>"
    )
    actions = ""
    if project.get("html_url"):
        actions += (
            f"<a class='ghost-btn' href='{project['html_url']}' target='_blank' rel='noopener'>GitHub</a>"
        )
    if project.get("homepage"):
        actions += (
            f"<a class='solid-btn' href='{project['homepage']}' target='_blank' rel='noopener'>Live Demo</a>"
        )

    return dedent(
        f"""
        <article class='portfolio-card' id='{card_id}' tabindex='0'>
            <div class='card-inner'>
                <div class='card-face card-front'>
                    <div class='card-header'>
                        {topic_html}
                        <div class='card-updated'>Updated {escape(project.get('updated', ''))}</div>
                    </div>
                    <h3>{escape(project.get('name', 'Project'))}</h3>
                    <p class='card-copy'>{escape(description[:140])}</p>
                    <div class='badge-row'>{tech_badges}</div>
                </div>
                <div class='card-face card-back'>
                    <h4>{escape(project.get('category', 'Applied AI'))}</h4>
                    {details}
                    <div class='badge-row'>{"".join(f"<span class='chip'>{escape(topic)}</span>" for topic in topics)}</div>
                    <div class='stats-row'>{stats}</div>
                    <div class='card-actions'>{actions}</div>
                </div>
            </div>
        </article>
        """
    ).strip()


def render_project_cards(projects: List[Dict]) -> None:
    """Render the responsive grid of project cards with hover/tap flip interactions."""
    if not projects:
        st.info("Publish a repository with the 'portfolio' topic to see it reflected here automatically.")
        return

    cards_html = "".join(_build_card(repo) for repo in projects)
    script = dedent(
        """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const prefersHover = window.matchMedia('(hover: hover)').matches;
            document.querySelectorAll('.portfolio-card').forEach(card => {
                if (!prefersHover) {
                    card.addEventListener('click', () => card.classList.toggle('is-flipped'));
                    card.addEventListener('keypress', (event) => {
                        if (event.key === 'Enter' || event.key === ' ') {
                            event.preventDefault();
                            card.classList.toggle('is-flipped');
                        }
                    });
                }
            });
        });
        </script>
        """
    ).strip()
    st.markdown(
        f"<div class='project-grid'>{cards_html}</div>{script}",
        unsafe_allow_html=True,
    )
