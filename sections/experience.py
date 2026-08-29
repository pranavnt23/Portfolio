import streamlit as st

def render_experience():
    st.markdown("""
    <div class="exp-section" id="experience">
        <div class="exp-title">💼 Work Experience</div>
        <div class="exp-card">
            <div class="exp-role">API Developer</div>
            <div class="exp-org">Satyukt Analytics Private Limited</div>
            <div class="exp-details">2025/06 - 2025/11 | Bengaluru, India</div>
            <div class="exp-desc">
                Developed backend APIs and Python services for Sat2Farm and ERP, implementing AWS cloud solutions with Lambda, API Gateway, DynamoDB, EC2, S3, and IAM, while automating workflows through EventBridge and Python scripts with SQL operations and deployments.
            </div>
        </div>
        <div class="exp-card">
            <div class="exp-role">Backend Developer</div>
            <div class="exp-org">Tia</div>
            <div class="exp-details">2024/03 – 2024/06 | Coimbatore, India</div>
            <div class="exp-desc">
                A forward-thinking company specializing in backend development using Node.js and AWS technologies, where I contributed to optimizing the backend structure for enhanced performance.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)