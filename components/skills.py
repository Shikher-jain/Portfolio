"""Skills section renderer (normal simple format)."""

from html import escape
from textwrap import dedent
from typing import Any

import streamlit as st


def _skill_line(skill: dict[str, Any]) -> str:
    name = escape(str(skill.get("name", "Unnamed")))
    badges = skill.get("badges", []) or []
    if not badges:
        return f"<li>{name}</li>"
    badges_text = ", ".join(escape(str(item)) for item in badges)
    return f"<li><strong>{name}</strong>: {badges_text}</li>"


def _group_block(group: dict[str, Any]) -> str:
    category = escape(str(group.get("category", "Skills")))
    skills = group.get("skills", []) or []
    lines = "".join(_skill_line(skill) for skill in skills if isinstance(skill, dict))
    return dedent(
        f"""
        <div class='skill-card'>
            <h4>{category}</h4>
            <ul>{lines}</ul>
        </div>
        """
    ).strip()


def render_skills(skill_groups: list[dict[str, Any]]) -> str:
    """Render skills as a carousel using Streamlit-native controls."""
    groups = [group for group in skill_groups if isinstance(group, dict) and group.get("category")]
    if not groups:
        return "<div class='skill-grid'><div class='skill-card'><h4>Skills</h4><p>No skills added yet.</p></div></div>"

    slide_key = "skills_slide_index"
    if slide_key not in st.session_state:
        st.session_state[slide_key] = 0

    total_slides = len(groups)
    st.session_state[slide_key] = st.session_state[slide_key] % total_slides

    prev_col, status_col, next_col = st.columns([1, 2, 1])
    with prev_col:
        if st.button("◀ Previous", key="skills-prev-btn"):
            st.session_state[slide_key] = (st.session_state[slide_key] - 1 + total_slides) % total_slides
    with status_col:
        current_index = st.session_state[slide_key]
        current_category = escape(str(groups[current_index].get("category", "Skills")))
        st.markdown(
            f"<p style='text-align:center; margin-top:0.6rem;'><strong>{current_category}</strong>"
            f" &nbsp;|&nbsp; Slide {current_index + 1} of {total_slides}</p>",
            unsafe_allow_html=True,
        )
    with next_col:
        if st.button("Next ▶", key="skills-next-btn"):
            st.session_state[slide_key] = (st.session_state[slide_key] + 1) % total_slides

    selected_group = groups[st.session_state[slide_key]]
    return f"<div class='skill-grid'>{_group_block(selected_group)}</div>"
