import streamlit as st
import base64
import os

def get_base64_of_bin_file(bin_file):
    if not os.path.isabs(bin_file):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        bin_file = os.path.join(project_root, bin_file)
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_hero(img_path):
    img_base64 = get_base64_of_bin_file(img_path)
    st.markdown(f"""
<div class="hero-section" id="home">
<img src="data:image/jpeg;base64,{img_base64}" alt="Profile Photo" class="hero-profile-image">
<div class="hero-about">
<span class="hero-about-title">Myself</span>
<div class="hero-name">Hi! I’m Pranav</div>
<p class="hero-bio">
A soul who finds rhythm in singing and strength in workouts, blending creativity with discipline to lead a fulfilling life.<br>
Whether it’s a melody or a mindset, always tuned in to growth.<br><br>
I'm currently pursuing <b>M.Sc Software Systems (Integrated)</b> at <b>Coimbatore Institute of Technology</b>, where I’m honing both my technical and problem-solving skills.
</p>
</div>
</div>
""", unsafe_allow_html=True)