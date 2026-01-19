"""Structured profile metadata consumed by the Streamlit portfolio app."""
from datetime import date

PROFILE = {
    "name": "Shikher Jain",
    "role": "Data Scientist & AI/ML Engineer",
    "tagline": "Entry-level ML engineer crafting RAG, vision, and NLP systems end to end.",
    "location": "Agra, Uttar Pradesh, India",
    "experience": "B.Tech CSE · Class of 2026",
    "email": "shikherjain786@gmail.com",
    "availability": "Open to data science internships, AI/ML fellowships, and freelance builds",
    "avatar": "assets/profile.png",
    "hero_stats": [
        {"label": "Projects Shipped", "value": "8+"},
        {"label": "Models Deployed", "value": "12"},
        {"label": "TCS CodeVita Rank", "value": "1040"}
    ],
    "socials": {
        "GitHub": "https://github.com/Shikher-jain",
        "LinkedIn": "https://www.linkedin.com/in/shikher-jain-0bb8a8259/",
        "Kaggle": "https://www.kaggle.com/shikherjain",
        "Resume": "assets/resume.pdf"
    }
}

ABOUT = {
    "headline": (
        "Entry-level Data Scientist and AI/ML Engineer with hands-on experience in developing and deploying ML and DL "
        "solutions. Skilled in data preprocessing, EDA, feature engineering, NLP, and computer vision with Python, PyTorch, "
        "and scikit-learn across RESTful and cloud-integrated systems."
    ),
    "highlights": [
        "Build end-to-end AI workflows that move from exploratory notebooks into production-ready APIs and dashboards.",
        "Comfortable with transformer-based NLP, embeddings, and MediaPipe/OpenCV pipelines for real-time insights.",
        "Experienced with data preprocessing, EDA, and feature engineering that keep downstream models stable and accurate."
    ],
    "focus": [
        "Data Preprocessing & Feature Engineering",
        "NLP & Transformer Pipelines",
        "Computer Vision & Real-time Analytics",
        "RESTful ML APIs on Cloud"
    ]
}
EXPERIENCE = [
        {
            "role": "Data Science Intern",
            "company": "Novas Arc Consulting Pvt. Ltd.",
            "location": "Remote",
            "date": "Aug 2025 – Nov 2025",
            "highlights": [
                "Systematized an FAQ extraction pipeline for 100+ web pages, reducing manual effort by 60%.",
                "Built an NLP-based context analyzer to classify intent, tone, persona, domain, and age group, enhancing prompt relevance.",
                "Fine-tuned OpenAI GPT-3.5 Turbo on custom datasets, improving response relevance by 20–30% per internal evaluation.",
                "Deployed a training-data–driven AI chatbot with iterative testing and logic refinement, reducing inconsistent responses.",
                "Processed 10k+ text records for training and evaluation pipelines, ensuring high-quality model inputs."
            ],
            "stack": ["NLP", "GPT-3.5 Turbo", "FastAPI", "LangChain", "Prompt Engineering"]
        }
    ]


EXPERIENCE = [
    {
        "role": "Data Science Intern",
        "company": "Novas Arc Consulting Pvt. Ltd.",
        "location": "Remote",
        "date": "Aug 2025 – Nov 2025",
        "highlights": [
            "Systematized an FAQ extraction pipeline for 100+ web pages, reducing manual effort by 60%.",
            "Built an NLP-based context analyzer to classify intent, tone, persona, domain, and age group, boosting prompt relevance.",
            "Fine-tuned OpenAI GPT-3.5 Turbo on custom datasets, improving response relevance by up to 30% in review cycles.",
            "Deployed a training-data–driven AI chatbot with iterative testing and logic refinement to cut inconsistent replies.",
            "Processed 10k+ text records for training and evaluation pipelines to maintain high-quality model inputs."
        ],
        "stack": ["NLP", "GPT-3.5 Turbo", "FastAPI", "LangChain", "Prompt Engineering"]
    }
]

