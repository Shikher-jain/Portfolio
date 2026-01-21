"""Skills grid rendering — now using flip-card layout for each skill."""
from textwrap import dedent
from typing import Dict, List
import streamlit as st

# Define a mapping of skill names to their corresponding Simple Icons identifiers
SKILL_ICON_MAP = {
    "Python": "python",
    "Java": "java",
    "C": "c",
    "NumPy": "numpy",
    "Pandas": "pandas",
    "Scikit-learn": "scikitlearn",
    "PyTorch": "pytorch",
    "TensorFlow": "tensorflow",
    "OpenCV": "opencv",
    "MediaPipe": "mediapipe",
    "FastAPI": "fastapi",
    "Flask": "flask",
    "Django": "django",
    "Streamlit": "streamlit",
    "Docker": "docker",
    "Git": "git",
    "GitHub": "github",
    "MySQL": "mysql",
    "SQLite": "sqlite",
    "Postman": "postman",
    "Power BI": "powerbi",
    "Tableau": "tableau",
    "Plotly": "plotly",
    "Matplotlib": "matplotlib",
    "Seaborn": "seaborn",
    "Kaggle": "kaggle",
    "Jupyter Notebook": "jupyter",
    "Google Colab": "googlecolab",
    "Hugging Face": "huggingface",
    "LangChain": "langchain",
    "OpenAI": "openai",
}

DEFAULT_SKILL_ICON = "simpleicons"


def render_skills(skill_groups: List[Dict]) -> str:
    """Render skills grouped by category as flip-cards.

    Front: icon, name, meter. Back: badges/details.
    """
    categories = [group.get("category", "") for group in skill_groups]
    filter_options = ["All"] + categories

    choice = st.selectbox("Filter skill category", filter_options, key="skills-filter")

    groups_to_render = (
        skill_groups if choice == "All" else [group for group in skill_groups if group.get("category") == choice]
    )

    cards: List[str] = []
    for group in groups_to_render:
        flips: List[str] = []
        for item in group.get("skills", []):
            name = item.get("name", "Unnamed")
            badges = item.get("badges", [])
            desc = item.get("description", "")

            icon_key = SKILL_ICON_MAP.get(name, DEFAULT_SKILL_ICON)
            icon_url = f"https://cdn.simpleicons.org/{icon_key}"
            icon_html = (
                f"<img src=\"{icon_url}\" alt=\"{name}\" "
                "class=\"skill-icon-img\" loading=\"lazy\" decoding=\"async\"/>"
            )

            back_badges = "".join(f"<span class='chip'>{b}</span>" for b in badges)

            flips.append(
                dedent(
                    f"""
                    <div class='flip-card'>
                      <div class='flip-inner'>
                        <div class='flip-front'>
                          <div class='skill-row'>
                            <div class='skill-icon'>{icon_html}</div>
                            <div class='skill-meta'>
                              <div class='skill-name'>{name}</div>
                            </div>
                          </div>
                        </div>
                        <div class='flip-back'>
                          <div class='flip-back-inner'>
                            <div class='skill-desc'>{desc}</div>
                            <div class='tag-row'>{back_badges}</div>
                          </div>
                        </div>
                      </div>
                    </div>
                    """
                ).strip()
            )

        cards.append(
            dedent(
                f"""
                <div class='skill-card'>
                  <h4>{group.get('category')}</h4>
                  <div class='flip-grid'>
                    {''.join(flips)}
                  </div>
                </div>
                """
            ).strip()
        )

    return f"<div class='skill-grid'>{''.join(cards)}</div>"


# Function to generate the HTML for skill icons
def generate_skill_icon_html(skill_name):
    """
    Generates an HTML <img> tag for the given skill name using the priority system:
    1. Devicon SVG fallback
    2. SimpleIcons CDN
    3. Generic tech icon fallback

    Args:
        skill_name (str): The name of the skill.

    Returns:
        str: HTML <img> tag as a string.
    """
    icon_name = SKILL_ICON_MAP.get(skill_name, None)
    if icon_name:
        devicon_url = f"https://raw.githubusercontent.com/devicons/devicon/master/icons/{icon_name}/{icon_name}-original.svg"
        simpleicons_url = f"https://cdn.simpleicons.org/{icon_name}"
        return (
            f'<img src="{devicon_url}" '
            f'onerror="this.onerror=null;this.src=\'{simpleicons_url}\';" '
            f'width="22" height="auto" alt="{skill_name} icon">'
        )
    else:
        # Generic tech icon fallback
        return (
            f'<img src="https://cdn.simpleicons.org/technology" '
            f'width="22" height="auto" alt="Generic tech icon">'
        )