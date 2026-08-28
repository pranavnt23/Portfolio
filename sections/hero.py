import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_hero(img_path):
    img_base64 = get_base64_of_bin_file(img_path)
    st.markdown(f"""
    <div class="hero-section" id="home">
        <div class="hero-about">
            <span class="hero-about-title">Myself</span>
            Hi! I’m <span class="hero-name">Pranav</span>,<br>
            A soul who finds rhythm in singing and strength in workouts, blending creativity with discipline to lead a fulfilling life.<br>
            Whether it’s a melody or a mindset, always tuned in to growth.<br><br>
            I'm currently pursuing <b>M.Sc Software Systems (Integrated)</b> at <b>Coimbatore Institute of Technology</b>, where I’m honing both my technical and problem-solving skills.
        </div>
        <div class="hero-pic-container">
            <img src="data:image/jpeg;base64,{img_base64}" alt="Profile Photo" class="hero-pic">
        </div>
    </div>
    """, unsafe_allow_html=True)