import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:wght@500&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Poppins:wght@700;900&family=Oswald:wght@700&family=Playfair+Display:wght@700&display=swap');
    html, body, .stApp {
        height: 100%;
        min-height: 100vh;
        background: linear-gradient(120deg, #da6bf5 0%, #e9b9f5 100%) !important;
        color: #fff !important;
    }
    #MainMenu, header, footer {visibility: hidden; height: 0;}
    .block-container {padding-top: 120px !important;}
    .navbar-header-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 80px;
        background: linear-gradient(120deg, #8f5fd1cc 0%, #c471f5cc 100%);
        opacity: 0.7;
        z-index: 999;
        box-shadow: 0 2px 12px #8f5fd1aa;
        display: flex;
        align-items: center;
    }
    .navbar-header-content {
        display: flex;
        align-items: center;
        height: 80px;
        max-width: 100vw;
        padding-left: 32px;
        z-index: 1001;
        position: relative;
    }
    .navbar-logo {
        width: 44px;
        height: 44px;
        margin-right: 14px;
        vertical-align: middle;
        border-radius: 50%;
        background: #fff;
        box-shadow: 0 2px 8px #0002;
        object-fit: cover;
    }
    .navbar-name {
        font-family: 'Playfair Display', 'Montserrat', 'Poppins', Arial, sans-serif;
        font-size: 2.5em;
        font-weight: 500;
        color: #fff;
        letter-spacing: 2px;
        margin-right: 36px;
        text-shadow: 0 2px 12px #c471f555;
        user-select: none;
    }
    .navbar {
        display: flex;
        justify-content: flex-end;
        flex-wrap: wrap;
        gap: 36px;
        margin-bottom: 30px;
        margin-top: 0px;
        padding-right: 2vw;
        padding-top: 27px;
        padding-bottom: 18px;
        opacity: 0;
        transform: translateY(-20px);
        animation: navbar-fade-in 1s ease-out 0.3s forwards;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background: none;
        box-shadow: none;
        height: 80px;
    }
    @keyframes navbar-fade-in {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    .nav-link {
        display: inline-block;
        background: none;
        color: #fff !important;
        border: none;
        border-radius: 0;
        font-weight: 700;
        font-size: 1.3em;
        font-family: 'Lora', 'Montserrat', 'Poppins', Arial, sans-serif !important;
        text-decoration: none !important;
        box-shadow: none;
        margin: 0;
        padding: 0 8px 4px 4px;
        position: relative;
        transition: color 0.2s;
        opacity: 0;
        transform: translateY(8px);
        animation: navlink-pop 0.5s cubic-bezier(.68,-0.55,.27,1.55) forwards;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    .nav-link:after {
        content: "";
        display: block;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        border-radius: 2px;
        transition: width 0.35s cubic-bezier(.77,0,.18,1);
        position: absolute;
        left: 0;
        bottom: 0;
    }
    .nav-link:hover, .nav-link:focus {
        color: #00e6ff !important;
    }
    .nav-link:hover:after, .nav-link:focus:after {
        width: 100%;
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
            transform: translateY(0);
        }
    }
    .nav-icon {
        width: 18px;
        height: 18px;
        margin-right: 7px;
        vertical-align: middle;
        filter: drop-shadow(0 1px 2px #0003);
    }

    /* Hero section */
    .hero-section {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2px;
        margin-top: 110px;
        margin-bottom: 32px;
        min-height: 32px;
        position: relative;
        z-index: 1;
    }
    .hero-content {
        flex: 2;
        min-width: 300px;
        max-width: 700px;
    }
    .hero-img-container {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        min-width: 220px;
    }
    .hero-img {
        width: 260px;
        height: 260px;
        object-fit: cover;
        border-radius: 50%;
        border: 6px solid #fff;
        box-shadow: 0 8px 32px #8f5fd1aa, 0 2px 16px #fbc2eb99;
        background: #fff;
        z-index: 2;
        filter: brightness(1.05) contrast(1.05);
        transition: transform 0.3s;
        animation: hero-img-fade 1.2s cubic-bezier(.68,-0.55,.27,1.55) 1s forwards;
        opacity: 0;
    }
    @keyframes hero-img-fade {
        to { opacity: 1; }
    }

    /* Hero about box */
    .hero-about {
        position: relative;
        font-size: 1.48em;
        color: #fff;
        background: rgba(20, 18, 38, 0.3);
        border-radius: 18px;
        padding: 48px 22px 18px 22px;
        box-shadow: 0 2px 12px #c471f555;
        font-weight: 500;
        line-height: 1.5;
        max-width: 820px;
        min-width: 260px;
        width: 100%;
        margin-right: 12px;
        animation: fade-in-up 1s ease-out 1.6s forwards;
        opacity: 0;
        white-space: normal;
        overflow-wrap: break-word;
    }
    .hero-about-title {
        position: absolute;
        top: 16px;
        right: 32px;
        font-size: 1.2em;
        font-weight: 700;
        color: #fff;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        letter-spacing: 1px;
        cursor: pointer;
        transition: color 0.2s;
        z-index: 2;
        background: transparent;
        padding: 0 8px;
        line-height: 1.2;
    }

    /* About section box */
    .about-section-box {
        background: rgba(20, 18, 38, 0.82);
        border-radius: 24px;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
        padding: 32px 36px 28px 36px;
        margin: 0 auto 36px auto;
        max-width: 70vw;
        width: 70vw;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        font-size: 1.18em;
        font-weight: 500;
        line-height: 1.7;
        position: relative;
        top: 0;
        z-index: 2;
        border: 2.5px solid #c471f5;
        transition: box-shadow 0.3s;
        opacity: 0;
        animation: fade-in-up 1s ease-out 2s forwards;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .about-title {
        font-size: 1.5em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 12px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        position: relative;
        transition: color 0.2s;
    }
    .about-title::after {
        content: "";
        display: block;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        border-radius: 2px;
        transition: width 0.35s cubic-bezier(.77,0,.18,1);
        position: absolute;
        left: 0;
        bottom: -4px;
    }
    .about-section-box:hover .about-title::after,
    .about-section-box:focus-within .about-title::after {
        width: 100%;
    }

    .about-interests-title {
        font-weight: 600;
        color: #00bcd4;
        font-size: 1.08em;
    }
    .about-interests-list {
        margin: 18px 0 0 0;
        padding-left: 0;
        color: #fff;
        font-size: 1.18em;
        font-family: inherit;
        list-style: none;
        display: flex;
        flex-wrap: wrap;
        gap: 18px;
        justify-content: center;
    }
    .about-interests-list li {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        min-width: 160px;
        min-height: 110px;
        background: linear-gradient(135deg, #c471f5 0%, #00e6ff 100%);
        color: #fff;
        border-radius: 18px;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
        font-weight: 700;
        font-size: 1.13em;
        letter-spacing: 0.5px;
        padding: 22px 18px 18px 18px;
        position: relative;
        overflow: hidden;
        cursor: pointer;
        transition: transform 0.22s cubic-bezier(.68,-0.55,.27,1.55), box-shadow 0.22s;
        animation: pop-in 0.7s cubic-bezier(.68,-0.55,.27,1.55) both;
    }
    .about-interests-list li:hover {
        transform: scale(1.08) rotate(-2deg);
        box-shadow: 0 8px 32px #00e6ff77, 0 2px 12px #fff7;
        background: linear-gradient(135deg, #00e6ff 0%, #c471f5 100%);
    }
    .about-interests-list li::before {
        content: "";
        position: absolute;
        top: -40px;
        right: -40px;
        width: 80px;
        height: 80px;
        background: radial-gradient(circle, #fff3 40%, transparent 70%);
        border-radius: 50%;
        z-index: 0;
        transition: opacity 0.3s;
        opacity: 0.7;
    }
    .about-interests-list li:hover::before {
        opacity: 1;
    }
    .interest-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
        z-index: 1;
        filter: drop-shadow(0 2px 8px #00e6ff66);
        animation: icon-bounce 1.2s infinite alternate;
    }
    .interest-title {
        font-weight: 800;
        color: #fff;
        font-size: 1.13em;
        letter-spacing: 1px;
        z-index: 1;
        text-shadow: 0 2px 8px #c471f555;
        margin-bottom: 0;
    }
    @keyframes pop-in {
        0% { opacity: 0; transform: scale(0.7) translateY(40px);}
        100% { opacity: 1; transform: scale(1) translateY(0);}
    }
    @keyframes icon-bounce {
        0% { transform: translateY(0);}
        100% { transform: translateY(-8px);}
    }
    @keyframes fade-in-up {
        0% { opacity: 0; transform: translateY(40px);}
        100% { opacity: 1; transform: translateY(0);}
    }

    /* Tech stack grid (skills) */
    .tech-category {
        margin-bottom: 2rem;
    }
    .category-title {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
        font-weight: bold;
        color: #ffffff;
        background: linear-gradient(90deg, #007cf0, #00dfd8);
        padding: 0.3rem 1rem;
        border-radius: 12px;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
    }
    .tech-stack-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
        justify-content: center;
    }
    .tech-box {
        background: #1e1e2f;
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        width: 110px;
        height: 110px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 15px #0ff;
        animation: float 4s ease-in-out infinite;
        transition: transform 0.3s, box-shadow 0.3s;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .tech-box:hover {
        transform: scale(1.07) rotate(2deg);
        box-shadow: 0 0 25px #0ff, 0 0 30px #00dfd8;
    }
    .tech-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .tech-name {
        font-weight: 600;
        font-size: 0.95rem;
        color: #ffffff;
    }
    .tech-python { background: radial-gradient(circle, #306998, #4B8BBE); }
    .tech-js { background: radial-gradient(circle, #f0db4f, #323330); color: #000; }
    .tech-dart { background: radial-gradient(circle, #00B4AB, #0175C2); }
    .tech-flutter { background: linear-gradient(135deg, #02569B, #13B9FD); }
    .tech-fastapi { background: linear-gradient(135deg, #059669, #10B981); }
    .tech-react { background: radial-gradient(circle, #61DBFB, #20232a); }
    .tech-docker { background: linear-gradient(135deg, #2496ED, #1D63ED); }
    .tech-git { background: linear-gradient(135deg, #F05032, #8F3F1F); }
    .tech-firebase { background: radial-gradient(circle, #FFA000, #F57C00); }
    .tech-aws { background: linear-gradient(135deg, #FF9900, #232F3E); }
    .tech-dynamodb { background: linear-gradient(135deg, #4053D6, #232F3E); }
    .tech-postgresql { background: linear-gradient(135deg, #336791, #2F5DAB); }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }
    @keyframes glow {
        0% { box-shadow: 0 0 10px #0ff; }
        50% { box-shadow: 0 0 20px #00dfd8, 0 0 30px #007cf0; }
        100% { box-shadow: 0 0 10px #0ff; }
    }

    /* Projects Section */
    .projects-section {
        margin: 0 auto 36px auto;
        max-width: 90vw;
        width: 90vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 2;
    }
    .projects-title {
        font-size: 2em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 18px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        background: linear-gradient(90deg, #8f5fd1 0%, #c471f5 100%);
        padding: 0.3rem 1.2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px #c471f555;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
    }
    .projects-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: center;
        width: 100%;
    }
    .project-card {
        background: linear-gradient(135deg, #8f5fd1 0%, #c471f5 100%);
        border-radius: 18px;
        box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
        padding: 2rem 1.5rem 1.5rem 1.5rem;
        min-width: 290px;
        max-width: 340px;
        flex: 1 1 320px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        transition: transform 0.22s cubic-bezier(.68,-0.55,.27,1.55), box-shadow 0.22s;
        position: relative;
        overflow: hidden;
        margin-bottom: 0.5rem;
    }
    .project-card:hover {
        transform: scale(1.04) translateY(-6px);
        box-shadow: 0 8px 32px #00e6ff77, 0 2px 12px #fff7;
    }
    .project-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
        filter: drop-shadow(0 2px 8px #00e6ff66);
    }
    .project-title {
        font-size: 1.25em;
        font-weight: 700;
        margin-bottom: 0.5em;
        color: #fff;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #c471f555;
    }
    .project-desc {
        font-size: 1.05em;
        font-weight: 400;
        margin-bottom: 0.7em;
        color: #f3eaff;
        line-height: 1.5;
    }
    .project-tech {
        font-size: 0.98em;
        color: #00e6ff;
        font-weight: 600;
        margin-bottom: 0.5em;
    }

    /* Certifications Section */
    .certifications-section {
        margin: 0 auto 36px auto;
        max-width: 90vw;
        width: 90vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 2;
    }
    .certifications-title {
        font-size: 2em;
        font-weight: 700;
        color: #fff;
        margin-bottom: 18px;
        letter-spacing: 1px;
        font-family: 'Montserrat', 'Poppins', Arial, sans-serif;
        text-shadow: 0 2px 12px #c471f555;
        background: linear-gradient(90deg, #00e6ff 0%, #c471f5 100%);
        padding: 0.3rem 1.2rem;
        border-radius: 14px;
        box-shadow: 0 2px 8px #c471f555;
        width: fit-content;
        animation: glow 2s infinite ease-in-out;
    }
    .certifications-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: center;
        width: 100%;
    }
    .cert-card {
        background: linear-gradient(135deg, #00e6ff 0%, #c471f5 100%);
        border-radius: 18px;
        box-shadow: 0 4px 24px #00e6ff55, 0 1.5px 8px #fff4;
        padding: 2rem 1.5rem 1.5rem 1.5rem;
        min-width: 260px;
        max-width: 320px;
        flex: 1 1 280px;
        color: #fff;
        font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        transition: transform 0.22s cubic-bezier(.68,-0.55,.27,1.55), box-shadow 0.22s;
        position: relative;
        overflow: hidden;
        margin-bottom: 0.5rem;
    }
    .cert-card:hover {
        transform: scale(1.04) translateY(-6px);
        box-shadow: 0 8px 32px #8f5fd177, 0 2px 12px #fff7;
    }
    .cert-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
        filter: drop-shadow(0 2px 8px #00e6ff66);
    }
    .cert-title {
        font-size: 1.15em;
        font-weight: 700;
        margin-bottom: 0.5em;
        color: #fff;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #c471f555;
    }
    .cert-org {
        font-size: 1em;
        font-weight: 500;
        color: #e0f7fa;
        margin-bottom: 0.3em;
    }

    @media (max-width: 900px) {
        .about-section-box, .hero-section {
            max-width: 95vw;
            width: 95vw;
        }
        .hero-img {
            width: 180px;
            height: 180px;
        }
        .projects-grid {
            gap: 1.2rem;
        }
        .project-card {
            min-width: 220px;
            max-width: 95vw;
            padding: 1.2rem 1rem 1rem 1rem;
        }
        .certifications-grid {
            gap: 1.2rem;
        }
        .cert-card {
            min-width: 180px;
            max-width: 95vw;
            padding: 1.2rem 1rem 1rem 1rem;
        }
    }
    @media (max-width: 700px) {
        .navbar-header-bg {
            flex-direction: column;
            height: auto;
            padding: 8px 0;
        }
        .navbar-header-content {
            flex-direction: column;
            align-items: flex-start;
            padding-left: 12px;
            gap: 6px;
        }
        .navbar-name {
            font-size: 1.3em !important;
            margin-right: 0;
        }
        .hero-section {
            flex-direction: column;
            align-items: center;
            margin-top: 90px;
        }
        .about-section-box {
            padding: 18px 6vw 18px 6vw;
        }
        .projects-title {
            font-size: 1.2em;
            padding: 0.2rem 0.7rem;
        }
        .projects-grid {
            flex-direction: column;
            align-items: center;
        }
        .project-card {
            width: 95vw;
            min-width: 0;
            max-width: 98vw;
            padding: 1rem 0.7rem 0.7rem 0.7rem;
        }
        .certifications-title {
            font-size: 1.2em;
            padding: 0.2rem 0.7rem;
        }
        .certifications-grid {
            flex-direction: column;
            align-items: center;
        }
        .cert-card {
            width: 95vw;
            min-width: 0;
            max-width: 98vw;
            padding: 1rem 0.7rem 0.7rem 0.7rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)