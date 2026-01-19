"""Production-ready Streamlit portfolio for an AI/ML engineer."""
from __future__ import annotations

import base64
import re
from pathlib import Path
from textwrap import dedent
from typing import Dict, List

import streamlit as st

from components.contact import render_contact_section
from components.education import render_certifications, render_education
from components.experience import render_experience
from components.flip_card import render_project_cards
from components.github_stats import render_github_stats
from components.resume import load_resume_base64, render_resume_section
from components.skills import render_skills
from data import (
    ABOUT,
    CERTIFICATIONS,
    CONTACT,
    EDUCATION,
    EXPERIENCE,
    GITHUB_CONFIG,
    ML_LAB,
    PROFILE,
    RESUME,
    SKILL_GROUPS,
)
from github_api import fetch_github_summary, fetch_portfolio_repositories

POSITIVE_TERMS = {
    "confident",
    "delight",
    "excellent",
    "fast",
    "improved",
    "seamless",
    "stable",
    "successful",
    "wins",
}

NEGATIVE_TERMS = {
    "bug",
    "crash",
    "delay",
    "friction",
    "issue",
    "lag",
    "risk",
    "slow",
    "unstable",
}


def _load_css() -> None:
    css_path = Path(__file__).parent / "styles" / "style.css"
    with css_path.open("r", encoding="utf-8") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


def _ensure_assets() -> None:
    assets_dir = Path(__file__).parent / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    avatar_path = assets_dir / "profile.png"
    if not avatar_path.exists() or avatar_path.stat().st_size == 0:
        placeholder_png = (
            "iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAACENnwnAAAAD0lEQVR42mNk+M/AwMAAAjUAmzquw3YAAAAASUVORK5CYII="
        )
        avatar_path.write_bytes(base64.b64decode(placeholder_png))
    resume_path = assets_dir / "resume.pdf"
    if not resume_path.exists() or resume_path.stat().st_size == 0:
        resume_bytes = (
            b"%PDF-1.4\n1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
            b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
            b"3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 300 200] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj\n"
            b"4 0 obj << /Length 90 >> stream\n"
            b"BT /F1 18 Tf 30 150 Td (Replace with your resume PDF) Tj ET\n"
            b"BT /F1 12 Tf 30 120 Td (assets/resume.pdf) Tj ET\n"
            b"endstream endobj\n"
            b"5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n"
            b"xref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000063 00000 n \n0000000116 00000 n \n0000000274 00000 n \n0000000387 00000 n \n"
            b"trailer << /Size 6 /Root 1 0 R >>\nstartxref\n470\n%%EOF\n"
        )
        resume_path.write_bytes(resume_bytes)


def _image_data_uri(path_str: str) -> str:
    path = Path(path_str)
    if path.exists():
        encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
        return f"data:image/png;base64,{encoded}"
    return path_str


def _lexicon_sentiment(text: str) -> tuple[str, float]:
    words = re.findall(r"[\w']+", text.lower())
    if not words:
        return "Neutral", 0.0
    pos_hits = sum(1 for token in words if token in POSITIVE_TERMS)
    neg_hits = sum(1 for token in words if token in NEGATIVE_TERMS)
    score = (pos_hits - neg_hits) / max(len(words), 1)
    if score > 0.02:
        label = "Positive"
    elif score < -0.02:
        label = "Negative"
    else:
        label = "Neutral"
    return label, score


def _render_nav() -> None:
    nav_items = [
        ("hero", "Hero"),
        ("about", "About"),
        ("experience", "Experience"),
        ("education", "Education"),
        ("skills", "Skills"),
        ("projects", "Projects"),
        ("github", "GitHub"),
        ("lab", "ML Lab"),
        ("resume", "Resume"),
        ("contact", "Contact"),
    ]
    links = "".join(f"<a href='#{slug}'>{label}</a>" for slug, label in nav_items)
    st.markdown(f"<nav class='sidebar-nav'>{links}</nav>", unsafe_allow_html=True)


def _anchor(slug: str) -> None:
    st.markdown(f"<span id='{slug}' class='section-anchor'></span>", unsafe_allow_html=True)


def _render_hero(summary: Dict) -> None:
    hero_stats = "".join(
        f"<div class='stat-tile'><p class='eyebrow'>{stat['label']}</p><h3>{stat['value']}</h3></div>"
        for stat in PROFILE["hero_stats"]
    )
    ctas = "".join(
        f"<a class='ghost-btn' href='{url}' target='_blank' rel='noopener'>{label}</a>"
        for label, url in PROFILE["socials"].items()
        if label != "Resume"
    )
    resume_b64 = load_resume_base64(RESUME.get("path", ""))
    resume_href = f"data:application/pdf;base64,{resume_b64}" if resume_b64 else "#resume"
    resume_btn = f"<a class='solid-btn' href='{resume_href}' download>Download Resume</a>"
    avatar_src = _image_data_uri(PROFILE["avatar"])

    hero_markup = dedent(
        f"""
        <section class='section-shell'>
            <div class='hero-grid'>
                <div class='hero-card'>
                    <p class='eyebrow'>{PROFILE['availability']}</p>
                    <h1>{PROFILE['name']}</h1>
                    <h3>{PROFILE['role']}</h3>
                    <p class='hero-bio'>{PROFILE['tagline']}</p>
                    <div class='hero-actions'>{resume_btn}{ctas}</div>
                    <div class='hero-stats'>{hero_stats}</div>
                </div>
                <div>
                    <img src='{avatar_src}' class='hero-avatar' alt='Profile portrait' />
                </div>
            </div>
        </section>
        """
    ).strip()
    st.markdown(hero_markup, unsafe_allow_html=True)


