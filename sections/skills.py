import streamlit as st

def render_skills():
    st.markdown("""
    <style>
    .tech-category {
        margin-bottom: 2.5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .category-title {
        font-size: 1.5rem;
        margin-bottom: 1.2rem;
        font-weight: bold;
        color: #ffffff;
        background: linear-gradient(90deg, #007cf0, #00dfd8);
        padding: 0.3rem 1.2rem;
        border-radius: 12px;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
        box-shadow: 0 2px 8px #00e6ff33;
    }
    .tech-stack-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        margin-top: 0.5rem;
        justify-content: center;
    }
    .tech-box {
        background: #1e1e2f;
        padding: 1.2rem 1rem 1rem 1rem;
        border-radius: 14px;
        text-align: center;
        width: 120px;
        height: 120px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 15px #0ff2;
        animation: float 4s ease-in-out infinite;
        transition: transform 0.3s, box-shadow 0.3s;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.5rem;
    }
    .tech-box:hover {
        transform: scale(1.09) rotate(2deg);
        box-shadow: 0 0 25px #0ff, 0 0 30px #00dfd8;
        z-index: 2;
    }
    .tech-icon {
        font-size: 2.1rem;
        margin-bottom: 0.7rem;
    }
    .tech-name {
        font-weight: 600;
        font-size: 1.05rem;
        color: #ffffff;
        letter-spacing: 0.5px;
    }
    .tech-python { background: radial-gradient(circle, #306998, #4B8BBE); }
    .tech-js { background: radial-gradient(circle, #f0db4f, #323330); color: #000; }
    .tech-dart { background: radial-gradient(circle, #00B4AB, #0175C2); }
    .tech-flutter { background: linear-gradient(135deg, #02569B, #13B9FD); }
    .tech-fastapi { background: linear-gradient(135deg, #059669, #10B981); }
    .tech-react { background: radial-gradient(circle, #61DBFB, #20232a); }
    .tech-docker { background: linear-gradient(135deg, #2496ED, #1D63ED); }
    .tech-git { background: linear-gradient(135deg, #F05032, #8F3F1F); }
    .tech-firebase { background: radial-gradient(circle, #FFA000, #F57C00); }
    .tech-aws { background: linear-gradient(135deg, #FF9900, #232F3E); }
    .tech-dynamodb { background: linear-gradient(135deg, #4053D6, #232F3E); }
    .tech-postgresql { background: linear-gradient(135deg, #336791, #2F5DAB); }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }
    @keyframes glow {
        0% { box-shadow: 0 0 10px #0ff; }
        50% { box-shadow: 0 0 20px #00dfd8, 0 0 30px #007cf0; }
        100% { box-shadow: 0 0 10px #0ff; }
    }
    @media (max-width: 900px) {
        .tech-stack-grid {
            gap: 1rem;
        }
        .tech-box {
            width: 100px;
            height: 100px;
            padding: 1rem 0.7rem 0.7rem 0.7rem;
        }
    }
    @media (max-width: 700px) {
        .category-title {
            font-size: 1.1rem;
            padding: 0.2rem 0.7rem;
        }
        .tech-box {
            width: 90px;
            height: 90px;
            font-size: 0.9rem;
        }
    }
    </style>
    <div id="skills" class="about-section-box" style="align-items:center;">
        <div class="about-title" style="margin-bottom:2.2rem;">🛠 Tech Stack</div>
        <div class="tech-category">
            <div class="category-title">Languages</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-python"><div class="tech-icon">🐍</div><div class="tech-name">Python</div></div>
                <div class="tech-box tech-js"><div class="tech-icon">✨</div><div class="tech-name">JavaScript</div></div>
                <div class="tech-box tech-dart"><div class="tech-icon">🎯</div><div class="tech-name">Dart</div></div>
            </div>
        </div>
        <div class="tech-category">
            <div class="category-title">Frameworks</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-flutter"><div class="tech-icon">📱</div><div class="tech-name">Flutter</div></div>
                <div class="tech-box tech-fastapi"><div class="tech-icon">⚡</div><div class="tech-name">FastAPI</div></div>
                <div class="tech-box tech-react"><div class="tech-icon">⚛️</div><div class="tech-name">React</div></div>
            </div>
        </div>
        <div class="tech-category">
            <div class="category-title">Tools</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-git"><div class="tech-icon">🌱</div><div class="tech-name">Git</div></div>
                <div class="tech-box tech-docker"><div class="tech-icon">🐳</div><div class="tech-name">Docker</div></div>
                <div class="tech-box tech-firebase"><div class="tech-icon">🔥</div><div class="tech-name">Firebase</div></div>
                <div class="tech-box tech-aws"><div class="tech-icon">☁️</div><div class="tech-name">AWS</div></div>
            </div>
        </div>
        <div class="tech-category">
            <div class="category-title">Database</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-dynamodb"><div class="tech-icon">🔷</div><div class="tech-name">DynamoDB</div></div>
                <div class="tech-box tech-postgresql"><div class="tech-icon">🐘</div><div class="tech-name">PostgreSQL</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)