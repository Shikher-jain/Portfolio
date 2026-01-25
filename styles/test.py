import streamlit as st

st.set_page_config(page_title="Shikher Jain | Portfolio", layout="wide")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

location = "Agra, Uttar Pradesh, India"
availability = "Available for Internships & Full-Time Roles"
email = "shikherjain786@gmail.com"
calendly = "https://calendly.com/your-link"

st.markdown(
    f"""
    <section class="section-shell">
        <div class="contact-card">
            <p class="eyebrow">Based in</p>
            <h3>{location}</h3>
            <p>{availability}</p>
            <div class="contact-chip-row">
                <a class="ghost-btn"
                   href="mailto:{email}?subject=Hello%20Shikher"
                   target="_blank">
                   Send Email
                </a>
                <a class="ghost-btn"
                   href="mailto:{email}?subject=Portfolio%20Inquiry&body=Hi%20Shikher,%0A%0AI%20came%20across%20your%20portfolio%20and%20would%20like%20to%20connect.%0A%0ARegards,">
                   Contact Me
                </a>
                <a href="mailto:{email}?subject=Portfolio%20Inquiry&amp;body=Hi%20Shikher,%0A%0AI%20came%20across%20your%20portfolio%20and%20would%20like%20to%20connect.%0A%0ARegards,"
                       target="_blank"
                       rel="noopener noreferrer">
                       Contact Me
                    </a>
                <a class="ghost-btn"
                   href="{calendly}"
                   target="_blank">
                   Schedule a Call
                </a>
            </div>  
            </div>
            <div class="social-list">
                <a href="https://www.linkedin.com/in/shikher-jain-0bb8a8259/" target="_blank">LinkedIn</a>
                <a href="https://github.com/Shikher-jain" target="_blank">GitHub</a>
                <a href="https://leetcode.com/u/shikherJain09/" target="_blank">LeetCode</a>
                <a href="https://www.kaggle.com/shikherjain" target="_blank">Kaggle</a>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True
)

st.markdown('''<a class='floating-resume-cta' href='data:application/pdf;base64,{b64_pdf}' download='{resume.get('file_name')}'>⬇ Resume</a>''', unsafe_allow_html=True)
