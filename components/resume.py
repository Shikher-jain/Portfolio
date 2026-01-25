from __future__ import annotations

import base64
from functools import lru_cache
from pathlib import Path
from typing import Dict

import streamlit as st

@lru_cache(maxsize=1)
def load_resume_base64(resume_path: str) -> str | None:
    path = Path(resume_path)
    if not path.exists():
        st.error("Resume file is missing. Please add it to the specified path and refresh.")
        return None
    with path.open("rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")
    


def render_resume_section(resume: Dict) -> None:
    b64_pdf = load_resume_base64(resume.get("path", ""))
    if not b64_pdf:
        st.error("Resume file is missing. Please add it to assets/ and refresh.")
        return

    st.markdown(
        f"""
        <div class='resume-card'>
            <div>
                <p class='eyebrow'>Resume</p>
                <h3>{resume.get('file_name')}</h3>
                <p>{resume.get('tagline')}</p>
                <small>Updated {resume.get('last_updated')}</small>
                <div class='resume-actions'>
                    <a class='solid-btn' href='data:application/pdf;base64,{b64_pdf}' download='{resume.get('file_name')}'>Download</a>
                </div>
            </div>
            <iframe src='data:application/pdf;base64,{b64_pdf}' title='Resume preview'></iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_floating_cta(resume: Dict) -> None:
    resume_url = "https://raw.githubusercontent.com/Shikher-jain/Portfolio/main/assets/resume.pdf"  # Raw file URL

    st.markdown(
        f"""
        <a class='floating-resume-cta' href='{resume_url}' download='{resume.get('file_name')}'>
            ⬇ Resume
        </a>
        """,
        unsafe_allow_html=True,
    )
