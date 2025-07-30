import streamlit as st

def render_projects():
    st.markdown("""
    <style>
    .projects-title {
        font-size: 2em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 18px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        background: linear-gradient(90deg, #8f5fd1 0%, #c471f5 100%);
        padding: 0.3rem 1.2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px #c471f555;
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
        display: block;
        text-align: center;
    }
    /* Style for Streamlit expanders */
    .stExpander {
        border-radius: 8px !important;
        margin-bottom: 1.2rem !important;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4 !important;
        background: linear-gradient(160deg, #6a11cb 0%, #2575fc 100%) !important;

    }
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #a18cd1 0%, #fbc2eb 100%) !important;
        color: #fff !important;
        font-weight: 900 !important;
        text-align: center !important;
        border-radius: 16px 16px 0 0 !important;
        font-size: 1.3em !important;
        letter-spacing: 1px;
        box-shadow: 0 2px 8px #a18cd188;
        border-bottom: 2px solid #a18cd1 !important;
        margin: 0 auto !important;
        display: flex !important;
        justify-content: center !important;
        padding: 1.2em 0 !important;
        min-height: 60px !important;
    }
    .streamlit-expanderContent {
        background: linear-gradient(120deg, #f7971e 0%, #ffd200 100%) !important;
        color: #222 !important;
        border-radius: 0 0 16px 16px !important;
        font-size: 0.7em !important;
        margin-bottom: 0.5em;
        text-align: center !important;
        font-weight: 300 !important;
        box-shadow: 0 2px 8px #ffd20055;
    }
    </style>
    <div class="projects-title" id="projects">🚀 Projects</div>
    """, unsafe_allow_html=True)

    with st.expander("💸 FundVerse - ChitFund Platform"):
        st.markdown("""
        <div style="font-weight:700; text-align:center;">
        Developing a full stack Chitfund platform to efficiently automate operations, ensuring secure and streamlined processes for all stakeholders.<br>
        <a href="https://github.com/pranavnt23/ChitFund_Platform" target="_blank" style="display:inline-block;margin-top:8px;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="28" style="vertical-align:middle;"/> 
            <span style="font-size:1.1em;vertical-align:middle;font-weight:700;color:#222;margin-left:6px;">GitHub</span>
        </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("✈️ Flight Delay Prediction Model"):
        st.markdown("""
        <div style="font-weight:700; text-align:center;">
        Built a machine learning model using Linear Regression and Random Forest Classifier to predict flight delays based on past data and multiple scenarios.<br>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🪑 Seating Allocation System"):
        st.markdown("""
        <div style="font-weight:700; text-align:center;">
        Automated University Seating Allocation System in Java, streamlining seat assignments for exams and events, enhancing efficiency, accuracy, and fairness.<br>
        <a href="https://github.com/pranavnt23/Seating_Allocation" target="_blank" style="display:inline-block;margin-top:8px;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="28" style="vertical-align:middle;"/> 
            <span style="font-size:1.1em;vertical-align:middle;font-weight:700;color:#222;margin-left:6px;">GitHub</span>
        </a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📊 Flight Delay Analysis Dashboard"):
        st.markdown("""
        <div style="font-weight:700; text-align:center;">
        PowerBI dashboard visualizing flight delays based on various parameters, helping to analyze and understand delay patterns using historical data.<br>
        <a href="https://drive.google.com/drive/folders/1V9X4I4ibsFfS0XzFrSbSYct267jzFg0q" target="_blank" style="display:inline-block;margin-top:8px;">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" alt="Google Drive" width="28" style="vertical-align:middle;"/> 
            <span style="font-size:1.1em;vertical-align:middle;font-weight:700;color:#222;margin-left:6px;">Drive</span>
        </a>
        </div>
        """, unsafe_allow_html=True)