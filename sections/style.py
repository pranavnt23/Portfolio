import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@500;700&display=swap');
    
    /* Theme variables - Pure Black & White Aesthetic */
    :root {
        --bg-color: #0f0f11;
        --text-color: #e5e5e7;
        --text-secondary: #9ca3af;
        --card-bg: #18181c;
        --card-border: #2e2e33;
        --navbar-bg: rgba(15, 15, 17, 0.85);
        --navbar-border: #222226;
        --accent-color: #f1f5f9;
        --accent-hover: #ffffff;
        --accent-text: #6366f1;
        --input-bg: #121214;
        --input-border: #2e2e33;
        --btn-bg: #e5e5e7;
        --btn-text: #0f0f11;
        --btn-hover-bg: #ffffff;
    }
    
    body.light-theme {
        --bg-color: #ffffff;
        --text-color: #1c1c1e;
        --text-secondary: #6b7280;
        --card-bg: #f9f9fb;
        --card-border: #e5e5ea;
        --navbar-bg: rgba(255, 255, 255, 0.85);
        --navbar-border: #e5e5ea;
        --accent-color: #1c1c1e;
        --accent-hover: #000000;
        --accent-text: #4f46e5;
        --input-bg: #ffffff;
        --input-border: #d1d1d6;
        --btn-bg: #1c1c1e;
        --btn-text: #ffffff;
        --btn-hover-bg: #000000;
    }
    
    /* Global Base */
    html {
        scroll-behavior: smooth !important;
    }
    
    html, body, .stApp {
        height: 100%;
        min-height: 100vh;
        background-color: var(--bg-color) !important;
        background-image: none !important;
        color: var(--text-color) !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    
    /* Global overrides for Streamlit dynamic parent components */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-color) !important;
        color: var(--text-color) !important;
    }
    
    /* Reset all Streamlit default margins/padding that conflict */
    #MainMenu, header, footer {
        visibility: hidden; 
        height: 0;
    }
    
    .block-container {
        padding-top: 110px !important;
        padding-bottom: 60px !important;
        max-width: 900px !important;
    }
    
    /* Scrollbar customization */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: var(--bg-color);
    }
    ::-webkit-scrollbar-thumb {
        background: var(--card-border);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: var(--text-secondary);
    }
    
    /* Fixed Header Background */
    .navbar-header-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 70px;
        background: var(--navbar-bg) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        z-index: 999;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border-bottom: 1px solid var(--navbar-border);
        display: flex;
        align-items: center;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }
    
    .navbar-header-content {
        display: flex;
        align-items: center;
        height: 70px;
        max-width: 100vw;
        padding-left: 32px;
        z-index: 1001;
        position: relative;
    }
    
    .navbar-logo {
        width: 32px !important;
        height: 32px !important;
        margin-right: 10px !important;
        vertical-align: middle;
        border-radius: 50%;
        background: #ffffff !important;
        object-fit: cover;
        padding: 3px !important;
        border: 1px solid var(--navbar-border) !important;
    }
    
    .navbar-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.6em;
        font-weight: 700;
        color: var(--accent-color);
        letter-spacing: 0.5px;
        margin-right: 36px;
        user-select: none;
        transition: color 0.3s ease;
    }
    
    /* Navbar Navigation Links */
    .navbar {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px !important;
        margin-bottom: 0px;
        margin-top: 0px;
        padding-right: 3vw;
        padding-top: 20px;
        padding-bottom: 20px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background: none;
        box-shadow: none;
        height: 70px;
    }
    
    .nav-link {
        display: inline-block;
        background: none;
        color: var(--text-secondary) !important;
        border: none;
        border-radius: 0;
        font-weight: 500;
        font-size: 0.95em !important;
        font-family: 'Inter', sans-serif !important;
        text-decoration: none !important;
        box-shadow: none;
        margin: 0;
        padding: 0 4px 6px 4px !important;
        position: relative;
        transition: color 0.3s, transform 0.3s;
        text-transform: capitalize;
        letter-spacing: 0.3px;
    }
    
    .nav-link:after {
        content: "";
        display: block;
        width: 0;
        height: 2px;
        background: var(--accent-color);
        border-radius: 1px;
        transition: width 0.3s ease;
        position: absolute;
        left: 0;
        bottom: 0;
    }
    
    .nav-link:hover, .nav-link:focus {
        color: var(--accent-color) !important;
    }
    
    .nav-link:hover:after, .nav-link:focus:after {
        width: 100%;
    }
    
    .nav-icon-emoji {
        font-size: 1.1em !important;
        margin-right: 6px !important;
        vertical-align: middle;
        display: inline-block;
    }
    
    /* Theme Toggle Button */
    .theme-toggle-btn {
        background: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        color: var(--text-color) !important;
        padding: 6px 12px !important;
        border-radius: 20px !important;
        font-size: 1em !important;
        cursor: pointer !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.3s ease !important;
        margin-left: 10px !important;
        outline: none !important;
    }
    .theme-toggle-btn:hover {
        border-color: var(--accent-color) !important;
        transform: scale(1.05);
    }
    
    /* Mobile Hamburger Menu Icon (3 lines) */
    .menu-toggle-btn {
        display: none;
        background: none !important;
        border: none !important;
        color: var(--text-color) !important;
        font-size: 1.8em !important;
        cursor: pointer !important;
        position: absolute !important;
        right: 24px !important;
        top: 15px !important;
        z-index: 1002 !important;
        outline: none !important;
        transition: transform 0.2s ease !important;
    }
    .menu-toggle-btn:hover {
        transform: scale(1.1);
    }
    
    /* Section Scroll Margins (Fix navbar overlap cut-off) */
    .hero-section,
    .about-section-box,
    .edu-section,
    .exp-section,
    .resp-section,
    .projects-title,
    .certifications-section,
    .contact-section-box {
        scroll-margin-top: 100px !important;
    }
    
    /* Hero Section */
    .hero-section {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        gap: 40px;
        padding: 40px 0;
        width: 100%;
    }
    
    .hero-content {
        flex: 1;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        width: 100%;
    }
    
    .hero-about {
        flex: 1.2;
        padding-right: 20px;
        font-size: 1.1em;
        line-height: 1.7;
        color: var(--text-secondary);
    }
    
    .hero-about-title {
        display: block;
        font-family: 'Playfair Display', serif;
        font-size: 1.4em;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: var(--text-color);
        margin-bottom: 12px;
    }
    
    .hero-name {
        color: var(--accent-color);
        font-weight: 800;
        font-size: 2.5em;
        line-height: 1.2;
    }
    
    .hero-pic-container {
        flex: 0.8;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .hero-pic {
        width: 250px;
        height: 250px;
        border-radius: 24px;
        object-fit: cover;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid var(--card-border);
        transition: transform 0.3s ease;
    }
    .hero-pic:hover {
        transform: translateY(-5px);
    }
    
    /* Sections Headers */
    .about-title, .edu-title, .exp-title, .resp-title, .projects-title, .certifications-title, .contact-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.2em;
        font-weight: 700;
        color: var(--accent-color);
        margin-bottom: 24px;
        position: relative;
        display: inline-block;
        padding-bottom: 6px;
    }
    .about-title:after, .edu-title:after, .exp-title:after, .resp-title:after, .projects-title:after, .certifications-title:after, .contact-title:after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 40px;
        height: 2px;
        background: var(--accent-color);
    }
    
    /* General Card Layouts */
    .edu-card, .exp-card, .resp-card, .about-section-box, .contact-section-box {
        background-color: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 16px !important;
        padding: 2rem !important;
        margin-bottom: 20px !important;
        transition: transform 0.2s, box-shadow 0.2s, background-color 0.3s;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
    }
    
    .edu-card:hover, .exp-card:hover, .resp-card:hover, .about-section-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        border-color: var(--text-secondary) !important;
    }
    
    /* About Box Specifics */
    .about-section-box {
        margin-top: 20px;
    }
    .about-text {
        font-size: 1.1em;
        line-height: 1.8;
        color: var(--text-secondary);
    }
    
    /* Tech Stack / Skills Styling */
    .tech-category {
        margin-bottom: 2.5rem;
    }
    .category-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: var(--accent-color);
        margin-bottom: 1.2rem;
        font-family: 'Playfair Display', serif;
    }
    .tech-stack-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
        gap: 12px;
        width: 100%;
    }
    .tech-box {
        background-color: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 10px;
        padding: 10px 14px;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.2s ease-in-out;
        justify-content: flex-start;
    }
    .tech-box:hover {
        border-color: var(--accent-color);
        background-color: var(--bg-color);
        transform: translateY(-2px);
    }
    .tech-icon {
        font-size: 1.1em;
        vertical-align: middle;
    }
    .tech-name {
        font-size: 0.9rem;
        color: var(--text-color);
        font-weight: 500;
    }
    
    /* Card Sub-elements */
    .edu-degree, .exp-role, .resp-role {
        font-size: 1.3em;
        font-weight: 600;
        color: var(--accent-color);
        margin-bottom: 4px;
    }
    
    .edu-institute, .exp-org, .resp-org {
        font-size: 1.1em;
        font-weight: 500;
        color: var(--text-color);
        margin-bottom: 6px;
    }
    
    .edu-details, .exp-details, .resp-details {
        font-size: 0.9em;
        color: var(--text-secondary);
        margin-bottom: 8px;
    }
    
    .edu-score {
        font-size: 1em;
        font-weight: 600;
        color: var(--accent-color);
    }
    
    .exp-desc {
        font-size: 1em;
        line-height: 1.6;
        color: var(--text-secondary);
    }
    
    /* Projects Section styling */
    .projects-title {
        display: block;
        width: 100%;
        margin-top: 30px;
    }
    /* Streamlit expander override to fit B&W system */
    .data-testid[data-testid="stExpander"] {
        border-color: var(--card-border) !important;
        background-color: var(--card-bg) !important;
        border-radius: 12px !important;
        margin-bottom: 12px !important;
    }
    
    /* Certifications Styling */
    .certifications-section {
        padding: 40px 0;
    }
    .certifications-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 20px;
    }
    .cert-card {
        background-color: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 14px;
        padding: 1.5rem;
        transition: transform 0.2s, border-color 0.2s;
        text-decoration: none !important;
        color: inherit !important;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .cert-card:hover {
        transform: translateY(-3px);
        border-color: var(--accent-color);
    }
    .cert-title {
        font-size: 1.1em;
        font-weight: 600;
        color: var(--accent-color);
        margin-bottom: 6px;
    }
    .cert-issuer {
        font-size: 0.95em;
        color: var(--text-color);
        margin-bottom: 4px;
    }
    .cert-date {
        font-size: 0.85em;
        color: var(--text-secondary);
    }
    
    /* Contact Section Styling */
    .contact-form {
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 100%;
        margin-top: 20px;
    }
    
    .contact-form label {
        font-size: 0.9em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--text-color);
    }
    
    .contact-form input, .contact-form textarea {
        background-color: var(--input-bg) !important;
        border: 1px solid var(--input-border) !important;
        color: var(--text-color) !important;
        padding: 12px !important;
        border-radius: 8px !important;
        font-size: 1em !important;
        width: 100% !important;
        box-sizing: border-box !important;
        transition: border-color 0.3s ease;
    }
    
    .contact-form input:focus, .contact-form textarea:focus {
        border-color: var(--accent-color) !important;
        outline: none !important;
    }
    
    .contact-form button {
        background-color: var(--btn-bg) !important;
        color: var(--btn-text) !important;
        border: 1px solid var(--btn-bg) !important;
        padding: 14px !important;
        border-radius: 8px !important;
        font-size: 1em !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        margin-top: 10px !important;
    }
    
    .contact-form button:hover {
        background-color: var(--btn-hover-bg) !important;
        color: var(--btn-text) !important;
        border-color: var(--btn-hover-bg) !important;
    }
    
    .contact-success {
        margin-top: 15px;
        font-size: 1em;
        font-weight: 600;
        color: var(--accent-text);
        text-align: center;
    }
    
    /* Responsive Media Queries (Mobile First) */
    @media (max-width: 1024px) {
        .block-container {
            padding-left: 24px !important;
            padding-right: 24px !important;
        }
    }
    
    @media (max-width: 768px) {
        .menu-toggle-btn {
            display: block !important;
        }
        
        .navbar-header-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 70px !important;
            background: var(--navbar-bg) !important;
            border-bottom: 1px solid var(--navbar-border);
            z-index: 999;
            display: flex;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: flex-start !important;
            padding: 0 !important;
        }
        
        .navbar-header-content {
            padding-left: 24px !important;
            margin-bottom: 0 !important;
            height: 70px !important;
            display: flex;
            align-items: center;
        }
        
        .navbar {
            display: none !important;
            flex-direction: column !important;
            position: fixed !important;
            top: 70px !important;
            left: 0 !important;
            width: 100% !important;
            height: auto !important;
            background: var(--navbar-bg) !important;
            border-bottom: 1px solid var(--navbar-border) !important;
            padding: 20px 0 !important;
            gap: 12px !important;
            z-index: 1000 !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            align-items: center !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        
        .navbar.active {
            display: flex !important;
        }
        
        .block-container {
            padding-top: 110px !important;
            padding-left: 16px !important;
            padding-right: 16px !important;
        }
        
        .hero-section {
            flex-direction: column !important;
            text-align: center !important;
            gap: 30px !important;
            padding: 20px 0 !important;
        }
        
        .hero-content {
            flex-direction: column !important;
        }
        
        .hero-pic-container {
            order: -1; /* Move profile picture on top of text */
            margin-bottom: 10px !important;
        }
        
        .hero-about {
            padding-right: 0 !important;
        }
        
        .hero-name {
            font-size: 2em !important;
        }
        
        .about-title, .edu-title, .exp-title, .resp-title, .projects-title, .certifications-title, .contact-title {
            font-size: 1.8em !important;
            text-align: center !important;
            display: block !important;
            margin: 0 auto 20px auto !important;
            width: fit-content !important;
        }
        .about-title:after, .edu-title:after, .exp-title:after, .resp-title:after, .projects-title:after, .certifications-title:after, .contact-title:after {
            left: 50% !important;
            transform: translateX(-50%) !important;
        }
        
        .edu-card, .exp-card, .resp-card, .about-section-box, .contact-section-box {
            padding: 1.5rem !important;
        }
        
        .tech-stack-grid {
            grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
        }
        
        .certifications-grid {
            grid-template-columns: 1fr !important;
        }
        
        /* Larger click/touch targets for mobile */
        .nav-link {
            width: 100% !important;
            text-align: center !important;
            font-size: 1em !important;
            padding: 12px 0 !important; /* Ensure min height target */
        }
        
        .theme-toggle-btn {
            padding: 8px 16px !important;
            margin-left: 0 !important;
            margin-top: 10px !important;
            width: 80% !important;
            max-width: 200px !important;
        }
    }
    
    @media (max-width: 480px) {
        .hero-name {
            font-size: 1.7em !important;
        }
        
        .about-title, .edu-title, .exp-title, .resp-title, .projects-title, .certifications-title, .contact-title {
            font-size: 1.5em !important;
        }
        
        .edu-card, .exp-card, .resp-card, .about-section-box, .contact-section-box {
            padding: 1.25rem !important;
        }
        
        .navbar-name {
            font-size: 1.4em !important;
        }
        
        .hero-pic {
            width: 180px !important;
            height: 180px !important;
        }
    </style>
    <script>
    (function() {
        const currentTheme = localStorage.getItem('theme') || 'dark';
        if (currentTheme === 'light') {
            document.body.classList.add('light-theme');
        } else {
            document.body.classList.remove('light-theme');
        }
    })();
    </script>
    """, unsafe_allow_html=True)