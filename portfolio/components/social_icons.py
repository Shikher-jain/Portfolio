"""Shared helpers for rendering platform icons."""
from __future__ import annotations

SOCIAL_ICON_MAP = {
    "linkedin": "https://cdn.simpleicons.org/linkedin/0A66C2",
    "youtube": "https://cdn.simpleicons.org/youtube/FF0000",
    "kaggle": "https://cdn.simpleicons.org/kaggle/20BEFF",
    "leetcode": "https://cdn.simpleicons.org/leetcode/F89F1B",
    "hackerrank": "https://cdn.simpleicons.org/hackerrank/00EA64",
    "geeksforgeeks": "https://cdn.simpleicons.org/geeksforgeeks/2F8D46",
    "github": "https://cdn.simpleicons.org/github/FFFFFF",
    "hugging face": "https://cdn.simpleicons.org/huggingface/FFAA1D",
    "google cloud": "https://cdn.simpleicons.org/googlecloud/4285F4",
    "credly": "https://cdn.simpleicons.org/credly/FF6B00",
    "instagram": "https://cdn.simpleicons.org/instagram/E4405F",
    "twitter": "https://cdn.simpleicons.org/x/FFFFFF",
    "stack overflow": "https://cdn.simpleicons.org/stackoverflow/F58025",
    "streamlit": "https://cdn.simpleicons.org/streamlit/FF4B4B",
    "resume": "https://cdn.simpleicons.org/file/9CA3AF",
}

DEFAULT_ICON_URL = "https://cdn.simpleicons.org/link/9CA3AF"


def get_social_icon_url(label: str) -> str:
    """Return icon URL for a given social/platform label."""
    lower = label.lower()
    for key, url in SOCIAL_ICON_MAP.items():
        if key in lower:
            return url
    return DEFAULT_ICON_URL
