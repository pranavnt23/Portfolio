import streamlit as st

def render_navbar():
    st.markdown("""
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