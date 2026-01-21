"""Contact surface with socials, forms, and copy helpers."""
from __future__ import annotations

import html
from typing import Dict
import streamlit as st
from .social_icons import get_social_icon_url
import sqlite3
import atexit
import threading


def _social_icon_html(label: str) -> str:
    icon_url = get_social_icon_url(label)
    return f"<span class='social-icon'><img src='{icon_url}' alt='{label} icon' loading='lazy' /></span>"


def render_contact_section(contact: dict[str, str]) -> None:
    location = html.escape(contact.get("location", "Remote"))
    availability = html.escape(contact.get("availability", "Currently onboarding new AI initiatives."))
    email = html.escape(contact.get("email", "shikherjain786@gmail.com"))
    calendly = html.escape(contact.get("calendly", "#"))

    socials_html = "".join(
        f"<a class='social-pill' href='{html.escape(url)}' target='_blank' rel='noopener'>"
        f"{_social_icon_html(name)}<span>{html.escape(name)}</span></a>"
        for name, url in contact.get('socials', {}).items()
    )

    st.markdown(
        f"""
        <div class='contact-card'>
            <div>
                <p class='eyebrow'>Based in</p>
                <h3>{location}</h3>
                <p>{availability}</p>
                <div class='contact-chip-row'>
                    <a class="ghost-btn"
                    href="mailto:{email}?subject=Hello%20Shikher"
                    target="_blank"
                    rel="noopener noreferrer"
                    aria-label="Send email">
                    Send Email
                    </a>
                    <a class='ghost-btn'
                       href='{calendly}'
                       target='_blank'
                       rel='noopener'>
                       Schedule a call
                    </a>
                </div>
                <div class='social-list'>{socials_html}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,  # Ensure raw HTML is rendered
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
                # Get a thread-local database connection
                conn = get_db_connection()
                cursor = conn.cursor()

                # Insert data into the database
                cursor.execute(
                    "INSERT INTO contact_form (name, email, message) VALUES (?, ?, ?)",
                    (name, email, message)
                )
                conn.commit()

                st.success("Thanks for reaching out! I will reply within 2 business days.")

# Use thread-local storage for SQLite connections
thread_local = threading.local()

def get_db_connection():
    if not hasattr(thread_local, "connection"):
        thread_local.connection = sqlite3.connect(DB_PATH, check_same_thread=False)
    return thread_local.connection

# Initialize database connection
DB_PATH = "contact_form.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS contact_form (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
)
conn.commit()

# Register a function to close the database connection at exit
atexit.register(lambda: conn.close())
