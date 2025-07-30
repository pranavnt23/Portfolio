import streamlit as st

def render_experience():
    st.markdown("""
    <style>
    .exp-section {
        max-width: 700px;
        margin: 0 auto 36px auto;
        padding: 1.5rem 1.2rem 1.2rem 1.2rem;
        border-radius: 18px;
        background: linear-gradient(120deg, #43cea2 0%, #185a9d 100%);
        box-shadow: 0 4px 24px #43cea255, 0 1.5px 8px #fff4;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .exp-title {
        font-size: 2em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 1.2rem;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #185a9d55;
        background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
        padding: 0.3rem 1.2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px #43cea255;
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }
    .exp-card {
        background: #fff;
        border-radius: 14px;
        box-shadow: 0 2px 12px #43cea233;
        padding: 1.2rem 1.2rem 1rem 1.2rem;
        margin-bottom: 1.2rem;
        width: 100%;
        max-width: 600px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        transition: box-shadow 0.22s;
        position: relative;
        overflow: hidden;
    }
    .exp-card:last-child {
        margin-bottom: 0;
    }
    .exp-role {
        font-size: 1.18em;
        font-weight: 700;
        color: #185a9d;
        margin-bottom: 0.2em;
        letter-spacing: 0.5px;
    }
    .exp-org {
        font-size: 1.05em;
        font-weight: 600;
        color: #222;
        margin-bottom: 0.3em;
    }
    .exp-details {
        font-size: 1em;
        color: #444;
        margin-bottom: 0.2em;
    }
    .exp-desc {
        font-size: 1em;
        font-weight: 600;
        color: #43cea2;
        margin-top: 0.2em;
    }
    @media (max-width: 800px) {
        .exp-section { padding: 1rem 0.3rem; }
        .exp-title { font-size: 1.2em; padding: 0.2rem 0.7rem; }
        .exp-card { padding: 0.8rem 0.5rem 0.7rem 0.5rem; }
    }
    </style>
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