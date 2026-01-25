from __future__ import annotations

import base64
import re
from contextlib import contextmanager
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
from components.social_icons import get_social_icon_url
from data import (
    ABOUT,
    CERTIFICATIONS,
    CONTACT,
    EDUCATION,
    EXPERIENCE,
    FEATURED_PROJECTS,
    FEATURED_TOPIC_TAGS,
    PROJECT_SHORTLIST,
    SHORTLIST_FALLBACKS,
    GITHUB_CONFIG,
    ML_LAB,
    PROFILE,
    RESUME,
    SKILL_GROUPS,
)

from github_api import fetch_github_summary, fetch_portfolio_repositories, fetch_repository
from live_demos import apply_live_demo_links

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
        ("resume", "Resume"),
        ("contact", "Contact"),
        ("lab", "ML Lab"),
    ]
    
    links = "".join(f"<a href='#{slug}'>{label}</a>" for slug, label in nav_items)
    logo_src = _image_data_uri(PROFILE.get("logo", ""))
    nav_markup = dedent(
        f"""
        <nav class='floating-nav'>
                <div class='nav-logo'>
                    {f"<img src='{logo_src}' alt='logo' />" if PROFILE.get('logo')
                      else '<span  class="nav-eyebrow">Portfolio</span>'}
                </div>
            <div class='nav-links'>{links}</div>
            <a class='nav-cta' href='#contact'>Let's Talk</a>
        </nav>
        """
    ).strip()
    st.markdown(nav_markup, unsafe_allow_html=True)


def _anchor(slug: str) -> None:
    st.markdown(f"<span id='{slug}' class='section-anchor'></span>", unsafe_allow_html=True)


@contextmanager
def _section_shell(anchor: str | None = None, title: str | None = None) -> None:
    if anchor:
        _anchor(anchor)
    container = st.container()
    with container:
        st.markdown("<section class='section-shell'>", unsafe_allow_html=True)
        if title:
            st.markdown(f"<h2>{title}</h2>", unsafe_allow_html=True)
        yield
        st.markdown("</section>", unsafe_allow_html=True)


def _social_cta(label: str, url: str) -> str:
    icon_url = get_social_icon_url(label)
    return (
        f"<a class='ghost-btn hero-cta' href='{url}' target='_blank' rel='noopener'>"
        f"<span class='social-icon'><img src='{icon_url}' alt='{label} icon' loading='lazy' /></span>"
        f"<span>{label}</span>"
        "</a>"
    )


