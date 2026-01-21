"""Render education history and certifications."""
from textwrap import dedent
from typing import Dict, List


def render_education(education: List[Dict]) -> str:
    if not education:
        return ""

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

    return f"<div class='education-grid'>{''.join(cards)}</div>"


def render_certifications(certifications: List[str]) -> str:
    if not certifications:
        return ""
    chips = "".join(f"<span class='chip'>{cert}</span>" for cert in certifications)
    return f"<div class='cert-chip-row'>{chips}</div>"
