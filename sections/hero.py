import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_hero(img_path):
    img_base64 = get_base64_of_bin_file(img_path)
    st.markdown(f"""
    <style>
    .hero-section {{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        padding: 24px 0 12px 0;
        font-size: 0.92em;
    }}
    .hero-content {{
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        font-size: 0.95em;
    }}
    .hero-about-title {{
        font-size: 1.1em;
        font-weight: 600;
    }}
    .hero-img-container {{
        flex: 0 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-left: 18px;
    }}
    .hero-img {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #c471f5;
        box-shadow: 0 2px 12px #c471f555;
    }}
    @media (max-width: 700px) {{
        .hero-section {{
            flex-direction: column;
            padding: 12px 0 6px 0;
            font-size: 0.85em;
        }}
        .hero-img-container {{
            margin-left: 0;
            margin-top: 12px;
        }}
        .hero-img {{
            width: 90px;
            height: 90px;
        }}
    }}
    </style>
    <div class="hero-section" id="home">
        <div class="hero-content">
            <div class="hero-about">
                <span class="hero-about-title">Myself</span><br>
                Hi! I’m <b>Pranav</b>,<br>
                A soul who finds rhythm in singing and strength in workouts, blending creativity with discipline to lead a fulfilling life.<br>
                Whether it’s a melody or a mindset, always tuned in to growth.<br><br>
                I'm currently pursuing <b>M.Sc Software Systems (Integrated)</b> at <b>Coimbatore Institute of Technology</b>, where I’m honing both my technical and problem-solving skills.
                <br><br>
            </div>
        </div>
        <div class="hero-img-container">
            <img src="data:image/png;base64,{img_base64}" alt="Profile Photo" class="hero-img">
        </div>
    </div>
    """, unsafe_allow_html=True)