import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_hero(img_path):
    st.markdown(f"""
    <div class="hero-section" id="home">
        <div class="hero-content">
            <div class="hero-about">
                <span class="hero-about-title">Myself</span><br>
                Hi! I’m <b>Pranav</b>, a passionate and curious developer with a strong foundation in software engineering and a love for building impactful digital solutions.<br>
                I'm currently pursuing <b>M.Sc Software Systems (Integrated)</b> at <b>Coimbatore Institute of Technology</b>, where I’m honing both my technical and problem-solving skills.
                <br><br>
            </div>
        </div>
        <div class="hero-img-container">
            <img src="{img_path}" alt="Profile Photo" class="hero-img">
        </div>
    </div>
    """, unsafe_allow_html=True)