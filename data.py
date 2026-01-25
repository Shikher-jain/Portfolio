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
        {"label": "Projects Shipped", "value": "10+"},
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

    # ===============================
    # Programming Foundations
    # ===============================
    {
        "category": "Programming Languages",
        "skills": [
            {"name": "Python", "badges": ["OOP", "Data Structures", "Automation", "Async"]},
            {"name": "Java", "badges": ["OOP", "Collections", "JVM Basics"]},
            {"name": "C", "badges": ["Pointers", "Memory Management"]}
        ]
    },

    # ===============================
    # Machine Learning & Data Science
    # ===============================
    {
        "category": "Machine Learning & Data Science",
        "skills": [
            {"name": "NumPy", "badges": ["Arrays", "Vectorization"]},
            {"name": "Pandas", "badges": ["DataFrames", "Feature Pipelines"]},
            {"name": "Scikit-learn", "badges": ["Regression", "Classification", "Pipelines"]},
            {"name": "EDA", "badges": ["Insights", "Outlier Detection"]},
            {"name": "Feature Engineering", "badges": ["Scaling", "Encoding", "Selection"]},
            {"name": "Model Evaluation", "badges": ["Accuracy", "F1", "ROC-AUC"]}
        ]
    },

    # ===============================
    # Deep Learning & AI
    # ===============================
    {
        "category": "Deep Learning & Artificial Intelligence",
        "skills": [
            {"name": "PyTorch", "badges": ["Autograd", "Custom Datasets", "Training Loops"]},
            {"name": "Neural Networks", "badges": ["MLP", "CNN", "RNN", "LSTM"]},
            {"name": "Model Optimization", "badges": ["Schedulers", "Dropout", "Weight Decay"]},
            {"name": "Transfer Learning", "badges": ["Pretrained Models", "Fine-tuning"]},
            {"name": "Model Deployment", "badges": ["Inference", "Batch vs Real-time"]}
        ]
    },

    # ===============================
    # NLP & LLMs
    # ===============================
    {
        "category": "Natural Language Processing (NLP)",
        "skills": [
            {"name": "Text Preprocessing", "badges": ["Cleaning", "Normalization"]},
            {"name": "Tokenization", "badges": ["BPE", "WordPiece"]},
            {"name": "Embeddings", "badges": ["Word2Vec", "GloVe", "Sentence-BERT"]},
            {"name": "Transformers", "badges": ["BERT", "GPT", "Fine-tuning"]},
            {"name": "LLM Techniques", "badges": ["Prompt Engineering", "LoRA", "RAG"]}
        ]
    },

    # ===============================
    # Computer Vision
    # ===============================
    {
        "category": "Computer Vision",
        "skills": [
            {"name": "OpenCV", "badges": ["Image Processing", "Video Streams"]},
            {"name": "MediaPipe", "badges": ["Hands", "Pose", "Face Mesh"]},
            {"name": "Face Recognition", "badges": ["Embeddings", "Similarity Search"]},
            {"name": "Pose Estimation", "badges": ["Keypoints", "Tracking"]},
            {"name": "Real-Time Vision Systems", "badges": ["FPS Optimization", "Threading"]}
        ]
    },

    # ===============================
    # Data Visualization
    # ===============================
    {
        "category": "Data Visualization & Analytics",
        "skills": [
            {"name": "Matplotlib", "badges": ["Custom Plots"]},
            {"name": "Seaborn", "badges": ["Statistical Visualization"]},
            {"name": "Plotly", "badges": ["Interactive Dashboards"]},
            {"name": "Tableau", "badges": ["KPIs", "Storytelling"]},
            {"name": "Power BI", "badges": ["DAX", "Business Reports"]}
        ]
    },

    # ===============================
    # Backend & Deployment
    # ===============================
    {
        "category": "Web, APIs & Deployment",
        "skills": [
            {"name": "FastAPI", "badges": ["Async", "REST APIs"]},
            {"name": "Flask", "badges": ["Inference APIs"]},
            {"name": "Django", "badges": ["Auth", "MVC"]},
            {"name": "Streamlit", "badges": ["ML Dashboards", "Deployment"]},
            {"name": "API Security", "badges": ["JWT", "Rate Limiting"]}
        ]
    },

    # ===============================
    # Databases & Tools
    # ===============================
    {
        "category": "Databases & Developer Tools",
        "skills": [
            {"name": "MySQL", "badges": ["Indexes", "Joins"]},
            {"name": "SQLite", "badges": ["Embedded Databases"]},
            {"name": "Git & GitHub", "badges": ["Version Control", "CI/CD"]},
            {"name": "Docker", "badges": ["Containers", "Image Optimization"]},
            {"name": "Postman", "badges": ["API Testing"]},
            {"name": "Kaggle", "badges": ["Competitions", "Notebooks"]},
            {"name": "Google Colab", "badges": ["GPU Training"]}
        ]
    },

    # ===============================
    # Math for AI
    # ===============================
    {
        "category": "Mathematics for Machine Learning",
        "skills": [
            {"name": "Linear Algebra", "badges": ["Vectors", "Matrices", "Eigenvalues"]},
            {"name": "Probability", "badges": ["Bayesian Thinking", "Distributions"]},
            {"name": "Statistics", "badges": ["Hypothesis Testing", "Confidence Intervals"]},
            {"name": "Optimization", "badges": ["Gradient Descent", "Loss Functions"]}
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
    # ===== Computer Vision =====
    "Hand-Gesture-Controller",
    "hand-volume-control",
    "Virtual-Painter",

    # ===== AI / ML Systems =====
    "AI_FOR_GOOD",
    "Sahayak_All_Version",
    "AI-Trainer",

    # ===== Data Science / Analytics =====
    "Data_Science",
    "Data-Vista",
    "India_Census_App",
    "Streamlit-IPL-App",

    # ===== Mini / Utility Projects =====
    "Cognifyz",
    "Password-Generator",
    "Contact-Book",
    "Bill-Generator",
    "Student_Management",
    "StudentAttendance",

    # ===== GenAI =====
    "GenAI",
    "voice-assistant",

    # ===== Live-demo aliases (needed for homepage linking) =====
    "ai_for_good_hackathon",
    "attendease",
    "gdp-dashboard",
    "next-word-prediction-tp35",
    "sahayak_ai",
]

FEATURED_PROJECTS = [
    {
        "name": "Sahayak_All_Version",
        "description": (
            "Unified Hindi-first assistant combining speech, OCR, and retrieval workflows for Bharat SaaS onboarding."
        ),
        "languages": ["Python", "Streamlit", "LangChain"],
        "topics": ["conversational-ai", "rag", "multimodal"],
        "category": "AI Assistant",
        "html_url": "https://github.com/Shikher-jain/Sahayak_All_Version",
        "homepage": "",
        "stars": 18,
        "forks": 3,
        "updated": "14 Jan 2026",
    },
    {
        "name": "StudentAttendance",
        "description": (
            "Face-recognition attendance tracker with on-device capture, analytics, and CSV export pipelines."
        ),
        "languages": ["Python", "OpenCV", "Streamlit"],
        "topics": ["computer-vision", "automation"],
        "category": "EdTech",
        "html_url": "https://github.com/Shikher-jain/StudentAttendance",
        "homepage": "",
        "stars": 9,
        "forks": 1,
        "updated": "05 Jan 2026",
    },
    {
        "name": "AI-Trainer",
        "description": (
            "Virtual AI fitness coach that fuses pose estimation with rule engines to guide real-time workouts."
        ),
        "languages": ["Python", "MediaPipe"],
        "topics": ["pose-estimation", "computer-vision"],
        "category": "Computer Vision",
        "html_url": "https://github.com/Shikher-jain/AI-Trainer",
        "homepage": "",
        "stars": 11,
        "forks": 2,
        "updated": "28 Dec 2025",
    },
    {
        "name": "Streamlit-IPL-App",
        "description": (
            "Interactive IPL analytics workbench featuring win predictors, radar charts, and player insights."
        ),
        "languages": ["Python", "Streamlit", "Plotly"],
        "topics": ["sports-analytics", "data-viz"],
        "category": "Analytics",
        "html_url": "https://github.com/Shikher-jain/Streamlit-IPL-App",
        "homepage": "https://ipl-analytics.streamlit.app",
        "stars": 13,
        "forks": 3,
        "updated": "16 Apr 2025",
    },
    {
        "name": "India_Census_App",
        "description": (
            "Census intelligence dashboard with district drilldowns, demographic KPIs, and geospatial plots."
        ),
        "languages": ["Python", "Streamlit", "Pandas"],
        "topics": ["census", "dashboard"],
        "category": "Data App",
        "html_url": "https://github.com/Shikher-jain/India_Census_App",
        "homepage": "https://india-census.streamlit.app",
        "stars": 7,
        "forks": 1,
        "updated": "14 Sep 2025",
    },
    {
        "name": "Sahayak_AI",
        "description": (
            "Voice-enabled assistant delivering bilingual answers with retrieval grounding and TTS playback."
        ),
        "languages": ["Python", "SpeechRecognition"],
        "topics": ["voice", "rag", "assistant"],
        "category": "Conversational AI",
        "html_url": "https://github.com/Shikher-jain/Sahayak_AI",
        "homepage": "https://sahayak-ai.streamlit.app",
        "stars": 12,
        "forks": 2,
        "updated": "28 Nov 2025",
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
