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
from components.resume import render_resume_section
from components.skills import render_skills
from components.social_icons import get_social_icon_img_tag
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
    RESUMES,
    SKILL_GROUPS,
)

from github_api import fetch_github_summary, fetch_portfolio_repositories, fetch_repository
from live_demos import apply_live_demo_links

NAV_ITEMS = [
    ("hero", "Hero"),
    ("about", "About"),
    ("experience", "Experience"),
    ("education", "Education"),
    ("skills", "Skills"),
    ("projects", "Projects"),
    ("github", "GitHub"),
    ("social_Links", "Social Links"),
    ("lab", "ML Lab"),
    ("resume", "Resume"),
    ("contact", "Contact"),
]

def _load_css() -> None:
    # Load and apply custom CSS styles for the app.
    css_path = Path(__file__).parent / "styles" / "style.css"
    with css_path.open("r", encoding="utf-8") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

def _ensure_assets() -> None:
    # Ensure essential assets like profile picture and resume exist.
    assets_dir = Path(__file__).parent / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Ensure profile picture exists
    avatar_path = assets_dir / "profile.png"
    if not avatar_path.exists() or avatar_path.stat().st_size == 0:
        placeholder_avatar = (
            "iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAACENnwnAAAAD0lEQVR42mNk+M/AwMAAAjUAmzquw3YAAAAASUVORK5CYII="
        )
        avatar_path.write_bytes(base64.b64decode(placeholder_avatar))

    # Ensure logo exists
    logo_path = assets_dir / "logo.png"
    if not logo_path.exists() or logo_path.stat().st_size == 0:
        placeholder_logo = (
            "iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAQAAACENnwnAAAAD0lEQVR42mNk+M/AwMAAAjUAmzquw3YAAAAASUVORK5CYII="
        )
        logo_path.write_bytes(base64.b64decode(placeholder_logo))

    # Ensure resume exists
    resume_path = assets_dir / "resume.pdf"
    if not resume_path.exists() or resume_path.stat().st_size == 0:
        # Placeholder for resume handling logic.
        pass

def _image_data_uri(path_str: str) -> str:
    # Convert image file to a data URI for embedding in HTML.
    path = Path(path_str)
    if path.exists():
        mime_type = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        with path.open("rb") as image_file:
            base64_data = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:{mime_type};base64,{base64_data}"
    return path_str

def _render_nav() -> None:
    # Render the navigation bar with links to different sections.
    links = "".join(f"<a href='#{slug}'>{label}</a>" for slug, label in NAV_ITEMS)
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
    # Add an anchor for navigation to specific sections.
    st.markdown(f"<span id='{slug}' class='section-anchor'></span>", unsafe_allow_html=True)


def _divider() -> None:
    st.markdown("<hr/>", unsafe_allow_html=True)