SKILL_GROUPS = [
    {
        "category": "Programming Languages",
        "skills": [
            {"name": "Python", "level": 95, "badges": ["NumPy", "Pandas"]},
            {"name": "Java", "level": 78, "badges": ["DSA", "Backend"]},
            {"name": "C", "level": 74, "badges": ["Systems", "Pointers"]}
        ]
    },
    {
        "category": "ML & Data Science",
        "skills": [
            {"name": "Data Preprocessing", "level": 90, "badges": ["Cleaning", "Pipelines"]},
            {"name": "EDA & Feature Eng.", "level": 88, "badges": ["EDA", "Feature Scaling"]},
            {"name": "scikit-learn", "level": 86, "badges": ["Modeling", "Evaluation"]}
        ]
    },
    {
        "category": "Deep Learning & NLP",
        "skills": [
            {"name": "PyTorch", "level": 92, "badges": ["Neural Nets", "Optimization"]},
            {"name": "Transformer Models", "level": 85, "badges": ["Embeddings", "LoRA"]},
            {"name": "NLP Pipelines", "level": 84, "badges": ["Tokenization", "Prompting"]}
        ]
    },
    {
        "category": "Computer Vision",
        "skills": [
            {"name": "OpenCV", "level": 90, "badges": ["Real-time", "LBPH"]},
            {"name": "MediaPipe", "level": 82, "badges": ["Pose", "Holistic"]},
            {"name": "Face & Pose Systems", "level": 80, "badges": ["Recognition", "Tracking"]}
        ]
    },
    {
        "category": "Data Viz & Analytics",
        "skills": [
            {"name": "Matplotlib / Seaborn", "level": 82, "badges": ["Explainers", "Dashboards"]},
            {"name": "Plotly", "level": 80, "badges": ["Interactive", "Maps"]},
            {"name": "Tableau / Power BI", "level": 75, "badges": ["Storyboards", "KPIs"]}
        ]
    },
    {
        "category": "Web & APIs",
        "skills": [
            {"name": "FastAPI", "level": 85, "badges": ["REST", "Async"]},
            {"name": "Flask", "level": 80, "badges": ["Microservices"]},
            {"name": "Streamlit", "level": 88, "badges": ["ML Demos"]}
        ]
    },
    {
        "category": "Data Platforms & Tools",
        "skills": [
            {"name": "MySQL / SQLite", "level": 82, "badges": ["Schema Design", "Queries"]},
            {"name": "Git, GitHub, Docker", "level": 84, "badges": ["CI", "Containers"]},
            {"name": "Jupyter / Colab / Kaggle", "level": 80, "badges": ["Notebooks", "Experiments"]}
        ]
    },
    {
        "category": "Applied Math & Logic",
        "skills": [
            {"name": "Linear Algebra", "level": 78, "badges": ["Vectors", "Matrices"]},
            {"name": "Probability & Statistics", "level": 82, "badges": ["Distributions", "Inference"]},
            {"name": "Rule-based Modeling", "level": 76, "badges": ["Logic", "Constraints"]}
        ]
    }
]

EDUCATION = [
    {
        "institution": "Faculty of Engineering and Technology, Agra College (AKTU)",
        "degree": "B.Tech in Computer Science and Engineering",
        "period": "2022–2026",
        "details": "CGPA: 7.78 / 10"
    }
]

CERTIFICATIONS = [
    "TCS CodeVita Season 12 – Global Rank 1040",
    "Geodata Processing (Python & ML) – ISRO–IIRS",
    "Machine Learning – Softpro India (AKTU)",
    "HP LIFE – Data Science & Analytics",
    "Python Programming – DataFlair",
    "Python – HackerRank",
    "Event Coordinator – Cryptic Coder"
]

CONTACT = {
    "email": PROFILE["email"],
    "location": PROFILE["location"],
    "phone": "+91 74520 17544",
    "availability": PROFILE["availability"],
    "socials": PROFILE["socials"],
    "calendly": "https://calendly.com/shikher-ai/30min"
}

RESUME = {
    "path": "assets/resume.pdf",
    "file_name": "Shikher_Jain_Resume.pdf",
    "tagline": "Full CV with professional summary, Novas Arc internship, projects, and certifications.",
    "last_updated": date.today().strftime("%b %Y")
}

GITHUB_CONFIG = {
    "username": "Shikher-jain",
    "topic": "portfolio"
}

ML_LAB = {
    "sentiment": {
        "title": "Sentiment Pulse",
        "description": "Rapid sentiment pulse powered by curated lexicons for qualitative scans.",
        "placeholder": "Paste any product feedback, standup summary, or customer snippet..."
    },
    "resume": {
        "title": "Resume Skill Mapper",
        "description": "Keyword-driven scoring that highlights ML, NLP, and MLOps coverage instantly.",
        "placeholder": "Drop a short resume paragraph to score coverage of ML stacks...",
        "keywords": [
            "pytorch",
            "transformer",
            "mlops",
            "langchain",
            "huggingface",
            "fastapi",
            "vector",
            "streamlit",
            "monitoring"
        ]
    }
}
