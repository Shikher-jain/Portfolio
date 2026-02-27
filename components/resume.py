from __future__ import annotations

import base64
from functools import lru_cache
from pathlib import Path
from typing import Any

import streamlit as st


@lru_cache(maxsize=16)
def load_resume_base64(resume_path: str) -> str | None:
    path = Path(resume_path)
    if not path.exists():
        st.error("Resume file is missing. Please add it to the specified path and refresh.")
        return None
    with path.open("rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")


def _render_single_resume_card(resume: dict[str, Any]) -> None:
    b64_pdf = load_resume_base64(resume.get("path", ""))

    if not b64_pdf:
        st.error("Resume file is missing. Please add it to assets/ and refresh.")
        return

    st.markdown(
        f"""
        <section class='section-shell'>
        <div class='resume-card'>
            <div>
                <p class='eyebrow'>Resume</p>
                <h3>{resume.get('file_name')}</h3>
                <p>{resume.get('tagline')}</p>
                <small>Updated {resume.get('last_updated')}</small>
            </div>
            <iframe src='data:application/pdf;base64,{b64_pdf}' title='Resume preview'></iframe>
        </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_resume_section(resume: dict[str, Any] | list[dict[str, Any]]) -> None:
    if isinstance(resume, list):
        valid_resumes = [item for item in resume if isinstance(item, dict) and item.get("path")]
        if not valid_resumes:
            st.error("No resume entries found. Please configure resume paths in data.py.")
            return

        if len(valid_resumes) == 1:
            _render_single_resume_card(valid_resumes[0])
            return

        slide_key = "resume-carousel-index"
        if slide_key not in st.session_state:
            st.session_state[slide_key] = 0

        total_slides = len(valid_resumes)
        st.session_state[slide_key] = st.session_state[slide_key] % total_slides

        prev_col, status_col, next_col = st.columns([1, 2, 1])
        with prev_col:
            if st.button("◀ Previous", key="resume-carousel-prev"):
                st.session_state[slide_key] = (st.session_state[slide_key] - 1 + total_slides) % total_slides
        with status_col:
            current_idx = st.session_state[slide_key]
            current_name = valid_resumes[current_idx].get("file_name", f"Resume {current_idx + 1}")
            st.markdown(
                f"<p style='text-align:center; margin-top:0.6rem;'><strong>{current_name}</strong>"
                f" &nbsp;|&nbsp; Slide {current_idx + 1} of {len(valid_resumes)}</p>",
                unsafe_allow_html=True,
            )
        with next_col:
            if st.button("Next ▶", key="resume-carousel-next"):
                st.session_state[slide_key] = (st.session_state[slide_key] + 1) % total_slides

        st.session_state[slide_key] = st.session_state[slide_key] % total_slides
        active_resume = valid_resumes[st.session_state[slide_key]]
        active_b64 = load_resume_base64(active_resume.get("path", ""))
        if active_b64:
            st.download_button(
                label="Download current resume",
                data=base64.b64decode(active_b64),
                file_name=active_resume.get("file_name", "resume.pdf"),
                mime="application/pdf",
                key="resume-download-current",
            )

        _render_single_resume_card(active_resume)
        return

    _render_single_resume_card(resume)
