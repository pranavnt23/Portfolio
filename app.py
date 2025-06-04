import streamlit as st
import base64

st.set_page_config(
    page_title="Pranav's Portfolio",
    page_icon="💡",
    layout="wide"
)

# Custom CSS for a modern purple gradient and hero section
st.markdown("""
    <style>
        /* Remove default margin/padding from the top */
        .stApp {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        body {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        .stApp {
            background: linear-gradient(120deg, #8f5fd1 0%, #c471f5 100%);
            min-height: 100vh;
            color: #fff !important;
        }
        .navbar {
            display: flex;
            justify-content: flex-end;
            flex-wrap: wrap;
            gap: 18px;
            margin-bottom: 30px;
            margin-top: 0px; /* Reduced from 10px */
            padding-right: 1vw;
            opacity: 0;
            transform: translateY(-20px); /* Reduced from -30px */
            animation: navbar-fade-in 1s ease-out 0.3s forwards;
        }
        @keyframes navbar-fade-in {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .nav-link {
            display: inline-block;
            margin: 6px 0;
            padding: 12px 32px;
            background: linear-gradient(90deg, #fff 0%, #8f5fd1 100%);
            color: #8f5fd1 !important;
            border-radius: 30px;
            font-weight: 700;
            font-size: 1.08em;
            text-decoration: none !important;
            box-shadow: 0 4px 16px #8f5fd155, 0 0 8px #fff2;
            transition: background 0.3s, color 0.3s, transform 0.2s, box-shadow 0.3s;
            border: 2px solid #fff;
            opacity: 0;
            transform: scale(0.8);
            animation: navlink-pop 0.5s cubic-bezier(.68,-0.55,.27,1.55) forwards;
        }
        .nav-link:nth-child(1) { animation-delay: 0.5s; }
        .nav-link:nth-child(2) { animation-delay: 0.65s; }
        .nav-link:nth-child(3) { animation-delay: 0.8s; }
        .nav-link:nth-child(4) { animation-delay: 0.95s; }
        .nav-link:nth-child(5) { animation-delay: 1.1s; }
        .nav-link:nth-child(6) { animation-delay: 1.25s; }
        @keyframes navlink-pop {
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        .nav-link:hover {
            background: linear-gradient(90deg, #fbc2eb 0%, #fff 100%);
            color: #6a3093 !important;
            transform: scale(1.08);
            box-shadow: 0 6px 24px #fff2, 0 0 16px #8f5fd1;
            border: 2px solid #8f5fd1;
        }
        /* Hero section */
        .hero-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2px; /* Slightly reduced */
            margin-top: 1px;  /* Reduced from 40px */
            margin-bottom: 32px; /* Reduced from 48px */
            min-height: 32px; /* Slightly reduced */
            position: relative;
            z-index: 1;
        }
        .hero-img-container {
            position: relative;
            width: 320px;
            height: 320px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .hero-img-bg {
            position: absolute;
            width: 320px;
            height: 320px;
            border-radius: 50%;
            background: radial-gradient(circle, #fff2 60%, #8f5fd1 100%);
            left: 0;
            top: 0;
            z-index: 0;
            animation: hero-bg-pop 1.2s cubic-bezier(.68,-0.55,.27,1.55) 0.7s forwards;
            opacity: 0;
        }
        @keyframes hero-bg-pop {
            to {
                opacity: 1;
                transform: scale(1.05);
            }
        }
        .hero-img {
            width: 260px;
            height: 320px;
            object-fit: cover;
            border-radius: 24px;
            border: 6px solid #fff;
            box-shadow: 0 8px 32px #8f5fd1aa;
            position: relative;
            z-index: 1;
            animation: hero-img-fade 1.2s cubic-bezier(.68,-0.55,.27,1.55) 1s forwards;
            opacity: 0;
        }
        @keyframes hero-img-fade {
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        .hero-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: center;
            gap: 14px; /* Slightly reduced */
            z-index: 2;
        }
        .hero-title {
            font-size: 2.8em;
            font-weight: 900;
            letter-spacing: 2px;
            color: #fff;
            margin-bottom: 0.1em;
            text-shadow: 2px 2px 16px #8f5fd1aa;
            animation: fade-in-up 1s ease-out 1.2s forwards;
            opacity: 0;
        }
        .hero-subtitle {
            font-size: 1.5em;
            font-weight: 700;
            color: #fbc2eb;
            margin-bottom: 0.2em;
            letter-spacing: 1px;
            animation: fade-in-up 1s ease-out 1.4s forwards;
            opacity: 0;
        }
        .hero-about {
            font-size: 1.18em;
            color: #2d1457;
            background: rgba(255,255,255,0.85);
            border-radius: 18px;
            padding: 20px 28px;
            box-shadow: 0 2px 12px #c471f555;
            font-weight: 500;
            line-height: 1.7;
            animation: fade-in-up 1s ease-out 1.6s forwards;
            opacity: 0;
        }
        @keyframes fade-in-up {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @media (max-width: 1100px) {
            .hero-section {
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
            .hero-content {
                align-items: center;
            }
        }
        @media (max-width: 600px) {
            .hero-img-container, .hero-img-bg {
                width: 200px;
                height: 200px;
            }
            .hero-img {
                width: 140px;
                height: 180px;
            }
            .hero-title {
                font-size: 2em;
            }
            .hero-subtitle {
                font-size: 1.1em;
            }
        }
        #MainMenu, header, footer {
            visibility: hidden;
            height: 0;
        }
        /* Remove Streamlit's default block container padding */
        section.main > div:first-child {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        .block-container {
            padding-top: 0rem !important;
            margin-top: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="navbar">
    <a class="nav-link" href="#home">Home</a>
    <a class="nav-link" href="#about">About</a>
    <a class="nav-link" href="#skills">Skills</a>
    <a class="nav-link" href="#project">Project</a>
    <a class="nav-link" href="#certifications">Certifications</a>
    <a class="nav-link" href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# Hero Section (about left, image right, same line)
st.markdown(f"""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-title">WE ARE<br> <span style="color:#00e6ff;font-family:monospace;font-size:1.2em;">Powerful</span></div>
        <div class="hero-subtitle">Streamlined Software Developer</div>
        <div class="hero-about">
            Streamlined software developer with strong coding and application development skills, efficient in problem-solving and eager to explore new opportunities in the software industry.
        </div>
    </div>
    <div class="hero-img-container">
        <div class="hero-img-bg"></div>
        <img src="data:image/jpeg;base64,{img_base64}" alt="Profile Photo" class="hero-img">
    </div>
</div>
""", unsafe_allow_html=True)