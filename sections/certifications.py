import streamlit as st

def render_certifications():
    st.markdown("""
    <style>
    .certifications-section {
        margin: 0 auto 36px auto;
        max-width: 90vw;
        width: 90vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 2;
    }
    .certifications-title {
        font-size: 2em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 18px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        padding: 0.3rem 1.2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px #c471f555;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
    }
    .certifications-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: center;
        width: 100%;
    }
    .cert-card {
        background: linear-gradient(135deg, #00e6ff 0%, #c471f5 100%);
        border-radius: 18px;
        box-shadow: 0 4px 24px #00e6ff55, 0 1.5px 8px #fff4;
        padding: 2rem 1.5rem 1.5rem 1.5rem;
        min-width: 260px;
        max-width: 320px;
        flex: 1 1 280px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        transition: transform 0.22s cubic-bezier(.68,-0.55,.27,1.55), box-shadow 0.22s;
        position: relative;
        overflow: hidden;
        margin-bottom: 0.5rem;
    }
    .cert-card:hover {
        transform: scale(1.04) translateY(-6px);
        box-shadow: 0 8px 32px #8f5fd177, 0 2px 12px #fff7;
    }
    .cert-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
        filter: drop-shadow(0 2px 8px #00e6ff66);
    }
    .cert-title {
        font-size: 1.15em;
        font-weight: 700;
        margin-bottom: 0.5em;
        color: #fff;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #c471f555;
    }
    .cert-org {
        font-size: 1em;
        font-weight: 500;
        color: #e0f7fa;
        margin-bottom: 0.3em;
    }
    @media (max-width: 900px) {
        .certifications-grid {
            gap: 1.2rem;
        }
        .cert-card {
            min-width: 180px;
            max-width: 95vw;
            padding: 1.2rem 1rem 1rem 1rem;
        }
    }
    @media (max-width: 700px) {
        .certifications-title {
            font-size: 1.2em;
            padding: 0.2rem 0.7rem;
        }
        .certifications-grid {
            flex-direction: column;
            align-items: center;
        }
        .cert-card {
            width: 95vw;
            min-width: 0;
            max-width: 98vw;
            padding: 1rem 0.7rem 0.7rem 0.7rem;
        }
    }
    </style>
    <div id="certifications" class="certifications-section">
        <div class="certifications-title">🎓 Certifications</div>
        <div class="certifications-grid">
            <div class="cert-card">
                <div class="cert-icon">🤖</div>
                <div class="cert-title">Machine Learning</div>
                <div class="cert-org">Certificate</div>
            </div>
            <div class="cert-card">
                <div class="cert-icon">☁️</div>
                <div class="cert-title">Google Cloud Study Jam</div>
                <div class="cert-org">Google Cloud</div>
            </div>
            <div class="cert-card">
                <div class="cert-icon">🐍</div>
                <div class="cert-title">The Joy of Computing Using Python</div>
                <div class="cert-org">NPTEL</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)