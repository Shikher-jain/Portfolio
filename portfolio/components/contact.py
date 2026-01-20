"""Contact surface with socials, forms, and copy helpers."""
from __future__ import annotations

from typing import Dict

import streamlit as st

from .social_icons import get_social_icon_url


def _social_icon_html(label: str) -> str:
    icon_url = get_social_icon_url(label)
    return f"<span class='social-icon'><img src='{icon_url}' alt='{label} icon' loading='lazy' /></span>"


def render_contact_section(contact: Dict) -> None:
    socials_html = "".join(
        f"<a class='social-pill' href='{url}' target='_blank' rel='noopener'>{_social_icon_html(name)}<span>{name}</span></a>"
        for name, url in contact.get('socials', {}).items()
    )
    st.markdown(
        f"""
        <div class='contact-card'>
            <div>
                <p class='eyebrow'>Based in</p>
                <h3>{contact.get('location')}</h3>
                <p>{contact.get('availability', 'Currently onboarding new AI initiatives.')}</p>
                <div class='contact-chip-row'>
                    <button class='ghost-btn copy-btn' data-copy='{contact.get('email')}'>Copy Email</button>
                    <a class='ghost-btn' href='{contact.get('calendly')}' target='_blank' rel='noopener'>Schedule a call</a>
                </div>
                <div class='social-list'>{socials_html}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("contact-form", clear_on_submit=True):
        st.write("### Contact Form")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("How can I help?", height=140)
        submitted = st.form_submit_button("Send message")
        if submitted:
            if not (name and email and message):
                st.error("Please complete all fields before sending.")
            else:
                st.success("Thanks for reaching out! I will reply within 2 business days.")

    st.markdown(
        """
        <script>
        document.addEventListener('DOMContentLoaded', () => {
            const copyButtons = document.querySelectorAll('.copy-btn');
            copyButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    navigator.clipboard.writeText(btn.dataset.copy);
                    btn.innerText = 'Copied ✔';
                    setTimeout(() => (btn.innerText = 'Copy Email'), 2000);
                });
            });
        });
        </script>
        """,
        unsafe_allow_html=True,
    )

