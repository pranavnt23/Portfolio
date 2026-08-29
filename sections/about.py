import streamlit as st
import base64
def render_about():
    st.markdown("""
    <div id="about" class="about-section-box">
        <div class="about-title">
            🧑‍💻 About Me
        </div>
        <div class="about-content">
            Software developer drawn to the space where ideas become real working solutions. Experienced in application development, AI systems, and cloud platforms, with a problem-solving mindset and a drive to turn ideas into technology that shapes what comes next.
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