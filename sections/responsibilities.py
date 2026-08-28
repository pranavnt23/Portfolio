import streamlit as st

def render_responsibilities():
    st.markdown("""
    <div class="resp-section" id="responsibilities">
        <div class="resp-title">🤝 Club Responsibilities</div>
        <div class="resp-card">
            <div class="resp-role">Content Writer</div>
            <div class="resp-org">FOSS CIT</div>
            <div class="resp-details">May 2024 - April 2025</div>
        </div>
        <div class="resp-card">
            <div class="resp-role">International Service Director</div>
            <div class="resp-org">Rotaract Club of Coimbatore Institute of Technology</div>
            <div class="resp-details">July 2024 - June 2025</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True)
