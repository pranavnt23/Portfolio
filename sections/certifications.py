import streamlit as st

def render_certifications():
    st.markdown("""
    <style>
    .certifications-section {
        margin: 0 auto 36px auto;
        max-width: 900px;
        width: 100%;
        background: rgba(20, 18, 38, 0.82);
        border-radius: 24px;
        box-shadow: 0 4px 24px #00e6ff55, 0 1.5px 8px #fff4;
        padding: 24px 12px 18px 12px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        font-size: 0.90em;           /* Decreased font size */
        font-weight: 400;
        line-height: 1.6;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        border: 2.5px solid #00e6ff;
        z-index: 2;
        animation: fade-in-up 1s ease-out 2.2s forwards;
        opacity: 0;
        box-sizing: border-box;
    }
    .certifications-title {
        font-size: 1.3em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 14px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        padding: 0.2rem 0.8rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px #c471f555;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
        margin-left: auto;
        margin-right: auto;
    }
    .certifications-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1.2rem;
        justify-content: center;
        align-items: center;
        width: 100%;
        box-sizing: border-box;
    }
    .cert-card {
        background: linear-gradient(135deg, #00e6ff 0%, #c471f5 100%);
        border-radius: 14px;
        box-shadow: 0 4px 18px #00e6ff55, 0 1.5px 8px #fff4;
        padding: 1.2rem 0.8rem 0.8rem 0.8rem;
        min-width: 180px;
        max-width: 320px;
        flex: 1 1 220px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: transform 0.22s cubic-bezier(.68,-0.55,.27,1.55), box-shadow 0.22s;
        position: relative;
        overflow: hidden;
        margin-bottom: 0.5rem;
        font-size: 0.95em;
        box-sizing: border-box;
        text-align: center;
    }
    .cert-card:hover {
        transform: scale(1.04) translateY(-6px);
        box-shadow: 0 8px 32px #8f5fd177, 0 2px 12px #fff7;
    }
    .cert-icon {
        font-size: 1.5em;
        margin-bottom: 8px;
        filter: drop-shadow(0 2px 8px #00e6ff66);
    }
    .cert-title {
        font-size: 1em;
        font-weight: 700;
        margin-bottom: 0.4em;
        color: #fff;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #c471f555;
    }
    .cert-org {
        font-size: 0.95em;
        font-weight: 500;
        color: #e0f7fa;
        margin-bottom: 0.2em;
    }
    @media (max-width: 900px) {
        .certifications-section {
            max-width: 98vw;
            padding: 16px 2vw 16px 2vw;
        }
        .certifications-grid {
            gap: 0.7rem;
        }
        .cert-card {
            min-width: 140px;
            max-width: 95vw;
            padding: 1rem 0.5rem 0.7rem 0.5rem;
        }
    }
    @media (max-width: 700px) {
        .certifications-section {
            max-width: 100vw;
            padding: 10px 0 10px 0;
        }
        .certifications-title {
            font-size: 1em;
            padding: 0.15rem 0.5rem;
        }
        .certifications-grid {
            flex-direction: column;
            align-items: center;
            width: 100vw;
            margin: 0 auto;
        }
        .cert-card {
            width: 95vw;
            min-width: 0;
            max-width: 98vw;
            padding: 0.7rem 0.3rem 0.5rem 0.3rem;
            margin-left: auto;
            margin-right: auto;
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