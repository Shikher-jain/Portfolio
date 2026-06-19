from datetime import date

PROFILE = {
    "name": "Shikher Jain",
    "role": "Data Scientist & AI/ML Engineer",
    "tagline": "AI/ML & Data Science Engineer specializing in backend systems and building scalable, production-ready intelligent solutions from data to deployment.",
    "location": "Agra, Uttar Pradesh, India",
    "experience": "B.Tech CSE | 2026",
    "email": "shikherjain786@gmail.com",
    # "availability": "Open to data science internships, AI/ML fellowships, and freelance builds",
    "avatar": "assets/profile.png",
    # "logo": "assets/logo.png",
    "logo": "assets/logo-SJ.png",
    "hero_stats": [
        {"label": "Projects Shipped", "value": "15+"},
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
        "AI/ML Engineer and Data Scientist with hands-on experience in Python and PyTorch, building end-to-end ML "
        "pipelines spanning data preprocessing, feature engineering, model training, evaluation, and FastAPI-based API "
        "deployment. Skilled in NLP, Langchain, computer vision, RAG-based semantic search, and interactive dashboards. Experienced "
        "in SQL-driven data analysis, backend system development, workflow automation, and scalable containerized "
        "deployment using Docker. Passionate about data-driven problem solving at scale."
    ),
    "highlights": [
        "Build end-to-end AI workflows that move from exploratory notebooks into production-ready APIs and dashboards.",
        "Comfortable with transformer-based NLP, embeddings, and MediaPipe/OpenCV pipelines for real-time insights.",
        "Experienced with data preprocessing, EDA, and feature engineering that keep downstream models stable and accurate.",
        "Skilled in debugging data pipelines, implementing structured validation, and resolving inconsistencies across large datasets.",
        "Experienced in building REST-based systems and improving operational reliability through systematic troubleshooting."
    ],
    "focus": [
        "Data Preprocessing & Feature Engineering",
        "NLP & Transformer Pipelines",
        "RAG-Based System, LanChain",
        "Computer Vision & Real-time Analytics",
        "RESTful ML APIs on Cloud"
    ]
}

