import streamlit as st

def render_experience():
    st.markdown("""
    <div class="exp-section" id="experience">
        <div class="exp-title">💼 Work Experience</div>
        <div class="exp-card">
            <div class="exp-role">API Developer</div>
            <div class="exp-org">Satyukt Analytics Private Limited</div>
            <div class="exp-details">2025/06 - 2025/11 | Bengaluru, India</div>
            <div class="exp-desc">
                Satyukt is a pioneering agri-tech company that leverages satellite data, advanced technology, and machine learning to provide innovative SaaS solutions.
            </div>
        </div>
        <div class="exp-card">
            <div class="exp-role">Backend Developer</div>
            <div class="exp-org">Tia</div>
            <div class="exp-details">2024/03 – 2024/06 | Coimbatore, India</div>
            <div class="exp-desc">
                A forward-thinking company specializing in backend development using Node.js and AWS technologies, where I contributed to optimizing the backend structure for enhanced performance.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)