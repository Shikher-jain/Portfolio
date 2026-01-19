"""Render education history and certifications."""
from textwrap import dedent
from typing import Dict, List

import streamlit as st


def render_education(education: List[Dict]) -> None:
    if not education:
        st.info("Education details coming soon.")
        return

    cards = []
    for item in education:
        cards.append(
            dedent(
                f"""
                <article class='education-card'>
                    <header>
                        <p class='eyebrow'>{item.get('period')}</p>
                        <h4>{item.get('institution')}</h4>
                        <p class='card-copy'>{item.get('degree')}</p>
                        <p class='card-copy'>{item.get('details')}</p>
                    </header>
                </article>
                """
            ).strip()
        )

    st.markdown(f"<div class='education-grid'>{''.join(cards)}</div>", unsafe_allow_html=True)


def render_certifications(certifications: List[str]) -> None:
    if not certifications:
        return
    chips = "".join(f"<span class='chip'>{cert}</span>" for cert in certifications)
    st.markdown(f"<div class='cert-chip-row'>{chips}</div>", unsafe_allow_html=True)
