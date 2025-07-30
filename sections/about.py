import streamlit as st
import base64
def render_about():
    st.markdown("""
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