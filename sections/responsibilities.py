import streamlit as st

def render_responsibilities():
    st.markdown("""
    <style>
    .resp-section {
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
    .resp-title {
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
    .resp-card {
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
    .resp-card:last-child {
        margin-bottom: 0;
    }
    .resp-role {
        font-size: 1.18em;
        font-weight: 700;
        color: #185a9d;
        margin-bottom: 0.2em;
        letter-spacing: 0.5px;
    }
    .resp-org {
        font-size: 1.05em;
        font-weight: 600;
        color: #222;
        margin-bottom: 0.3em;
    }
    .resp-details {
        font-size: 1em;
        color: #444;
        margin-bottom: 0.2em;
    }
    @media (max-width: 800px) {
        .resp-section { padding: 1rem 0.3rem; }
        .resp-title { font-size: 1.2em; padding: 0.2rem 0.7rem; }
        .resp-card { padding: 0.8rem 0.5rem 0.7rem 0.5rem; }
    }
    </style>
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