def _render_hero(summary: Dict) -> None:
    # Render the hero section with profile details and stats.
    hero_stats = "".join(
        f"<div class='stat-tile'><p class='eyebrow'>{stat['label']}</p><h3>{stat['value']}</h3></div>"
        for stat in PROFILE["hero_stats"]
    )
    resume_btn = "<a class='solid-btn' href='#resume'>Download Resume</a>"
    email = PROFILE.get("email", "")
    calendly = CONTACT.get("calendly", "#")
    linkedin_url = PROFILE.get("socials", {}).get("LinkedIn", "#")
    github_url = PROFILE.get("socials", {}).get("GitHub", "#")
    linkedin_icon = get_social_icon_img_tag("LinkedIn", "LinkedIn icon")
    github_icon = get_social_icon_img_tag("GitHub", "GitHub icon")
    hero_contact_ctas = (
        f"<a class='ghost-btn' href='mailto:{email}?subject=Hello%20Shikher' target='_blank' rel='noopener noreferrer'>Send Email</a>"
        "<a class='ghost-btn' href='#contact'>Contact Me</a>"
        f"<a class='ghost-btn' href='{calendly}' target='_blank' rel='noopener'>Schedule a call</a>"
        f"<a class='ghost-btn hero-cta' href='{linkedin_url}' target='_blank' rel='noopener'>"
        f"<span class='social-icon'>{linkedin_icon}</span>"
        "<span>LinkedIn</span>"
        "</a>"
        f"<a class='ghost-btn hero-cta' href='{github_url}' target='_blank' rel='noopener'>"
        f"<span class='social-icon'>{github_icon}</span>"
        "<span>GitHub</span>"
        "</a>"
    )
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
                        <h1>{PROFILE['name']}</h1>
                        <p class='hero-bio'>{PROFILE['tagline']}</p>
                        <div class='hero-actions'>{resume_btn}{hero_contact_ctas}</div>
                    </div>
                </div>
            <!--    <div class='hero-stats'>{hero_stats}</div>  -->
            </div>
            <div class='hero-meta-panel'>{hero_meta}</div>
        </section>
        """
    ).strip()
    st.markdown(hero_markup, unsafe_allow_html=True)

def _render_about() -> None:
    # Render the about section with personal highlights and focus areas.
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
    # Render the experience section with work history.
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
    # Render the education section with degrees and certifications.
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


def _render_skills_section() -> None:
    """Render the skills section shell and skill cards."""
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

def _render_projects(username: str, topic: str) -> tuple[List[Dict], List[Dict]]:
    # Render the projects section with GitHub repositories and featured projects.

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

    return github_repos, filtered


def _normalize_text(text: str) -> str:
    return " ".join((text or "").lower().split())


def _contains_term(text: str, term: str, aliases: dict[str, list[str]]) -> bool:
    candidates = [term] + aliases.get(term, [])
    for candidate in candidates:
        pattern = rf"\b{re.escape(candidate.lower())}\b"
        if re.search(pattern, text):
            return True
    return False


def _jaccard_similarity(left: str, right: str) -> float:
    left_tokens = set(re.findall(r"[a-zA-Z0-9+\-#\.]+", left.lower()))
    right_tokens = set(re.findall(r"[a-zA-Z0-9+\-#\.]+", right.lower()))
    if not left_tokens or not right_tokens:
        return 0.0
    union = left_tokens | right_tokens
    if not union:
        return 0.0
    return (len(left_tokens & right_tokens) / len(union)) * 100.0

def _render_ml_lab() -> None:
    # Render the ML Lab section with advanced role-based resume matching.
    st.subheader("ML Lab — Advanced Resume Matcher")
    resume_cfg = ML_LAB["resume"]
    st.caption(resume_cfg["description"])

    roles = resume_cfg.get("roles", {})
    if not roles:
        st.warning("No role profiles configured for ML Lab.")
        return

    role_name = st.selectbox("Target role", list(roles.keys()), key="resume-role")
    role_profile = roles[role_name]
    weights = role_profile.get("weights", {})
    aliases = role_profile.get("aliases", {})
    must_have = role_profile.get("must_have", [])

    resume_text = st.text_area(
        "Resume snippet",
        value="Architected PyTorch transformers with Vertex pipelines.",
        placeholder=resume_cfg["placeholder"],
        key="resume-input",
    )

    jd_text = st.text_area(
        "Job description (optional)",
        value="",
        placeholder=resume_cfg.get("jd_placeholder", "Paste JD to compare alignment..."),
        key="jd-input",
    )

    if st.button("Analyze resume", key="resume-btn"):
        normalized_resume = _normalize_text(resume_text)
        if not normalized_resume:
            st.warning("Please provide a resume snippet.")
            return

        matched_skills: list[str] = []
        missing_skills: list[str] = []
        matched_weight = 0
        total_weight = sum(int(value) for value in weights.values()) or 1

        for skill, weight in weights.items():
            if _contains_term(normalized_resume, skill, aliases):
                matched_skills.append(skill)
                matched_weight += int(weight)
            else:
                missing_skills.append(skill)

        weighted_score = (matched_weight / total_weight) * 100
        jd_score = _jaccard_similarity(normalized_resume, jd_text) if jd_text.strip() else 0.0
        final_score = weighted_score if not jd_text.strip() else (0.75 * weighted_score + 0.25 * jd_score)

        metrics_cols = st.columns(3)
        with metrics_cols[0]:
            st.metric("Weighted Skill Score", f"{weighted_score:.1f}%")
        with metrics_cols[1]:
            st.metric("JD Alignment", f"{jd_score:.1f}%")
        with metrics_cols[2]:
            st.metric("Final Match", f"{final_score:.1f}%")

        st.progress(min(max(final_score / 100.0, 0.0), 1.0))

        missing_must_have = [item for item in must_have if item in missing_skills]
        top_strengths = sorted(matched_skills, key=lambda item: weights.get(item, 0), reverse=True)[:6]
        top_gaps = sorted(missing_skills, key=lambda item: weights.get(item, 0), reverse=True)[:6]

        st.write(f"Detected skills: {len(matched_skills)} / {len(weights)}")
        if top_strengths:
            st.success("Top strengths: " + ", ".join(top_strengths))
        if missing_must_have:
            st.error("Critical gaps: " + ", ".join(missing_must_have))
        if top_gaps:
            st.info("Recommended next skills: " + ", ".join(top_gaps))


def _render_social_links_expander() -> None:
    """Render all social links as a responsive visible section."""
    social_dict = PROFILE.get("socials", {})
    labels = list(social_dict.keys())
    if not labels:
        st.info("No social links available.")
        return

    cards_list: List[str] = []
    for label in labels:
        is_resume = "resume" in label.lower()
        href = "#resume" if is_resume else social_dict[label]
        rel_attr = "noopener" if not is_resume else ""
        target_attr = "_blank" if not is_resume else "_self"
        cta_text = "Choose Resume" if is_resume else f"Open {label}"

        cards_list.append(
            dedent(
                f"""
                <div class='social-card'>
                    {get_social_icon_img_tag(label, f'{label} icon', "style='height:28px;width:28px;'")}
                    <h4>{label}</h4>
                    <div class='card-actions'>
                        <a class='solid-btn' href='{href}' target='{target_attr}' rel='{rel_attr}'>{cta_text}</a>
                    </div>
                </div>
                """
            ).strip()
        )

    cards = "".join(cards_list)
    st.markdown(
        f"""
        <section class='section-shell'>
            <h2>Social Links</h2>
            <div class='social-grid'>{cards}</div>
        </section>
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

    _divider()
    _anchor("about")
    _render_about()

    _divider()
    _anchor("experience")
    _render_experience()

    _divider()
    _anchor("education")
    _render_education_section()

    _divider()
    _anchor("skills")
    _render_skills_section()

    _divider()

    _anchor("projects")
    github_repos, showcased_projects = _render_projects(GITHUB_CONFIG["username"], GITHUB_CONFIG["topic"])

    summary_for_stats = dict(gh_summary)
    if github_repos:
        summary_for_stats["total_stars"] = sum(repo.get("stars", 0) for repo in github_repos)
        summary_for_stats["latest_repo"] = github_repos[0].get("name", "")
    else:
        summary_for_stats.setdefault("total_stars", 0)
        summary_for_stats.setdefault("latest_repo", "")

    _divider()
    _anchor("github")
    st.subheader("GitHub Snapshot")
    st.markdown("<p class='subtle-subhead'>Contribution activity</p>", unsafe_allow_html=True)

    spotlight_pool = showcased_projects or github_repos
    render_github_stats(summary_for_stats, spotlight_pool)


    _divider()
    _anchor("lab")
    _render_ml_lab()

    _divider()
    _anchor("resume")
    render_resume_section(RESUMES)

    _anchor("social_Links")
    _render_social_links_expander()

    _divider()
    _anchor("contact")
    render_contact_section(CONTACT)

if __name__ == "__main__":
    main()
