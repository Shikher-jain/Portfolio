"""Skills grid with animated progress bars."""
from textwrap import dedent
from typing import List, Dict

import streamlit as st


def render_skills(skill_groups: List[Dict]) -> None:
    categories = [group.get("category", "") for group in skill_groups]
    filter_options = ["All"] + categories
    choice = st.selectbox("Filter skill category", filter_options, key="skills-filter")

    groups_to_render = skill_groups if choice == "All" else [group for group in skill_groups if group.get("category") == choice]

    grid = []
    for group in groups_to_render:
        items_html = "".join(
            dedent(
                f"""
                <div class='skill-item'>
                    <div class='skill-heading'>
                        <span>{item['name']}</span>
                    </div>
                    <div class='tag-row'>{' '.join(f"<span class='chip'>{badge}</span>" for badge in item.get('badges', []))}</div>
                </div>
                """
            ).strip()
            for item in group.get("skills", [])
        )
        grid.append(
            dedent(
                f"""
                <section class='skill-card'>
                    <h4>{group.get('category')}</h4>
                    {items_html}
                </section>
                """
            ).strip()
        )

    st.markdown(f"<div class='skill-grid'>{''.join(grid)}</div>", unsafe_allow_html=True)
