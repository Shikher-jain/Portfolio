"""Shared helpers for rendering platform icons."""
from __future__ import annotations

SOCIAL_ICON_MAP = {
    "linkedin": "https://img.icons8.com/ios-filled/50/linkedin.png",
    "youtube": "https://cdn.simpleicons.org/youtube/FF0000",
    "kaggle": "https://cdn.simpleicons.org/kaggle/20BEFF",
    "leetcode": "https://cdn.simpleicons.org/leetcode/F89F1B",
    "hackerrank": "https://cdn.simpleicons.org/hackerrank/00EA64",
    "geeksforgeeks": "https://cdn.simpleicons.org/geeksforgeeks/2F8D46",
    "github": "https://img.icons8.com/ios-glyphs/50/github.png",

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
DEFAULT_FALLBACK_ICON_URL = "https://img.icons8.com/ios-filled/50/link--v1.png"

SOCIAL_FALLBACK_ICON_MAP = {
    "linkedin": "https://img.icons8.com/ios-filled/50/linkedin.png",
    "youtube": "https://img.icons8.com/ios-filled/50/youtube-play.png",
    "kaggle": "https://img.icons8.com/ios-filled/50/experimental-kaggle-an-external-company-an-online-community-of-data-scientists-and-machine-learners-owned-by-google-icons8.png",
    "leetcode": "https://img.icons8.com/ios-filled/50/code.png",
    "hackerrank": "https://img.icons8.com/ios-filled/50/code.png",
    "geeksforgeeks": "https://img.icons8.com/ios-filled/50/code.png",
    "github": "https://img.icons8.com/ios-glyphs/50/github.png",
    "hugging face": "https://img.icons8.com/emoji/48/hugging-face.png",
    "google cloud": "https://img.icons8.com/fluency/48/google-cloud.png",
    "credly": "https://img.icons8.com/ios-filled/50/badge.png",
    "instagram": "https://img.icons8.com/ios-filled/50/instagram-new.png",
    "twitter": "https://img.icons8.com/ios-filled/50/twitterx--v1.png",
    "stack overflow": "https://img.icons8.com/ios-filled/50/stack-overflow.png",
    "streamlit": "https://img.icons8.com/ios-filled/50/dashboard-layout.png",
    "resume": "https://img.icons8.com/ios-filled/50/document--v1.png",
}


def get_social_icon_url(label: str) -> str:
    """Return icon URL for a given social/platform label."""
    lower = label.lower()
    for key, url in SOCIAL_ICON_MAP.items():
        if key in lower:
            return url
    return DEFAULT_ICON_URL


def get_social_icon_fallback_url(label: str) -> str:
    """Return fallback icon URL for a given social/platform label."""
    lower = label.lower()
    for key, url in SOCIAL_FALLBACK_ICON_MAP.items():
        if key in lower:
            return url
    return DEFAULT_FALLBACK_ICON_URL


def get_social_icon_img_tag(label: str, alt: str, extra_attrs: str = "") -> str:
    """Return an img tag with primary URL and fallback on error."""
    primary = get_social_icon_url(label)
    fallback = get_social_icon_fallback_url(label)
    attrs = f" {extra_attrs.strip()}" if extra_attrs.strip() else ""
    return (
        f"<img src='{primary}' alt='{alt}' loading='lazy' "
        f"onerror=\"this.onerror=null;this.src='{fallback}';\"{attrs} />"
    )
