import streamlit as st

def render_projects():
    st.markdown("""
    <style>
    .projects-section {
        margin: 0 auto 36px auto;
        max-width: 90vw;
        width: 90vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 2;
    }
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
        animation: glow 2s infinite ease-in-out;
    }
    .projects-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: center;
        width: 100%;
    }
    .project-card {
        background: linear-gradient(135deg, #8f5fd1 0%, #c471f5 100%);
        border-radius: 18px;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
        padding: 2rem 1.5rem 1.5rem 1.5rem;
        min-width: 290px;
        max-width: 340px;
        flex: 1 1 320px;
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
    .project-card:hover {
        transform: scale(1.04) translateY(-6px);
        box-shadow: 0 8px 32px #00e6ff77, 0 2px 12px #fff7;
    }
    .project-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
        filter: drop-shadow(0 2px 8px #00e6ff66);
    }
    .project-title {
        font-size: 1.25em;
        font-weight: 700;
        margin-bottom: 0.5em;
        color: #fff;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #c471f555;
    }
    .project-desc {
        font-size: 1.05em;
        font-weight: 400;
        margin-bottom: 0.7em;
        color: #f3eaff;
        line-height: 1.5;
    }
    .project-tech {
        font-size: 0.98em;
        color: #00e6ff;
        font-weight: 600;
        margin-bottom: 0.5em;
    }
    @media (max-width: 900px) {
        .projects-grid {
            gap: 1.2rem;
        }
        .project-card {
            min-width: 220px;
            max-width: 95vw;
            padding: 1.2rem 1rem 1rem 1rem;
        }
    }
    @media (max-width: 700px) {
        .projects-title {
            font-size: 1.2em;
            padding: 0.2rem 0.7rem;
        }
        .projects-grid {
            flex-direction: column;
            align-items: center;
            width: 100vw;
            margin: 0 auto;
        }
        .project-card {
            width: 95vw;
            min-width: 0;
            max-width: 98vw;
            padding: 1rem 0.7rem 0.7rem 0.7rem;
            margin-left: auto;
            margin-right: auto;
        }
    }
    </style>
    <div id="project" class="projects-section">
        <div class="projects-title">🚀 Projects</div>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-icon">💸</div>
                <div class="project-title">FundVerse - ChitFund Platform</div>
                <div class="project-desc">
                    Developing a full stack Chitfund platform to efficiently automate operations, ensuring secure and streamlined processes for all stakeholders.
                </div>
                <div class="project-tech">#FullStack #Automation #Fintech</div>
            </div>
            <div class="project-card">
                <div class="project-icon">✈️</div>
                <div class="project-title">Flight Delay Prediction Model</div>
                <div class="project-desc">
                    Built a machine learning model using Linear Regression and Random Forest Classifier to predict flight delays based on past data and multiple scenarios.
                </div>
                <div class="project-tech">#ML #Regression #RandomForest</div>
            </div>
            <div class="project-card">
                <div class="project-icon">🪑</div>
                <div class="project-title">Seating Allocation System</div>
                <div class="project-desc">
                    Automated University Seating Allocation System in Java, streamlining seat assignments for exams and events, enhancing efficiency, accuracy, and fairness.
                </div>
                <div class="project-tech">#Java #Automation #University</div>
            </div>
            <div class="project-card">
                <div class="project-icon">📊</div>
                <div class="project-title">Flight Delay Analysis Dashboard</div>
                <div class="project-desc">
                    PowerBI dashboard visualizing flight delays based on various parameters, helping to analyze and understand delay patterns using historical data.
                </div>
                <div class="project-tech">#PowerBI #Visualization #Analytics</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)