EXPERIENCE = [
    {
        "role": "Data Science Intern",
        "company": "XYlofy AI",
        "location": "Bengaluru, Karnataka, India",
        "date": "Jun 2026 - Present · 1 mo",
        "highlights": [
            "Contributed to the development of AI-powered solutions for data analysis and machine learning applications.",
            "Assisted in preprocessing large datasets and implementing feature engineering techniques.",
            "Collaborated with senior engineers to build and deploy scalable ML models."
        ],
        "stack": ["Python", "Machine Learning", "Pandas", "NumPy"]
    }, 
    {
        "role": "Data Science Intern",
        "company": "AISECT LEARN",
        "location": "Bhopal, Madhya Pradesh, India",
        "date": "Apr 2026 - May 2026 · 2 mos",
        "highlights": [
            "Completed applied ML and NLP capstone project covering end-to-end model development workflows.",
            "Implemented data preprocessing, feature engineering, and model evaluation pipelines for NLP tasks.",
            "Applied classification and regression techniques with cross-validation and performance metrics (F1, Precision, Recall).",
            "Worked with HuggingFace Transformers for text classification and NLP preprocessing."
        ],
        "stack": ["Python", "NLP", "HuggingFace", "Scikit-learn", "Pandas"]
    },
    {
        "role": "Data Science Intern",
        "company": "Dynamix Networks",
        "location": "Haryana, India",
        "date": "Jan 2026 - Apr 2026 · 4 mos",
        "highlights": [
            "Built end-to-end fake news detection system using ML classification on large-scale news datasets.",
            "Collected and preprocessed news data from X (Twitter) API and Wikipedia with automated ETL pipelines.",
            "Developed classification model (text features + TF-IDF vectorization) for fake vs genuine news detection.",
            "Designed time-series database schema for efficient storage and retrieval of news articles at scale.",
            "Deployed interactive Streamlit interface for real-time model inference and result visualization."
        ],
        "stack": ["Python", "Machine Learning", "FastAPI", "Streamlit", "PostgreSQL", "Web Scraping"]
    },
    {
        "role": "Data Science Intern",
        "company": "Cognifyz Technologies",
        "location": "Nagpur, India",
        "date": "Nov 2025 – Dec 2025",
        "highlights": [
            "Executed end-to-end data preprocessing and EDA, including missing value handling, feature cleaning, and statistical analysis to extract key insights.",
            "Performed geospatial and business analysis to identify trends across cities, cuisines, pricing, and service features (table booking, delivery).",
            "Applied feature engineering techniques to create meaningful variables improving downstream model performance.",
            "Built and evaluated regression models (Linear, Decision Tree, Random Forest) to predict restaurant ratings, comparing performance using standard metrics.",
            "Developed data visualizations and insight reports to communicate patterns in customer preferences and business drivers effectively."
        ],
        "stack": ["Python", "Matplotlib", "Seaborn", "PyTorch", "Scikit-Learn", "Git", "Pandas", "NumPy", "SQL"]
    },
    {
        "role": "Jr. Software Engineer Intern",
        "company": "Novas Arc Consulting Pvt. Ltd.",
        "location": "Remote",
        "date": "Aug 2025 – Nov 2025",
        "highlights": [
            "Designed and maintained a modular Python backend service processing 10k+ structured records with input validation, structured logging, centralized exception handling, and exponential backoff retry logic for fault-tolerant execution.",
            "Engineered automated data ingestion pipelines extracting FAQs from 100+ dynamic web pages using Selenium and REST API integration, reducing manual effort by 50–60% and improving data consistency.",
            "Built NLP-based preprocessing and feature engineering pipelines for 10,000+ text records, integrating LLM APIs to structure unstructured web data for model-ready datasets.",
            "Developed text classification and context analysis models for intent, persona, tone, domain, and age group, enhancing response relevance by 20–30%; fine-tuned GPT-3.5 Turbo and deployed a training-data–driven AI chatbot with iterative testing.",
            "Collaborated in Agile sprints using Git and AWS CodeCommit, diagnosing pipeline issues and streamlining feature deployment cycles."
        ],
        "stack": ["Python", "Selenium", "NLP", "GPT-3.5 Turbo", "REST APIs", "RAG", "Git", "AWS CodeCommit"]
    },
    {
        "role": "Python Developer Intern",
        "company": "CodSoft",
        "location": "New Delhi, India",
        "date": "June 2024 – July 2024",
        "highlights": [
            "Developed 5 Python GUI applications using Tkinter including task manager, calculator, password generator, and contact book — strengthened Python fundamentals and OOP concepts."   
        ],
        "stack": ["Python", "Tkinter", "Pandas", "NumPy", "Git"]
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
            {"name": "SQL", "badges": ["Querying", "Joins", "Aggregation","Window Functions"]},
            {"name": "Java", "badges": ["OOP", "Collections"]},
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
            {"name": "Model Training", "badges": ["Cross Validation", "Hyperparameter Tuning"]},
            {"name": "Data Wrangling", "badges": ["Cleaning", "Transformation"]},
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
            {"name": "Transformer Models", "badges": ["Attention", "Fine-tuning"]},
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
            {"name": "Hugging Face", "badges": ["Transformers", "Pipelines"]},
            {"name": "Embeddings", "badges": ["Word2Vec", "GloVe", "Sentence-BERT"]},
            {"name": "Semantic Search", "badges": ["Vector Similarity", "Retrieval"]},
            {"name": "FAISS", "badges": ["Vector Indexing", "Nearest Neighbor Search"]},
            {"name": "Qdrant", "badges": ["Vector Database", "Payload Filtering"]},
            {"name": "Transformers", "badges": ["BERT", "GPT", "Fine-tuning"]},
            {"name": "LLM Techniques", "badges": ["Prompt Engineering", "LoRA", "RAG"]}
        ]
    },
    # ===============================
    # Langchain & RAG
    # ===============================
    {
        "category": "Langchain & RAG",
        "skills": [
            {"name": "Langchain", "badges": ["Agent Development", "Memory Management"]},
            {"name": "Retrieval-Augmented Generation (RAG)", "badges": ["Document Retrieval", "Contextual Generation"]}
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
            {"name": "Selenium", "badges": ["Web Automation", "Data Collection"]},
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
            {"name": "FastAPI", "badges": ["Async", "REST APIs", "Async Processing"]},
            {"name": "Flask", "badges": ["Inference APIs", "REST APIs"]},
            {"name": "REST API Design", "badges": ["CRUD", "Versioning"]},
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
            {"name": "PostgreSQL", "badges": ["Schema Design", "Query Optimization"]},
            {"name": "SQLite", "badges": ["Embedded Databases"]},
            {"name": "Git & GitHub", "badges": ["Version Control", "CI/CD"]},
            {"name": "Linux", "badges": ["CLI", "Process Management"]},
            {"name": "Docker", "badges": ["Containers", "Image Optimization"]},
            {"name": "Postman", "badges": ["API Testing"]},
            {"name": "Structured Logging", "badges": ["Observability", "Debugging"]},
            {"name": "Kaggle", "badges": ["Competitions", "Notebooks"]},
            {"name": "Google Colab", "badges": ["GPU Training"]}
        ]
    },

    # ===============================
    # Core Computer Science
    # ===============================
    {
        "category": "Core Computer Science",
        "skills": [
            {"name": "Data Structures & Algorithms", "badges": ["Complexity Analysis", "Problem Solving"]},
            {"name": "Operating Systems", "badges": ["Processes", "Memory Management"]},
            {"name": "Object-Oriented Programming", "badges": ["Abstraction", "Inheritance", "Polymorphism"]},
            {"name": "DBMS", "badges": ["Normalization", "Transactions"]}
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
            {"name": "Statistics", "badges": ["Hypothesis Testing", "Confidence Intervals", "Statistical Inference"]},
            {"name": "Optimization", "badges": ["Gradient Descent", "Loss Functions"]}
        ]
    }
]

