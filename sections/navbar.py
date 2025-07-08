import streamlit as st

def render_navbar():
    st.markdown("""
    <style>
        /* Add this CSS to your style section for a smaller navbar */
        .navbar {
            gap: 18px !important;
            padding-right: 1vw !important;
            height: 48px !important;
        }
        .nav-link {
            font-size: 0.95em !important;
            padding: 0 4px 2px 2px !important;
        }
        .nav-icon {
            width: 14px !important;
            height: 14px !important;
            margin-right: 4px !important;
        }
        .navbar-logo {
            width: 28px !important;
            height: 28px !important;
            margin-right: 8px !important;
        }
    </style>
    <div class="navbar-header-bg">
        <div class="navbar-header-content">
            <img class="navbar-logo" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo">
        </div>
    </div>
    <div class="navbar">
        <a class="nav-link" href="#home">
            <img src="https://img.icons8.com/ios-filled/20/ffffff/home.png" alt="Home" class="nav-icon" />
            Home
        </a>
        <a class="nav-link" href="#about">
            <img src="https://img.icons8.com/ios-filled/20/ffffff/user.png" alt="About" class="nav-icon" />
            About
        </a>
        <a class="nav-link" href="#skills">
            <img src="https://img.icons8.com/ios-filled/20/ffffff/maintenance.png" alt="Skills" class="nav-icon" />
            Skills
        </a>
        <a class="nav-link" href="#project">
            <img src="https://img.icons8.com/ios-filled/20/ffffff/project.png" alt="Project" class="nav-icon" />
            Project
        </a>
        <a class="nav-link" href="#certifications">
            <img src="https://img.icons8.com/ios-filled/20/ffffff/certificate.png" alt="Certifications" class="nav-icon" />
            Certifications
        </a>
        <a class="nav-link" href="#contact">
            <img src="https://img.icons8.com/ios-filled/20/ffffff/secured-letter.png" alt="Contact" class="nav-icon" />
            Contact
        </a>
    </div>
    """, unsafe_allow_html=True)