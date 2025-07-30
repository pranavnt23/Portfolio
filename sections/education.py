import streamlit as st

def render_education():
    st.markdown("""
    <style>
    .edu-section {
        max-width: 700px;
        margin: 0 auto 36px auto;
        padding: 1.5rem 1.2rem 1.2rem 1.2rem;
        border-radius: 18px;
        background: linear-gradient(120deg, #a18cd1 0%, #fbc2eb 100%);
        box-shadow: 0 4px 24px #a18cd155, 0 1.5px 8px #fff4;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .edu-title {
        font-size: 2em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 1.2rem;
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
        text-align: center;
    }
    .edu-card {
        background: #fff;
        border-radius: 14px;
        box-shadow: 0 2px 12px #a18cd133;
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
    .edu-card:last-child {
        margin-bottom: 0;
    }
    .edu-degree {
        font-size: 1.18em;
        font-weight: 700;
        color: #8f5fd1;
        margin-bottom: 0.2em;
        letter-spacing: 0.5px;
    }
    .edu-institute {
        font-size: 1.05em;
        font-weight: 600;
        color: #222;
        margin-bottom: 0.3em;
    }
    .edu-details {
        font-size: 1em;
        color: #444;
        margin-bottom: 0.2em;
    }
    .edu-score {
        font-size: 1em;
        font-weight: 600;
        color: #c471f5;
        margin-top: 0.2em;
    }
    @media (max-width: 800px) {
        .edu-section { padding: 1rem 0.3rem; }
        .edu-title { font-size: 1.2em; padding: 0.2rem 0.7rem; }
        .edu-card { padding: 0.8rem 0.5rem 0.7rem 0.5rem; }
    }
    </style>
    <div class="edu-section" id="education">
        <div class="edu-title">🎓 Education</div>
        <div class="edu-card">
            <div class="edu-degree">M.Sc. Software Systems (Integrated)</div>
            <div class="edu-institute">Coimbatore Institute of Technology</div>
            <div class="edu-details">2022/10 – Present | Coimbatore, India</div>
            <div class="edu-score">CGPA: 8.395 <span style="font-size:0.95em;font-weight:400;">(Till 5th sem)</span></div>
        </div>
        <div class="edu-card">
            <div class="edu-degree">Higher Secondary - 12th Grade</div>
            <div class="edu-institute">Sri Chaitanya Senior Secondary School</div>
            <div class="edu-details">2021/07 – 2022/07 | Coimbatore, India</div>
            <div class="edu-score">Percentage: 87.8</div>
        </div>
        <div class="edu-card">
            <div class="edu-degree">Secondary - 10th Grade</div>
            <div class="edu-institute">Kathir Vidyaa Mandhir</div>
            <div class="edu-details">2019/06 – 2020/05 | Coimbatore, India</div>
            <div class="edu-score">Percentage: 90.2</div>
        </div>
    </div>
    """, unsafe_allow_html=True)