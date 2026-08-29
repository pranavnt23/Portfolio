import streamlit as st

def render_education():
    st.markdown("""
    <div class="edu-section" id="education">
        <div class="edu-title">🎓 Education</div>
        <div class="edu-card">
            <div class="edu-degree">M.Sc. Software Systems (Integrated)</div>
            <div class="edu-institute">Coimbatore Institute of Technology</div>
            <div class="edu-details">2022/10 – Present | Coimbatore, India</div>
            <div class="edu-score">CGPA: 8.43 <span style="font-size:0.95em;font-weight:400;">(Till 8th Semester)</span></div>
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