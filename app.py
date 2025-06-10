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
        @import url('https://fonts.googleapis.com/css2?family=Lora:wght@500&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Poppins:wght@700;900&family=Oswald:wght@700&family=Playfair+Display:wght@700&display=swap');
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
            background: linear-gradient(120deg, #da6bf5 0%, #e9b9f5 100%);
            min-height: 100vh;
            color: #fff !important;
        }
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
            border-radius: 50%;        /* Makes the logo circular */
            background: #fff;          /* Optional: white bg for contrast */
            box-shadow: 0 2px 8px #0002; /* Optional: subtle shadow */
            object-fit: cover;         /* Ensures image fills the circle */
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
            font-size: 1.3em; /* Increased font size */
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
        /* Increase top padding for main content so it's not hidden under navbar */
        .block-container {
            padding-top: 120px !important;
        }
        /* Hero section */
        .hero-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2px;
            margin-top: 110px;  /* Increased top margin to push below navbar */
            margin-bottom: 32px;
            min-height: 32px;
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
    border-radius: 80px; /* More rounded corners */
    border: 6px solid;
    border-image: linear-gradient(135deg, #00e6ff, #c471f5, #fbc2eb) 1;
    box-shadow: 0 8px 32px #8f5fd1aa;
    position: relative;
    z-index: 1;
    animation: hero-img-fade 1.2s cubic-bezier(.68,-0.55,.27,1.55) 1s forwards;
    opacity: 0;
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
            font-family: 'Playfair Display', 'Montserrat', 'Poppins', 'Oswald', Arial, sans-serif !important;
            font-weight: 700;
            font-size: 3.5em;
            letter-spacing: 2px;
            color: #fff;
            margin-bottom: 0.15em;
            text-shadow: 0 4px 24px #c471f5cc, 0 2px 8px #fff4;
            animation: fade-in-up 1s ease-out 1.2s forwards;
            opacity: 0;
        }
        .hero-title span {
            font-family: 'Poppins', 'Montserrat', 'Oswald', Arial, sans-serif !important;
            font-size: 1.4em;
            color: #00e6ff;
            letter-spacing: 2px;
            text-shadow: 2px 2px 12px #00e6ff55;
        }
        .hero-subtitle {
            font-family: 'Poppins', 'Montserrat', 'Oswald', Arial, sans-serif !important;
            font-weight: 700;
            font-size: 2em;
            color: #fbc2eb;
            margin-bottom: 0.3em;
            letter-spacing: 2px;
            text-shadow: 1px 1px 8px #c471f5aa;
            animation: fade-in-up 1s ease-out 1.4s forwards;
            opacity: 0;
        }
        .hero-about {
            position: relative;
            font-size: 1.48em;
            color: #fff;
            background: rgba(20, 18, 38, 0.3); /* opacity set to 0.3 */
            border-radius: 18px;
            padding: 48px 22px 18px 22px; /* increased top padding for space */
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

.hero-about-title::after {
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

.hero-about-title:hover,
.hero-about-title:focus {
    color: #00e6ff;
}

.hero-about-title:hover::after,
.hero-about-title:focus::after {
    width: 100%;
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
            .hero-img-container, .hero-img_bg {
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
        .about-section-box {
    background: rgba(20, 18, 38, 0.3);
    border-radius: 8px;
    box-shadow: 0 4px 24px #c471f555, 0 1.5px 8px #fff4;
    padding: 32px 36px 28px 36px;
    margin: 0 auto 36px auto;
    max-width: 70vw;    /* Cover 70% of the viewport width */
    width: 70vw;        /* Ensure it stretches to 70% */
    color: #fff;
    font-family: 'Poppins', 'Montserrat', Arial, sans-serif;
    font-size: 1.18em;
    font-weight: 30;
    line-height: 1.7;
    position: relative;
    top: 0;
    z-index: 2;
    border: 2.5px solid #c471f5;
    transition: box-shadow 0.3s;
    opacity: 0;
    animation: fade-in-up 1s ease-out 2s forwards;
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
    color: #93daf7 ;
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
html {
    scroll-behavior: smooth;
}
    </style>
""", unsafe_allow_html=True)

# Add the header background and name+logo to the top left
st.markdown("""
<div class="navbar-header-bg">
    <div class="navbar-header-content">
        <img class="navbar-logo" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo">
    </div>
</div>
""", unsafe_allow_html=True)

# Navbar (remains as is, will appear to the right)
st.markdown("""
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

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = "assets/pic.jpg"  # Update the path if your image is elsewhere
img_base64 = get_base64_of_bin_file(img_path)

# Hero Section (about left, image right, both inside hero-section for CSS)
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-about">
            <span class="hero-about-title">Myself</span><br>
            Hi! I’m <b>Pranav</b>, a passionate and curious developer with a strong foundation in software engineering and a love for building impactful digital solutions.<br>
            I'm currently pursuing <b>M.Sc Software Systems (Integrated)</b> at <b>Coimbatore Institute of Technology</b>, where I’m honing both my technical and problem-solving skills.
            <br><br>
        </div>
    </div>
    <div class="hero-img-container">
        <img src="assets/pic.jpg" alt="Profile Photo" class="hero-img">
    </div>
</div>
""", unsafe_allow_html=True)

# About Me Section (styled box below hero section)
st.markdown("""
<div id="about" class="about-section-box">
    <div class="about-title">
        🧑‍💻 About Me
    </div>
    <div class="about-content">
        Streamlined software developer with strong coding and application development skills, efficient in problem-solving and eager to explore new opportunities in the software industry.
        <br><br><span class="about-interests-title">🔍 I’m particularly interested in:</span>
        <ul class="about-interests-list">
    <li>
        <span class="interest-icon">🌐</span>
        <span class="interest-title">Full-Stack</span>
    </li>
    <li>
        <span class="interest-icon">🤖</span>
        <span class="interest-title">AI/ML</span>
    </li>
    <li>
        <span class="interest-icon">💻</span>
        <span class="interest-title">Open Source</span>
    </li>
    <li>
        <span class="interest-icon">☁️</span>
        <span class="interest-title">Cloud</span>
    </li>
</ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Skills Section (add this below your About section)
st.markdown("""
<div id="skills" class="about-section-box">
    <div class="about-title">
        🛠 Tech Stack
    </div>
    <div class="about-content">
        <b>Languages:</b> Python, JavaScript, Dart<br>
        <b>Frameworks:</b> Flutter, FastAPI, React<br>
        <b>Tools:</b> Git, Docker, Firebase, AWS<br>
        <b>Database:</b> DynamoDB, PostgreSQL
    </div>
</div>
""", unsafe_allow_html=True)

# Inject JavaScript for animated smooth scrolling
st.markdown("""
<script>
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.nav-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href.startsWith("#")) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    window.scrollTo({
                        top: target.getBoundingClientRect().top + window.pageYOffset - 30, // adjust offset if needed
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});
</script>
""", unsafe_allow_html=True)