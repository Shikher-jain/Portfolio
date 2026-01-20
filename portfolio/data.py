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
