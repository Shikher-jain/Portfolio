"""Contact surface with socials, forms, and copy helpers."""
from __future__ import annotations

import html
from typing import Dict
import streamlit as st
from .social_icons import get_social_icon_url
import mysql.connector
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


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
                # Insert data into the MySQL database
                conn = get_db_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO contact_form (name, email, message) VALUES (%s, %s, %s)",
                        (name, email, message)
                    )
                    conn.commit()
                    conn.close()

                    st.success("Thanks for reaching out! I will reply within 2 business days.")

# ====================================================================
# MySQL database configuration using environment variables
# ====================================================================

# DB_CONFIG = {
#     "host": os.getenv("DB_HOST", "localhost"),
#     "user": os.getenv("DB_USER", "root"),
#     "password": os.getenv("DB_PASSWORD", ""),
#     "database": os.getenv("DB_NAME", "portfolio")
# }


# ====================================================================
# Use Streamlit secrets for database configuration
# ====================================================================
DB_CONFIG = {
    "host": st.secrets["DB_HOST"],
    "user": st.secrets["DB_USER"],
    "password": st.secrets["DB_PASSWORD"],
    "database": st.secrets["DB_NAME"]
}


# Establish a connection to the MySQL database with error handling
def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        logging.error(f"Database connection failed: {err}")
        st.error("Unable to connect to the database. Please try again later.")
        return None

# Ensure the table exists with error handling
try:
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contact_form (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        conn.close()
except mysql.connector.Error as err:
    logging.error(f"Failed to ensure table exists: {err}")
    st.error("Database setup failed. Please contact support.")