def _render_hero(summary: Dict) -> None:
    hero_stats = "".join(
        f"<div class='stat-tile'><p class='eyebrow'>{stat['label']}</p><h3>{stat['value']}</h3></div>"
        for stat in PROFILE["hero_stats"]
    )
    ctas = "".join(_social_cta(label, url) for label, url in PROFILE["socials"].items() if label != "Resume")
    resume_b64 = load_resume_base64(RESUME.get("path", ""))
    resume_href = f"data:application/pdf;base64,{resume_b64}" if resume_b64 else "#resume"
    resume_btn = f"<a class='solid-btn' href='{resume_href}' download>Download Resume</a>"
    avatar_src = _image_data_uri(PROFILE["avatar"])
    hero_meta = "".join(
        f"<div><p class='eyebrow'>{label}</p><h4>{value}</h4></div>"
        for label, value in [
            ("Location", PROFILE.get("location", "")),
            ("Education", PROFILE.get("experience", "")),
            ("Email", PROFILE.get("email", "")),
        ]
        if value
    )

    hero_markup = dedent(
        f"""
        <section class='section-shell hero-section'>
            <div class='hero-card hero-card--expanded'>
                <div class='hero-top'>
                    <div class='hero-avatar-card'>
                        <img src='{avatar_src}' alt='Profile portrait'/>
                        <p class='hero-bio' style="padding:12px 2px 2px 1px;">{PROFILE['role']}</p>
                    </div>
                    <div class='hero-copy'>
                        <p class='eyebrow'>{PROFILE['availability']}</p>
                        <h1>{PROFILE['name']}</h1>
                        <p class='hero-bio'>{PROFILE['tagline']}</p>
                        <div class='hero-actions'>{resume_btn}{ctas}</div>
                    </div>
                </div>
                <div class='hero-stats'>{hero_stats}</div>
            </div>
            <div class='hero-meta-panel'>{hero_meta}</div>
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
    experience_markup = render_experience(EXPERIENCE)
    if not experience_markup:
        st.info("Work experience will appear here once it's added.")
        return
    st.markdown(
        f"""
        <section class='section-shell'>
            <h2>Work Experience</h2>
            {experience_markup}
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_education_section() -> None:
    _anchor("education")
    education_markup = render_education(EDUCATION)
    cert_markup = render_certifications(CERTIFICATIONS)
    if not education_markup and not cert_markup:
        st.info("Add your education details to showcase degrees and certifications here.")
        return
    st.markdown(
        f"""
        <section class='section-shell'>
            <h2>Education & Certifications</h2>
            {education_markup}
            {cert_markup}
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_projects(username: str, topic: str) -> tuple[List[Dict], List[Dict]]:
    _anchor("projects")

    # st.markdown("""
    #     <div class='card-container' style='background-color: #2c2c2c; padding: 20px; border-radius: 10px;'>
    # """, unsafe_allow_html=True)

    st.subheader("Live Projects")

    col_left, col_right = st.columns([3, 1.6])
    with col_left:
        source_choice = st.radio(
            "Project feed",
            ("GitHub sync", "Featured showcase"),
            horizontal=True,
            key="project-source",
        )
    with col_right:
        live_toggle = st.toggle("Live demos only", value=False, key="live-only-toggle")

    with st.spinner("Fetching projects from GitHub..."):
        github_repos = fetch_portfolio_repositories(username=username, topic=topic)
        github_repos = apply_live_demo_links(github_repos)

    featured_topic_tags = {tag.lower() for tag in FEATURED_TOPIC_TAGS} or {"feature"}
    shortlist_fallback_map = {key.lower(): value for key, value in SHORTLIST_FALLBACKS.items()}

    featured_candidates = [
        repo
        for repo in github_repos
        if featured_topic_tags.issubset({topic.lower() for topic in repo.get("topics", [])})
    ]

    curated_featured = apply_live_demo_links(FEATURED_PROJECTS)
    using_github_feed = source_choice == "GitHub sync"

    dataset: List[Dict]
    if source_choice == "GitHub sync":
        dataset = github_repos
        if not github_repos:
            st.info("No repositories tagged with 'portfolio' were found. Showing featured showcase instead.")
            dataset = curated_featured
            source_choice = "Featured showcase"
            using_github_feed = False
    else:
        if featured_candidates:
            dataset = featured_candidates
        else:
            st.info(
                "Tag any repository with both 'portfolio' and 'feature' topics on GitHub to auto-populate this gallery."
            )
            dataset = curated_featured
        using_github_feed = False

    filtered = dataset
    if live_toggle:
        filtered = [repo for repo in dataset if repo.get("homepage")]
        if not filtered:
            st.warning("No live deployments yet for this view. Showing all projects instead.")
            filtered = dataset

    missing_shortlist: List[str] = []
    if using_github_feed and PROJECT_SHORTLIST:
        name_map = {repo.get("name", "").lower(): repo for repo in filtered}
        shortlist_matches: List[Dict] = []
        fallback_matches: List[Dict] = []

        for desired in PROJECT_SHORTLIST:
            key = desired.lower()
            match = name_map.get(key)
            if match:
                shortlist_matches.append(match)
            else:
                hydrated = fetch_repository(username=username, repo_name=desired)
                if hydrated:
                    fallback_matches.append(hydrated)
                else:
                    fallback = shortlist_fallback_map.get(key)
                    if fallback:
                        fallback_matches.append({**fallback})
                    else:
                        missing_shortlist.append(desired)

        if fallback_matches:
            fallback_matches = apply_live_demo_links(fallback_matches)

        if shortlist_matches or fallback_matches:
            filtered = shortlist_matches + fallback_matches

    if missing_shortlist and using_github_feed:
        st.caption(
            "Shortlisted repos not returned in this view: " + ", ".join(missing_shortlist)
        )

    render_project_cards(filtered)
    st.caption(f"{len(filtered)} projects - {source_choice}")

    # st.markdown("""
    #     </div>
    # """, unsafe_allow_html=True)

    return github_repos, filtered


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
        page_title="Shikher Jain Data Scientist & AI/ML Engineer",
        page_icon="assets/logo-SJ.png",
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

    st.markdown("<hr/>", unsafe_allow_html=True)
    _anchor("about")
    _render_about()

    st.markdown("<hr/>", unsafe_allow_html=True)
    _anchor("experience")
    _render_experience()

    st.markdown("<hr/>", unsafe_allow_html=True)
    _render_education_section()

    st.markdown("<hr/>", unsafe_allow_html=True)
    _anchor("skills")
    skills_markup = render_skills(SKILL_GROUPS)
    st.markdown(
        f"""
        <section class='section-shell'>
            <h2>Skills</h2>
            {skills_markup}
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr/>", unsafe_allow_html=True)

    github_repos, showcased_projects = _render_projects(GITHUB_CONFIG["username"], GITHUB_CONFIG["topic"])

    summary_for_stats = dict(gh_summary)
    if github_repos:
        summary_for_stats["total_stars"] = sum(repo.get("stars", 0) for repo in github_repos)
        summary_for_stats["latest_repo"] = github_repos[0].get("name", "")
    else:
        summary_for_stats.setdefault("total_stars", 0)
        summary_for_stats.setdefault("latest_repo", "")


    st.markdown("<hr/>", unsafe_allow_html=True)
    _anchor("github")
    st.subheader("GitHub Snapshot")
    st.markdown("<p class='subtle-subhead'>Contribution activity</p>", unsafe_allow_html=True)

    spotlight_pool = showcased_projects or github_repos
    render_github_stats(summary_for_stats, spotlight_pool)

    st.markdown("<hr/>", unsafe_allow_html=True)
    _render_ml_lab()

    st.markdown("<hr/>", unsafe_allow_html=True)
    _anchor("resume")
    render_resume_section(RESUME)


    st.markdown("<hr/>", unsafe_allow_html=True)
    _anchor("contact")
    render_contact_section(CONTACT)



if __name__ == "__main__":
    main()
