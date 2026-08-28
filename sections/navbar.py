import streamlit as st
import streamlit.components.v1 as components
import base64

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

def render_navbar():
    img_base64 = get_base64_of_bin_file("assets/pic.jpg")
    logo_html = f'<img class="navbar-logo" src="data:image/jpeg;base64,{img_base64}" alt="Logo">' if img_base64 else ''
    
    # Render navbar HTML structure in parent document
    st.markdown("""
    <div class="navbar-header-bg">
        <div class="navbar-header-content">
            """ + logo_html + """
            <span class="navbar-name">Pranav</span>
        </div>
        <button id="menu-toggle" class="menu-toggle-btn">☰</button>
    </div>
    <div class="navbar">
        <a class="nav-link" href="#home">
            <span class="nav-icon-emoji">🏠</span>
            Home
        </a>
        <a class="nav-link" href="#about">
            <span class="nav-icon-emoji">👤</span>
            About
        </a>
        <a class="nav-link" href="#skills">
            <span class="nav-icon-emoji">🛠</span>
            Skills
        </a>
        <a class="nav-link" href="#education">
            <span class="nav-icon-emoji">🎓</span>
            Education
        </a>
        <a class="nav-link" href="#experience">
            <span class="nav-icon-emoji">💼</span>
            Experience
        </a>
        <a class="nav-link" href="#responsibilities">
            <span class="nav-icon-emoji">🤝</span>
            Responsibilities
        </a>
        <a class="nav-link" href="#projects">
            <span class="nav-icon-emoji">🚀</span>
            Project
        </a>
        <a class="nav-link" href="#certifications">
            <span class="nav-icon-emoji">📜</span>
            Certifications
        </a>
        <a class="nav-link" href="#contact">
            <span class="nav-icon-emoji">📞</span>
            Contact
        </a>
        <button id="theme-toggle" class="theme-toggle-btn">🌙</button>
    </div>
    """, unsafe_allow_html=True)

    # Execute Javascript using components.html to bypass st.markdown innerHTML script blocks
    components.html("""
    <script>
    const parentDoc = window.parent.document;

    function applyTheme() {
        const currentTheme = localStorage.getItem('theme') || 'dark';
        
        // Target parent body and stApp view containers
        const targets = [
            parentDoc.body,
            parentDoc.querySelector('.stApp'),
            parentDoc.querySelector('[data-testid="stAppViewContainer"]')
        ];
        
        targets.forEach(el => {
            if (el) {
                if (currentTheme === 'light') {
                    el.classList.add('light-theme');
                } else {
                    el.classList.remove('light-theme');
                }
            }
        });
        
        const btn = parentDoc.getElementById('theme-toggle');
        if (btn) {
            btn.innerText = currentTheme === 'light' ? '☀️' : '🌙';
        }
    }

    function toggleTheme() {
        const currentTheme = localStorage.getItem('theme') || 'dark';
        const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
        localStorage.setItem('theme', nextTheme);
        applyTheme();
    }

    function toggleMenu() {
        const navbar = parentDoc.querySelector('.navbar');
        const toggleBtn = parentDoc.getElementById('menu-toggle');
        if (navbar) {
            if (navbar.classList.contains('active')) {
                navbar.classList.remove('active');
                if (toggleBtn) toggleBtn.innerText = '☰';
            } else {
                navbar.classList.add('active');
                if (toggleBtn) toggleBtn.innerText = '✕';
            }
        }
    }

    // Set up global click event delegation on the parent window document
    parentDoc.addEventListener("click", function(e) {
        // Toggle menu button click
        if (e.target && (e.target.id === 'menu-toggle' || e.target.closest('#menu-toggle'))) {
            e.preventDefault();
            toggleMenu();
            return;
        }
        
        // Toggle theme button click
        if (e.target && (e.target.id === 'theme-toggle' || e.target.closest('#theme-toggle'))) {
            e.preventDefault();
            toggleTheme();
            return;
        }
        
        // Smooth scroll listener
        const link = e.target.closest('.nav-link');
        if (link) {
            const href = link.getAttribute('href');
            if (href && href.startsWith("#")) {
                e.preventDefault();
                const target = parentDoc.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
                
                // Auto close mobile menu when link is clicked
                const navbar = parentDoc.querySelector('.navbar');
                const toggleBtn = parentDoc.getElementById('menu-toggle');
                if (navbar && navbar.classList.contains('active')) {
                    navbar.classList.remove('active');
                    if (toggleBtn) toggleBtn.innerText = '☰';
                }
            }
        }
    });

    // Run theme sync on load
    applyTheme();
    
    // Periodically re-enforce the theme class to prevent resets when Streamlit reruns
    if (!window.themeIntervalSet) {
        window.themeIntervalSet = true;
        setInterval(applyTheme, 300);
    }
    </script>
    """, height=0, width=0)