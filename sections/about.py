import streamlit as st

def render_about():
    st.markdown("""
    <style>
    .about-section-box {
        max-width: 900px;
        margin: 0 auto 36px auto;
        background: rgba(20, 18, 38, 0.82);
        border-radius: 24px;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
        padding: 28px 28px 18px 28px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        font-size: 0.90em; /* Decreased overall font size */
        font-weight: 400;
        line-height: 1.6;
        text-align: center;
        border: 2.5px solid #c471f5;
        box-sizing: border-box;
    }
    .about-title {
        font-size: 1.15em; /* Decreased title size */
        font-weight: 700;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }
    .about-content {
        font-size: 0.92em; /* Decreased content size */
    }
    .about-interests-title {
        font-size: 0.98em; /* Decreased interests title size */
        font-weight: 600;
    }
    .about-interests-list {
        list-style: none;
        padding: 0;
        margin: 10px 0 0 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
    }
    .interest-icon {
        font-size: 1em; /* Decreased icon size */
        margin-right: 4px;
    }
    .interest-title {
        font-size: 0.92em; /* Decreased interest text size */
        font-weight: 500;
    }
    @media (max-width: 700px) {
        .about-section-box {
            padding: 14px 2vw 10px 2vw;
            font-size: 0.85em;
        }
        .about-title {
            font-size: 1em;
        }
        .about-content {
            font-size: 0.85em;
        }
        .about-interests-title {
            font-size: 0.92em;
        }
        .interest-icon {
            font-size: 0.92em;
        }
        .interest-title {
            font-size: 0.85em;
        }
    }
    </style>
    <div id="about" class="about-section-box">
        <div class="about-title">
            🧑‍💻 About Me
        </div>
        <div class="about-content">
            Streamlined software developer with strong coding and application development skills, efficient in problem-solving and eager to explore new opportunities in the software industry.
            <br><br><span class="about-interests-title">🔍 I’m particularly interested in:</span>
            <ul class="about-interests-list">
                <li>
                    <span class="interest-icon">🌐</span>
                    <span class="interest-title">Full-Stack</span>
                </li>
                <li>
                    <span class="interest-icon">🤖</span>
                    <span class="interest-title">AI/ML</span>
                </li>
                <li>
                    <span class="interest-icon">💻</span>
                    <span class="interest-title">Open Source</span>
                </li>
                <li>
                    <span class="interest-icon">☁️</span>
                    <span class="interest-title">Cloud</span>
                </li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)