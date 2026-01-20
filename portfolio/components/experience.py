"""Timeline cards for work experience."""
from textwrap import dedent
from typing import Dict, List


def render_experience(experiences: List[Dict]) -> str:
    if not experiences:
        return ""

    cards = []
    for item in experiences:
        bullets = "".join(f"<li>{point}</li>" for point in item.get("highlights", []))
        stack = "".join(f"<span class='chip'>{tag}</span>" for tag in item.get("stack", []))
        cards.append(
            dedent(
                f"""
                <article class='experience-card'>
                    <header>
                        <p class='eyebrow'>{item.get('date')}</p>
                        <h4>{item.get('role')}</h4>
                        <p class='card-copy'>{item.get('company')} · {item.get('location')}</p>
                    </header>
                    <ul>{bullets}</ul>
                    <div class='experience-tags'>{stack}</div>
                </article>
                """
            ).strip()
        )

    return f"<div class='experience-grid'>{''.join(cards)}</div>"