EDUCATION = [
    {
        "institution": "Faculty of Engineering and Technology, Agra College (AKTU)",
        "degree": "B.Tech in Computer Science and Engineering",
        "period": "2022–2026",
        "details": "CGPA: 7.9 / 10"
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
    # "availability": PROFILE["availability"],
    "socials": PROFILE["socials"],
    "calendly": "https://calendly.com/shikher-ai/30min"
}

RESUME = {
    "path": "assets/resume.pdf",
    "file_name": "Shikher_Jain_Resume.pdf",
    "tagline": "Full CV with professional summary, Novas Arc internship, projects, and certifications.",
    "last_updated": date.today().strftime("%b %Y")
}

RESUMES = [
    {
        "path": "assets/ShikherJain_Resume_AI.pdf",
        "file_name": "Shikher_Jain_Resume_AI.pdf",
        "tagline": "AI/ML focused profile for machine learning and applied AI roles.",
        "last_updated": date.today().strftime("%b %Y"),
    },
    {
        "path": "assets/ShikherJain_Resume_ML.pdf",
        "file_name": "Shikher_Jain_Resume_ML.pdf",
        "tagline": "Machine Learning profile highlighting algorithm development and model deployment.",
        "last_updated": date.today().strftime("%b %Y"),
    },
    {
        "path": "assets/ShikherJain_Resume_Backend.pdf",
        "file_name": "Shikher_Jain_Resume_Backend.pdf",
        "tagline": "Backend Development profile highlighting API design and production-ready development.",
        "last_updated": date.today().strftime("%b %Y"),
    },
    {
        "path": "assets/ShikherJain_Resume_DataScientist.pdf",
        "file_name": "ShikherJain_Resume_DataScientist.pdf",
        "tagline": "Data Science focused version highlighting EDA, modeling, and analytics projects.",
        "last_updated": date.today().strftime("%b %Y"),
    },
    {
        "path": "assets/ShikherJain_Resume_DataAnalyst.pdf",
        "file_name": "Shikher_Jain_Resume_DataAnalyst.pdf",
        "tagline": "Data Analysis profile highlighting data visualization, reporting, and business intelligence projects.",
        "last_updated": date.today().strftime("%b %Y"),
    },
]

Research_Paper = {
    "title": "Sahayak: A Unified Multi-Linguistic Assistant for Bharat SaaS Onboarding",
    "authors": ["Shikher Jain"],
    "publication": "https://zenodo.org/",
    "year": 2026,
    "abstract": "This paper presents a new method for image recognition using deep learning techniques.",
    "path": "assets/Sahayak_Research_Paper_SJ.pdf",
    "file_name": "Sahayak_Research_Paper_SJ.pdf",
    "url": "https://zenodo.org/record/1234567",
    "tagline": "Research paper on the development of a unified multi-linguistic assistant for Bharat SaaS onboarding.",
    "last_updated": date.today().strftime("%b %Y"),
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
    "resume": {
        "title": "Resume Skill Mapper",
        "description": "Role-based weighted scoring with skill-gap detection and optional JD similarity.",
        "placeholder": "Paste resume summary/experience/skills here...",
        "jd_placeholder": "Paste target job description (optional) to compute alignment...",
        "roles": {
            "AI/ML Engineer": {
                "weights": {
                    "python": 10,
                    "pytorch": 10,
                    "rag": 10,
                    "transformers": 9,
                    "nlp": 9,
                    "fastapi": 8,
                    "docker": 8,
                    "langchain": 8,
                    "faiss": 7,
                    "mlops": 8,
                    "monitoring": 6,
                    "sql": 6,
                },
                "aliases": {
                    "transformers": ["transformer", "huggingface", "bert"],
                    "rag": ["retrieval augmented generation", "retrieval-augmented generation"],
                    "monitoring": ["observability", "model monitoring"],
                },
                "must_have": ["python", "pytorch", "rag", "fastapi"],
            },
            "Data Scientist": {
                "weights": {
                    "python": 10,
                    "sql": 10,
                    "pandas": 8,
                    "numpy": 8,
                    "scikit-learn": 9,
                    "feature engineering": 8,
                    "statistics": 8,
                    "eda": 7,
                    "visualization": 7,
                    "machine learning": 9,
                    "streamlit": 5,
                },
                "aliases": {
                    "scikit-learn": ["sklearn"],
                    "visualization": ["plotly", "matplotlib", "seaborn", "dashboard"],
                    "machine learning": ["ml", "predictive modeling"],
                },
                "must_have": ["python", "sql", "scikit-learn"],
            },
            "SWE": {
                "weights": {
                    "python": 9,
                    "java": 9,
                    "sql": 8,
                    "data structures": 10,
                    "algorithms": 10,
                    "oop": 8,
                    "fastapi": 7,
                    "rest api": 8,
                    "git": 7,
                    "docker": 7,
                    "debugging": 8,
                    "testing": 8,
                },
                "aliases": {
                    "rest api": ["rest", "api development", "api design"],
                    "data structures": ["dsa", "data structure"],
                    "algorithms": ["algorithm"],
                    "testing": ["unit test", "pytest", "unittest"],
                },
                "must_have": ["data structures", "algorithms", "oop", "git"],
            },
            "SQL Developer": {
                "weights": {
                    "sql": 10,
                    "joins": 9,
                    "window functions": 9,
                    "stored procedures": 9,
                    "query optimization": 9,
                    "indexing": 8,
                    "normalization": 8,
                    "etl": 8,
                    "data modeling": 8,
                    "postgresql": 7,
                    "mysql": 7,
                    "debugging": 6,
                },
                "aliases": {
                    "stored procedures": ["stored procedure", "procedure"],
                    "query optimization": ["performance tuning", "query tuning"],
                    "indexing": ["indexes", "index"],
                    "etl": ["data pipeline", "data ingestion"],
                },
                "must_have": ["sql", "joins", "window functions", "query optimization"],
            },
        },
    }
}
