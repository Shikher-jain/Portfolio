from datetime import date

PROFILE = {
    "name": "Shikher Jain",
    "role": "Data Scientist & AI/ML Engineer",
    "tagline": "Entry-level ML engineer crafting RAG, vision, and NLP systems end to end.",
    "location": "Agra, Uttar Pradesh, India",
    "experience": "B.Tech CSE | 2026",
    "email": "shikherjain786@gmail.com",
    "availability": "Open to data science internships, AI/ML fellowships, and freelance builds",
    "avatar": "assets/profile.png",
    "logo": "assets/logo.png",
    "hero_stats": [
        {"label": "Projects Shipped", "value": "8+"},
        {"label": "Models Deployed", "value": "12"},
        {"label": "TCS CodeVita Rank", "value": "1040"}
    ],
    "socials": {
        "LinkedIn": "https://www.linkedin.com/in/shikher-jain-0bb8a8259/",
        "YouTube": "https://www.youtube.com/@shikherjain0906",
        "Kaggle": "https://www.kaggle.com/shikherjain",
        "LeetCode": "https://leetcode.com/u/shikherJain09/",
        "HackerRank": "https://www.hackerrank.com/profile/shikherjain786",
        "GeeksforGeeks": "https://www.geeksforgeeks.org/user/shikherj/",
        "GitHub": "https://github.com/Shikher-jain",
        "Hugging Face": "https://huggingface.co/Shikher09",
        "Google Cloud Skill Boost": "https://www.cloudskillsboost.google/public_profiles/ec9eb266-a3ec-472d-a1ec-1015892b92f2",
        "Credly": "https://www.credly.com/users/shikher-jain",
        "Instagram": "https://www.instagram.com/shikher.09",
        "X / Twitter": "https://x.com/shikherjain786",
        "Stack Overflow": "https://stackoverflow.com/users/32228704/shikher-jain",
        "Streamlit Cloud ": "https://share.streamlit.io/user/shikher-jain",
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
            {"name": "Python", "level": 95, "badges": ["OOP", "Data Structures", "Automation"]},
            {"name": "Java", "level": 80, "badges": ["OOP", "Collections"]},
            {"name": "C", "level": 75, "badges": ["Pointers", "Memory Management"]}
        ]
    },

    {
        "category": "Machine Learning & Data Science",
        "skills": [
            {"name": "NumPy", "level": 90, "badges": ["Arrays", "Vectorization"]},
            {"name": "Pandas", "level": 92, "badges": ["DataFrames", "Data Cleaning"]},
            {"name": "Scikit-learn", "level": 88, "badges": ["Modeling", "Evaluation"]},
            {"name": "Data Preprocessing", "level": 90, "badges": ["Missing Values", "Encoding"]},
            {"name": "EDA", "level": 88, "badges": ["Visualization", "Insights"]},
            {"name": "Feature Engineering", "level": 85, "badges": ["Scaling", "Selection"]}
        ]
    },

    {
        "category": "Deep Learning & Artificial Intelligence",
        "skills": [
            {"name": "PyTorch", "level": 92, "badges": ["Autograd", "Training Loops"]},
            {"name": "Neural Networks", "level": 90, "badges": ["MLP", "CNN", "RNN"]},
            {"name": "Model Optimization", "level": 85, "badges": ["Schedulers", "Regularization"]}
        ]
    },

    {
        "category": "Natural Language Processing (NLP)",
        "skills": [
            {"name": "Text Preprocessing", "level": 90, "badges": ["Cleaning", "Normalization"]},
            {"name": "Tokenization", "level": 88, "badges": ["BPE", "WordPiece"]},
            {"name": "Embeddings", "level": 85, "badges": ["Word2Vec", "Sentence-BERT"]},
            {"name": "Transformer Models", "level": 84, "badges": ["BERT", "LoRA", "Fine-tuning"]}
        ]
    },

    {
        "category": "Computer Vision",
        "skills": [
            {"name": "OpenCV", "level": 90, "badges": ["Image Processing", "Real-time"]},
            {"name": "MediaPipe", "level": 85, "badges": ["Pose", "Hands", "Face Mesh"]},
            {"name": "Face Recognition", "level": 82, "badges": ["LBPH", "Embeddings"]},
            {"name": "Pose Estimation", "level": 80, "badges": ["Tracking", "Keypoints"]},
            {"name": "Real-Time Vision Pipelines", "level": 78, "badges": ["Camera", "FPS Optimization"]}
        ]
    },

    {
        "category": "Data Visualization & Analysis",
        "skills": [
            {"name": "Matplotlib", "level": 85, "badges": ["Plots", "Explainers"]},
            {"name": "Seaborn", "level": 82, "badges": ["Statistical Charts"]},
            {"name": "Plotly", "level": 80, "badges": ["Interactive", "Dashboards"]},
            {"name": "Tableau", "level": 75, "badges": ["Storytelling", "KPIs"]},
            {"name": "Power BI", "level": 75, "badges": ["Reports", "DAX"]}
        ]
    },

    {
        "category": "Web & API Development",
        "skills": [
            {"name": "FastAPI", "level": 88, "badges": ["Async", "REST APIs"]},
            {"name": "Flask", "level": 82, "badges": ["Microservices"]},
            {"name": "Django", "level": 75, "badges": ["MVC", "Auth"]},
            {"name": "RESTful APIs", "level": 90, "badges": ["CRUD", "JWT"]},
            {"name": "Streamlit", "level": 92, "badges": ["Dashboards", "ML Apps"]}
        ]
    },

    {
        "category": "Databases & Developer Tools",
        "skills": [
            {"name": "MySQL", "level": 82, "badges": ["Joins", "Indexes"]},
            {"name": "SQLite", "level": 80, "badges": ["Embedded DB"]},
            {"name": "Git & GitHub", "level": 88, "badges": ["Version Control", "CI/CD"]},
            {"name": "Docker", "level": 82, "badges": ["Containers", "Deployment"]},
            {"name": "Jupyter Notebook", "level": 90, "badges": ["EDA", "Experiments"]},
            {"name": "Google Colab", "level": 88, "badges": ["GPU Training"]},
            {"name": "Kaggle", "level": 85, "badges": ["Competitions", "Notebooks"]},
            {"name": "Postman", "level": 80, "badges": ["API Testing"]}
        ]
    },

    {
        "category": "Applied Mathematics & Logical Foundations",
        "skills": [
            {"name": "Linear Algebra", "level": 80, "badges": ["Vectors", "Matrices"]},
            {"name": "Probability", "level": 82, "badges": ["Distributions", "Bayes"]},
            {"name": "Statistics", "level": 85, "badges": ["Hypothesis Testing"]},
            {"name": "Rule-based Logic", "level": 78, "badges": ["Conditions", "Inference"]},
            {"name": "Mathematical Modeling", "level": 76, "badges": ["Formulation", "Optimization"]}
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

FEATURED_TOPIC_TAGS = {"portfolio", "feature"}

PROJECT_SHORTLIST = [
    "ai_for_good",
    "ai_for_good_hackathon",
    "attendease",
    "chatbot",
    "gdp-dashboard",
    "genai",
    "india_census_app",
    "next-word-prediction-tp35",
    "sahayak_ai",
    "streamlit-ipl-app",
]

FEATURED_PROJECTS = [
    {
        "name": "DocuSense RAG Copilot",
        "description": (
            "Retrieval-augmented QA copilot that indexes policy PDFs, vectorizes snippets with MiniLM, and "
            "streams grounded answers via LangChain tools."
        ),
        "languages": ["Python", "LangChain", "FAISS"],
        "topics": ["RAG", "LangChain", "OpenAI"],
        "category": "NLP",
        "html_url": "https://github.com/Shikher-jain/DocuSense-RAG-Copilot",
        "homepage": "https://docusense.streamlit.app",
        "stars": 18,
        "forks": 4,
        "updated": "05 Jan 2026",
    },
    {
        "name": "VisionGuard PPE Monitor",
        "description": (
            "Real-time PPE compliance tracker that fuses Mediapipe pose landmarks with YOLOv8 detections to flag "
            "missing helmets and vests on shop floors."
        ),
        "languages": ["Python", "OpenCV", "YOLOv8"],
        "topics": ["computer-vision", "safety", "edge-ai"],
        "category": "Computer Vision",
        "html_url": "https://github.com/Shikher-jain/VisionGuard-PPE",
        "homepage": "https://visionguard.streamlit.app",
        "stars": 14,
        "forks": 2,
        "updated": "22 Dec 2025",
    },
    {
        "name": "CampusPulse Placement Tracker",
        "description": (
            "An end-to-end analytics stack that ingests placement drive CSVs, cleans data with Pandas, and serves "
            "Streamlit dashboards plus FastAPI webhooks for alerts."
        ),
        "languages": ["Python", "Streamlit", "FastAPI"],
        "topics": ["data-engineering", "analytics"],
        "category": "Data Engineering",
        "html_url": "https://github.com/Shikher-jain/CampusPulse-Tracker",
        "homepage": "https://campuspulse.streamlit.app",
        "stars": 10,
        "forks": 1,
        "updated": "11 Nov 2025",
    },
]

SHORTLIST_FALLBACKS = {
    "ai_for_good": {
        "name": "ai_for_good",
        "description": "UN SDG insights dashboard that blends Kaggle datasets with Streamlit storytelling for policy teams.",
        "languages": ["Python", "Streamlit", "Plotly"],
        "topics": ["sdg", "dashboard", "hackathon"],
        "category": "Analytics",
        "html_url": "https://github.com/Shikher-jain/ai_for_good",
        "homepage": "https://ai-for-good.streamlit.app",
        "stars": 5,
        "forks": 1,
        "updated": "10 Oct 2025",
    },
    "ai_for_good_hackathon": {
        "name": "ai_for_good_hackathon",
        "description": "Hackathon-winning ML pipeline that scores NGO initiatives with Explainable AI notebooks and APIs.",
        "languages": ["Python", "FastAPI"],
        "topics": ["hackathon", "explainable-ai"],
        "category": "Hackathon",
        "html_url": "https://github.com/Shikher-jain/ai_for_good_hackathon",
        "homepage": "https://ai-for-good-hackathon.streamlit.app",
        "stars": 4,
        "forks": 0,
        "updated": "02 Oct 2025",
    },
    "genai": {
        "name": "genai",
        "description": "Micro GenAI lab showcasing prompt chaining, semantic search, and multi-agent workflows with LangChain.",
        "languages": ["Python", "LangChain"],
        "topics": ["genai", "prompt-engineering"],
        "category": "GenAI",
        "html_url": "https://github.com/Shikher-jain/genai",
        "homepage": "https://genai-playground.streamlit.app",
        "stars": 7,
        "forks": 1,
        "updated": "18 Dec 2025",
    },
    "india_census_app": {
        "name": "india_census_app",
        "description": "Interactive census explorer with district drilldowns, demographic trends, and Mapbox visualizations.",
        "languages": ["Python", "Streamlit", "Pandas"],
        "topics": ["census", "viz"],
        "category": "Data App",
        "html_url": "https://github.com/Shikher-jain/india_census_app",
        "homepage": "https://india-census.streamlit.app",
        "stars": 6,
        "forks": 1,
        "updated": "14 Sep 2025",
    },
    "next-word-prediction-tp35": {
        "name": "next-word-prediction-tp35",
        "description": "LSTM + GPT hybrid next-word predictor trained on interview transcripts with live typing assistant UI.",
        "languages": ["Python", "TensorFlow"],
        "topics": ["nlp", "lstm", "text-generation"],
        "category": "NLP",
        "html_url": "https://github.com/Shikher-jain/next-word-prediction-tp35",
        "homepage": "https://next-word.streamlit.app",
        "stars": 8,
        "forks": 2,
        "updated": "05 Aug 2025",
    },
    "sahayak_ai": {
        "name": "sahayak_ai",
        "description": "Hindi-first AI assistant combining speech, translation, and retrieval for Bharat SaaS onboarding.",
        "languages": ["Python", "SpeechRecognition"],
        "topics": ["voice", "rag", "india"],
        "category": "Conversational AI",
        "html_url": "https://github.com/Shikher-jain/sahayak_ai",
        "homepage": "https://sahayak-ai.streamlit.app",
        "stars": 9,
        "forks": 1,
        "updated": "28 Nov 2025",
    },
    "streamlit-ipl-app": {
        "name": "streamlit-ipl-app",
        "description": "IPL analytics workbench with match prediction, player radar charts, and shot-density maps.",
        "languages": ["Python", "Streamlit", "Plotly"],
        "topics": ["sports-analytics", "ipl"],
        "category": "Sports",
        "html_url": "https://github.com/Shikher-jain/streamlit-ipl-app",
        "homepage": "https://ipl-analytics.streamlit.app",
        "stars": 11,
        "forks": 3,
        "updated": "16 Apr 2025",
    },
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
