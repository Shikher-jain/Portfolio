"""Central registry for live deployment URLs per repository."""
from __future__ import annotations

from typing import Dict, List

# Map repository names (case-insensitive) to their deployed Streamlit URLs.
# Update this dictionary whenever you ship a new live demo.
LIVE_DEMOS = {
    "sahayak_ai": "https://sahayak-sj-09.streamlit.app/",
    "streamlit-ipl-app": "https://shikherjain09ipldata.streamlit.app/",
    "next-word-prediction-tp35": "https://tp35-next-word-prediction.streamlit.app/",
    "india_census_app": "https://shikherjain09censusapp.streamlit.app/",
    "genai": "https://shikherjain09skilladvicer.streamlit.app/",
    "gdp-dashboard": "https://shikherjain09gpd-dashboard.streamlit.app/",
    "chatbot": "https://aahikherjain09chatbot.streamlit.app/",
    "attendease": "https://attendease-shikher-09.streamlit.app/",
    "ai_for_good": "https://ai-housing-inspection-sj-0906.streamlit.app/",
    "ai_for_good_hackathon": "https://ai-housing-inspection-sj-09.streamlit.app/",
    "weather-app": "https://shikherjain09weatherapp.streamlit.app/"
}


def apply_live_demo_links(projects: List[Dict]) -> List[Dict]:
    """Attach live demo URLs to project dictionaries when available."""
    enriched: List[Dict] = []
    for project in projects:
        record = dict(project)
        repo_name = (record.get("name") or "").lower()
        live_url = LIVE_DEMOS.get(repo_name)
        if live_url and not record.get("homepage"):
            record["homepage"] = live_url
        enriched.append(record)
    return enriched
