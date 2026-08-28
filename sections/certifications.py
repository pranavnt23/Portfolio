import streamlit as st

def render_certifications():
    st.markdown("""
    <div id="certifications" class="certifications-section">
        <div class="certifications-title">🎓 Certifications</div>
        <div class="certifications-grid">
            <a href="https://drive.google.com/file/d/1f5eEXBiPa7gWiLgzUWYe4qScNNkKp8kb/view?usp=sharing" target="_blank" style="text-decoration:none;">
                <div class="cert-card">
                    <div class="cert-icon">🤖</div>
                    <div class="cert-title">Machine Learning</div>
                    <div class="cert-org">Certificate</div>
                    <div style="margin-top:8px; display:flex; align-items:center; gap:6px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" alt="Google Drive" width="20"/>
                        <span style="font-size:0.95em; font-weight:600; color:#38bdf8;">View</span>
                    </div>
                </div>
            </a>
            <a href="https://drive.google.com/file/d/1UOB0rWG9Vs1T44uZ3N6MH7gD2s8rGIos/view?usp=sharing" target="_blank" style="text-decoration:none;">
                <div class="cert-card">
                    <div class="cert-icon">☁️</div>
                    <div class="cert-title">Google Cloud Study Jam</div>
                    <div class="cert-org">Google Cloud</div>
                    <div style="margin-top:8px; display:flex; align-items:center; gap:6px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" alt="Google Drive" width="20"/>
                        <span style="font-size:0.95em; font-weight:600; color:#38bdf8;">View</span>
                    </div>
                </div>
            </a>
            <a href="https://drive.google.com/file/d/1-rXH-UupyQyhcWmbAENMCHBDE3xJuZhK/view?usp=sharing" target="_blank" style="text-decoration:none;">
                <div class="cert-card">
                    <div class="cert-icon">🐍</div>
                    <div class="cert-title">The Joy of Computing Using Python</div>
                    <div class="cert-org">NPTEL</div>
                    <div style="margin-top:8px; display:flex; align-items:center; gap:6px;">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" alt="Google Drive" width="20"/>
                        <span style="font-size:0.95em; font-weight:600; color:#38bdf8;">View</span>
                    </div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)