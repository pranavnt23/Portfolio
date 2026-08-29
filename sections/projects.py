import streamlit as st

def render_projects():
    st.markdown("""
    <div class="projects-title" id="projects">🚀 Projects</div>
    """, unsafe_allow_html=True)

    with st.expander("🤖 AI Smart Study Planner"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="font-size:1.1em; font-weight:600; margin-bottom:6px; color:var(--accent-color);">Cloud-Based AI-Powered Personalized Learning Platform</p>
            <p style="margin-bottom:12px; font-size:1.02em;">Engineered an AI-powered Smart Study Planner that processes learning documents using OCR, text cleaning, chunking, embeddings, and RAG for contextual question answering and personalized study assistance, built with React, FastAPI, PostgreSQL, ChromaDB, Sentence Transformers, and Ollama.</p>
            <a href="https://github.com/pranavnt23/AI-Powered-Smart-Study-Planner" target="_blank" style="display:inline-flex; align-items:center; text-decoration:none; color:#38bdf8; font-weight:600; gap:8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="22" style="filter:invert(1) brightness(2);"/> 
                <span>GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🎫 Melinia'26 - Event Registration and Participation Site"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="font-size:1.1em; font-weight:600; margin-bottom:6px; color:var(--accent-color);">Department of Computing Event Platform</p>
            <p style="margin-bottom:12px; font-size:1.02em;">Architected and scaled Melinia, a full-stack event platform using a Bun/Hono/React monorepo to seamlessly support 2,000+ users. PostgreSQL schema for transactional registrations while optimizing performance via a Redis/BullMQ processing layer.</p>
            <a href="https://github.com/Melinia-CIT/melinia-26" target="_blank" style="display:inline-flex; align-items:center; text-decoration:none; color:#38bdf8; font-weight:600; gap:8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="22" style="filter:invert(1) brightness(2);"/> 
                <span>GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📅 Attendance Portal"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="font-size:1.1em; font-weight:600; margin-bottom:6px; color:var(--accent-color);">Cloud-Based Full-Stack Attendance Management System</p>
            <p style="margin-bottom:12px; font-size:1.02em;">Designed and deployed a responsive Attendance Portal with JWT authentication, subject-wise attendance tracking, and real-time reporting using React, FastAPI, Render, Vercel, and Neon PostgreSQL.</p>
            <a href="https://github.com/pranavnt23/Attendance-Tracker" target="_blank" style="display:inline-flex; align-items:center; text-decoration:none; color:#38bdf8; font-weight:600; gap:8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="22" style="filter:invert(1) brightness(2);"/> 
                <span>GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("💸 FundVerse - ChitFund Platform"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="margin-bottom:12px; font-size:1.02em;">Developing a full stack Chitfund platform to efficiently automate operations, ensuring secure and streamlined processes for all stakeholders.</p>
            <a href="https://github.com/pranavnt23/ChitFund_Platform" target="_blank" style="display:inline-flex; align-items:center; text-decoration:none; color:#38bdf8; font-weight:600; gap:8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="22" style="filter:invert(1) brightness(2);"/> 
                <span>GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("✈️ Flight Delay Prediction Model"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="margin-bottom:0; font-size:1.02em;">Built a machine learning model using Linear Regression and Random Forest Classifier to predict flight delays based on past data and multiple scenarios.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🪑 Seating Allocation System"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="margin-bottom:12px; font-size:1.02em;">Automated University Seating Allocation System in Java, streamlining seat assignments for exams and events, enhancing efficiency, accuracy, and fairness.</p>
            <a href="https://github.com/pranavnt23/Seating_Allocation" target="_blank" style="display:inline-flex; align-items:center; text-decoration:none; color:#38bdf8; font-weight:600; gap:8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="22" style="filter:invert(1) brightness(2);"/> 
                <span>GitHub</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📊 Flight Delay Analysis Dashboard"):
        st.markdown("""
        <div style="text-align:center; padding: 6px 0;">
            <p style="margin-bottom:12px; font-size:1.02em;">PowerBI dashboard visualizing flight delays based on various parameters, helping to analyze and understand delay patterns using historical data.</p>
            <a href="https://drive.google.com/drive/folders/1V9X4I4ibsFfS0XzFrSbSYct267jzFg0q" target="_blank" style="display:inline-flex; align-items:center; text-decoration:none; color:#38bdf8; font-weight:600; gap:8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" alt="Google Drive" width="22"/> 
                <span>Google Drive</span>
            </a>
        </div>
        """, unsafe_allow_html=True)