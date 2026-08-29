import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@500;700&display=swap');
    
    /* Theme variables - iOS Glassmorphic Aesthetic */
    :root {
        --bg-gradient: radial-gradient(circle at 10% 20%, #16122c 0%, #070709 50%), radial-gradient(circle at 90% 80%, #0d1e36 0%, #070709 50%);
        --text-color: #e5e5e7;
        --text-secondary: #9ca3af;
        --card-bg: rgba(24, 24, 28, 0.45);
        --card-border: rgba(255, 255, 255, 0.08);
        --navbar-bg: rgba(15, 15, 17, 0.5);
        --navbar-bg-mobile: rgba(15, 15, 17, 0.98);
        --navbar-border: rgba(255, 255, 255, 0.08);
        --accent-color: #f1f5f9;
        --accent-hover: #ffffff;
        --accent-text: #6366f1;
        --input-bg: rgba(18, 18, 20, 0.6);
        --input-border: rgba(255, 255, 255, 0.08);
        --btn-bg: #e5e5e7;
        --btn-text: #0f0f11;
        --btn-hover-bg: #ffffff;
    }
    
    body.light-theme {
        --bg-gradient: radial-gradient(circle at 10% 20%, #f4f3ff 0%, #f9f9fb 50%), radial-gradient(circle at 90% 80%, #ebf5ff 0%, #f9f9fb 50%);
        --text-color: #1c1c1e;
        --text-secondary: #6b7280;
        --card-bg: rgba(255, 255, 255, 0.45);
        --card-border: rgba(0, 0, 0, 0.06);
        --navbar-bg: rgba(255, 255, 255, 0.5);
        --navbar-bg-mobile: rgba(255, 255, 255, 0.98);
        --navbar-border: rgba(0, 0, 0, 0.06);
        --accent-color: #1c1c1e;
        --accent-hover: #000000;
        --accent-text: #4f46e5;
        --input-bg: rgba(255, 255, 255, 0.6);
        --input-border: rgba(0, 0, 0, 0.06);
        --btn-bg: #1c1c1e;
        --btn-text: #ffffff;
        --btn-hover-bg: #000000;
    }
    
    /* Global Base */
    html {
        scroll-behavior: smooth !important;
    }
    
    html, body {
        height: 100%;
        min-height: 100vh;
        background-image: var(--bg-gradient) !important;
        background-attachment: fixed !important;
        background-size: cover !important;
        color: var(--text-color) !important;
        font-family: 'Inter', -apple-system, sans-serif !important;
        transition: background-image 0.3s ease, color 0.3s ease;
    }
    
    /* Streamlit transparency overhaul for watery look */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stHeader"], .main, .block-container {
        background-color: transparent !important;
        background-image: none !important;
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
    /* Floating Capsule Navbar */
    .navbar-capsule {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 95% !important;
        max-width: 1200px;
        height: 60px;
        background: var(--navbar-bg) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid var(--navbar-border) !important;
        border-radius: 30px !important;
        z-index: 9999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-sizing: border-box;
    }
    
    .navbar-logo-name {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-right: 40px !important;
        flex-shrink: 0 !important;
    }
    
    /* Elevate stacking context of navbar capsule wrapper */
    div[data-testid="element-container"]:has(.navbar-capsule),
    div[data-testid="stVerticalBlock"] > div:has(.navbar-capsule) {
        z-index: 99999 !important;
        position: relative !important;
        overflow: visible !important;
    }
    
    .navbar-profile-image {
        width: 42px !important;
        height: 42px !important;
        margin-right: 12px !important;
        vertical-align: middle !important;
        border-radius: 50% !important;
        object-fit: cover !important;
        background: #ffffff !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 0 0 1px var(--navbar-border), 0 2px 8px rgba(0, 0, 0, 0.08) !important;
        display: inline-block !important;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.15s ease, visibility 0.15s ease;
    }
    
    .navbar-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.4em;
        font-weight: 700;
        color: var(--accent-color);
        letter-spacing: 0.5px;
        user-select: none;
    }
    
    /* Navbar Navigation Links */
    .navbar-links-container {
        display: flex;
        align-items: center;
        gap: 8px !important;
        flex-shrink: 1 !important;
        margin-left: auto !important;
    }
    
    .nav-link {
        display: inline-block;
        background: none;
        color: var(--text-secondary) !important;
        border: none;
        border-radius: 0;
        font-weight: 500;
        font-size: 0.8em !important;
        font-family: 'Inter', sans-serif !important;
        white-space: nowrap !important;
        text-decoration: none !important;
        box-shadow: none;
        margin: 0;
        padding: 4px 6px !important;
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
        font-size: 1.05em !important;
        margin-right: 4px !important;
        vertical-align: middle;
        display: inline-block;
    }
    
    /* Theme Toggle Button */
    .theme-toggle-btn {
        background: var(--navbar-bg) !important;
        border: 1px solid var(--navbar-border) !important;
        color: var(--text-color) !important;
        font-size: 0.95em !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 34px !important;
        height: 34px !important;
        border-radius: 50% !important;
        transition: transform 0.2s, background-color 0.2s !important;
        margin-left: 12px !important;
        outline: none !important;
        box-sizing: border-box !important;
        padding: 0 !important;
        flex-shrink: 0 !important;
    }
    .theme-toggle-btn:hover {
        transform: scale(1.1) !important;
        background-color: var(--card-border) !important;
        border-color: var(--accent-color) !important;
    }
    
    /* Mobile Hamburger Menu Icon (3 lines) */
    .menu-toggle-btn {
        display: none;
        background: none !important;
        border: none !important;
        color: var(--text-color) !important;
        font-size: 1.6em !important;
        cursor: pointer !important;
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
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 40px 0;
        width: 100%;
        box-sizing: border-box;
        position: relative;
    }
    
    .hero-profile-image {
        width: 260px !important;
        height: 260px !important;
        border-radius: 24px !important;
        object-fit: cover !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25) !important;
        border: 4px solid var(--card-bg) !important;
        display: block !important;
        margin: 0 auto 30px auto !important;
        opacity: 1;
        visibility: visible;
        transition: opacity 0.2s ease, visibility 0.2s ease;
    }
    
    .hero-profile-image:hover {
        transform: scale(1.03);
    }
    
    .hero-about {
        max-width: 750px;
        font-size: 1.1em;
        line-height: 1.7;
        color: var(--text-color);
        position: relative;
        z-index: 2;
        text-shadow: 0 1px 5px rgba(0, 0, 0, 0.25);
        margin-top: 15px; /* Clean spacing below profile picture */
    }
    
    .hero-about-title {
        display: block;
        font-family: 'Playfair Display', serif;
        font-size: 1.3em;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: var(--accent-color);
        margin-bottom: 16px;
    }
    
    .hero-name {
        color: var(--accent-color);
        font-weight: 800;
        font-size: 3em;
        line-height: 1.2;
        margin-bottom: 20px;
        font-family: 'Playfair Display', serif;
    }
    
    .hero-bio {
        font-size: 1.05em;
        color: var(--text-secondary);
        margin: 0;
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
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
    }
    
    .edu-card:hover, .exp-card:hover, .resp-card:hover, .about-section-box:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1) !important;
        border-color: var(--accent-color) !important;
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
        background-color: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        transition: all 0.3s ease !important;
        justify-content: flex-start !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
    }
    .tech-box:hover {
        border-color: var(--accent-color) !important;
        background-color: var(--card-bg) !important;
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
    }
    .tech-icon {
        font-size: 1.1em;
        vertical-align: middle;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .tech-logo-img {
        width: 22px !important;
        height: 22px !important;
        object-fit: contain !important;
        vertical-align: middle !important;
        display: inline-block !important;
    }
    /* Invert Next.js logo in dark theme */
    .tech-logo-img.nextjs-logo {
        filter: invert(1) brightness(1.5) !important;
    }
    .light-theme .tech-logo-img.nextjs-logo {
        filter: none !important;
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
    div[data-testid="stExpander"] {
        border: 1px solid var(--card-border) !important;
        background-color: var(--card-bg) !important;
        border-radius: 12px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
    }
    
    div[data-testid="stExpander"] details {
        border: none !important;
        background-color: transparent !important;
    }
    
    div[data-testid="stExpander"] summary {
        background-color: transparent !important;
        color: var(--text-color) !important;
        border-radius: 12px !important;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    
    /* Ensure summary text elements are styled correctly */
    div[data-testid="stExpander"] summary span,
    div[data-testid="stExpander"] summary p,
    div[data-testid="stExpander"] summary label,
    div[data-testid="stExpander"] summary div {
        color: var(--text-color) !important;
    }
    
    /* Ensure toggle arrow chevron matches text color */
    div[data-testid="stExpander"] summary svg {
        color: var(--text-color) !important;
        fill: var(--text-color) !important;
    }
    
    /* Styling when expanded or hovered to prevent dark background in bright mode */
    div[data-testid="stExpander"] summary:hover,
    div[data-testid="stExpander"] summary:focus,
    div[data-testid="stExpander"] details[open] > summary {
        background-color: transparent !important;
        color: var(--text-color) !important;
    }

    div[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        background-color: transparent !important;
        color: var(--text-color) !important;
        border-radius: 0 0 12px 12px !important;
        border-top: 1px solid var(--card-border) !important;
        padding: 1.5rem !important;
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
        background-color: var(--card-bg) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 14px !important;
        padding: 1.5rem !important;
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease !important;
        text-decoration: none !important;
        color: inherit !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05) !important;
    }
    .cert-card:hover {
        transform: translateY(-3px) scale(1.02) !important;
        border-color: var(--accent-color) !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1) !important;
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
    @media (max-width: 1200px) {
        .block-container {
            padding-left: 24px !important;
            padding-right: 24px !important;
        }
        
        .menu-toggle-btn {
            display: block !important;
        }
        
        .navbar-capsule {
            width: 95% !important;
            height: 55px !important;
            top: 10px !important;
            padding: 0 16px !important;
            border-radius: 20px !important;
        }
        
        .navbar-links-container {
            display: none !important;
            flex-direction: column !important;
            position: absolute !important;
            top: 65px !important;
            left: 0 !important;
            width: 100% !important;
            height: auto !important;
            background: var(--navbar-bg-mobile) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid var(--navbar-border) !important;
            border-radius: 20px !important;
            padding: 20px 0 !important;
            gap: 10px !important;
            z-index: 9999 !important;
            align-items: center !important;
            box-shadow: 0 10px 35px rgba(0,0,0,0.2) !important;
            box-sizing: border-box !important;
        }
        
        .navbar-links-container.active {
            display: flex !important;
        }
        
        .nav-link:after {
            display: none !important;
        }
        
        .block-container {
            padding-top: 100px !important;
            padding-left: 16px !important;
            padding-right: 16px !important;
        }
        
        .hero-section {
            padding: 30px 0 20px 0 !important;
            gap: 20px !important;
        }
        
        .hero-profile-image {
            width: 180px !important;
            height: 180px !important;
            border-radius: 24px !important;
            margin-bottom: 20px !important;
        }
        
        .hero-about {
            margin-top: -5vh !important;
        }
        
        .hero-name {
            font-size: 2.2em !important;
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
            padding: 10px 0 !important;
        }
        
        .theme-toggle-btn {
            margin-left: auto !important;
            margin-right: 12px !important;
            margin-top: 0 !important;
            width: 34px !important;
            height: 34px !important;
            border-radius: 50% !important;
            padding: 0 !important;
        }
    }
    
    @media (max-width: 480px) {
        .hero-name {
            font-size: 1.8em !important;
        }
        
        .about-title, .edu-title, .exp-title, .resp-title, .projects-title, .certifications-title, .contact-title {
            font-size: 1.5em !important;
        }
        
        .edu-card, .exp-card, .resp-card, .about-section-box, .contact-section-box {
            padding: 1.25rem !important;
        }
        
        .navbar-name {
            font-size: 1.2em !important;
        }
        
        .hero-profile-image {
            width: 140px !important;
            height: 140px !important;
            margin-bottom: 15px !important;
        }
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