def _render_about() -> None:
    highlights = "".join(f"<li>{point}</li>" for point in ABOUT["highlights"])
    focus = "".join(f"<span class='chip'>{item}</span>" for item in ABOUT["focus"])
    st.markdown(
        f"""
        <section class='section-shell'>
            <h2>About</h2>
            <p>{ABOUT['headline']}</p>
            <ul>{highlights}</ul>
            <div class='badge-row'>{focus}</div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_experience() -> None:
    _anchor("experience")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    st.subheader("Work Experience")
    render_experience(EXPERIENCE)
    st.markdown("</section>", unsafe_allow_html=True)


def _render_education_section() -> None:
    _anchor("education")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    st.subheader("Education & Certifications")
    render_education(EDUCATION)
    render_certifications(CERTIFICATIONS)
    st.markdown("</section>", unsafe_allow_html=True)


def _render_projects(username: str, topic: str) -> List[Dict]:
    _anchor("projects")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    st.subheader("Live Projects")
    with st.spinner("Fetching projects from GitHub..."):
        repos = fetch_portfolio_repositories(username=username, topic=topic)
    render_project_cards(repos)
    st.markdown("</section>", unsafe_allow_html=True)
    return repos


def _render_ml_lab() -> None:
    _anchor("lab")
    st.subheader("ML Lab — quick demos")
    sentiment_tab, resume_tab = st.tabs([ML_LAB["sentiment"]["title"], ML_LAB["resume"]["title"]])

    with sentiment_tab:
        st.caption(ML_LAB["sentiment"]["description"])
        default_text = "The new multilingual assistant delightfully resolved onboarding issues in seconds."
        text = st.text_area("Text input", value=default_text, placeholder=ML_LAB["sentiment"]["placeholder"], key="sentiment-input")
        if st.button("Analyze sentiment", key="sentiment-btn"):
            if not text.strip():
                st.warning("Please provide some text.")
            else:
                label, score = _lexicon_sentiment(text)
                st.metric("Sentiment", label, f"score {score:+.2f}")

    with resume_tab:
        st.caption(ML_LAB["resume"]["description"])
        resume_text = st.text_area("Resume snippet", value="Architected PyTorch transformers with Vertex pipelines.", placeholder=ML_LAB["resume"]["placeholder"], key="resume-input")
        if st.button("Score resume", key="resume-btn"):
            keywords = ML_LAB["resume"]["keywords"]
            text_lower = resume_text.lower()
            hits = [kw for kw in keywords if kw in text_lower]
            coverage = int((len(hits) / len(keywords)) * 100)
            st.progress(coverage)
            st.write(f"Coverage: {coverage}% ({len(hits)} / {len(keywords)} critical keywords)")
            if hits:
                st.write("Detected keywords:", ", ".join(hits))

    st.markdown(
        """
        <div class='chatbot-banner'>
            <p class='eyebrow'>AI Chatbot (beta)</p>
            <h4>"Chat with my portfolio" </h4>
            <p>LangChain · FAISS · MiniLM embeddings · Resume PDF · README vectors</p>
            <p class='card-copy'>The conversational agent ingests my resume, project READMEs, and FAQs so recruiters can ask bespoke questions about impact, stacks, and decisions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="Shikher Jain · AI Engineer",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    _ensure_assets()
    _load_css()
    _render_nav()
    st.markdown("<div class='app-shell'>", unsafe_allow_html=True)

    _anchor("hero")
    gh_summary = fetch_github_summary(GITHUB_CONFIG["username"])
    _render_hero(gh_summary)

    _anchor("about")
    _render_about()

    _render_experience()

    _render_education_section()

    _anchor("skills")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    st.subheader("Skills")
    render_skills(SKILL_GROUPS)
    st.markdown("</section>", unsafe_allow_html=True)

    repos = _render_projects(GITHUB_CONFIG["username"], GITHUB_CONFIG["topic"])

    summary_for_stats = dict(gh_summary)
    if repos:
        summary_for_stats["total_stars"] = sum(repo.get("stars", 0) for repo in repos)
        summary_for_stats["latest_repo"] = repos[0].get("name", "")
    else:
        summary_for_stats.setdefault("total_stars", 0)
        summary_for_stats.setdefault("latest_repo", "")

    _anchor("github")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    st.subheader("GitHub Snapshot")
    st.markdown("<h4 class='subtle-subhead'>Contribution activity</h4>", unsafe_allow_html=True)

    render_github_stats(summary_for_stats, repos)
    st.markdown("</section>", unsafe_allow_html=True)


    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    _render_ml_lab()
    st.markdown("</section>", unsafe_allow_html=True)

    _anchor("resume")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    render_resume_section(RESUME)
    st.markdown("</section>", unsafe_allow_html=True)

    _anchor("contact")
    st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
    render_contact_section(CONTACT)
    st.markdown("</section>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
