import streamlit as st
import streamlit.components.v1 as components
import base64
import os

def get_base64_of_bin_file(bin_file):
    try:
        if not os.path.isabs(bin_file):
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            bin_file = os.path.join(project_root, bin_file)
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

def render_navbar():
    img_base64 = get_base64_of_bin_file("assets/pic.jpeg")
    logo_html = f'<img class="navbar-profile-image" src="data:image/jpeg;base64,{img_base64}" alt="Profile Photo">' if img_base64 else ''
    
    # Render navbar HTML structure in parent document with a dynamic logo placeholder
    st.markdown("""
    <div class="navbar-capsule">
        <div class="navbar-logo-name">
            """ + logo_html + """
            <span class="navbar-name">Pranav</span>
        </div>
        <div class="navbar-links-container">
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
        </div>
        <button id="theme-toggle" class="theme-toggle-btn">🌙</button>
        <button id="menu-toggle" class="menu-toggle-btn">☰</button>
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
        if (window.updateImagePosition) window.updateImagePosition();
    }

    function toggleMenu() {
        const navbar = parentDoc.querySelector('.navbar-links-container');
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
                const navbar = parentDoc.querySelector('.navbar-links-container');
                const toggleBtn = parentDoc.getElementById('menu-toggle');
                if (navbar && navbar.classList.contains('active')) {
                    navbar.classList.remove('active');
                    if (toggleBtn) toggleBtn.innerText = '☰';
                }
            }
        }
    });

    // iPhone-style morphing scroll sync using a flying clone
    window.updateImagePosition = function() {
        const heroImg = parentDoc.querySelector('.hero-profile-image');
        const navImg = parentDoc.querySelector('.navbar-profile-image');
        
        // Dynamic flying clone creation
        let clone = parentDoc.getElementById('flying-profile-clone');
        if (!clone && heroImg) {
            clone = parentDoc.createElement('img');
            clone.id = 'flying-profile-clone';
            clone.src = heroImg.src;
            clone.style.display = 'none';
            clone.style.position = 'fixed';
            clone.style.zIndex = '100000';
            clone.style.pointerEvents = 'none';
            clone.style.objectFit = 'cover';
            clone.style.border = '2px solid #ffffff';
            clone.style.boxShadow = '0 0 0 1px var(--navbar-border), 0 4px 15px rgba(0,0,0,0.15)';
            parentDoc.body.appendChild(clone);
        }
        
        if (!heroImg || !navImg || !clone) return;
        
        // Dynamically find scrolled container and calculate scrollTop
        let scrollTop = 0;
        const candidates = [
            parentDoc.querySelector('.main'),
            parentDoc.querySelector('[data-testid="stAppViewContainer"]'),
            parentDoc.querySelector('.block-container'),
            parentDoc.documentElement,
            parentDoc.body,
            parentDoc.defaultView
        ];
        for (const el of candidates) {
            if (el && el.scrollTop > 0) {
                scrollTop = el.scrollTop;
                break;
            }
        }
        if (scrollTop === 0) {
            scrollTop = parentDoc.defaultView.pageYOffset || parentDoc.documentElement.scrollTop || parentDoc.body.scrollTop || 0;
        }
        
        const startScroll = 40;
        const endScroll = 340;
        const scrollRange = endScroll - startScroll;
        
        if (scrollTop <= startScroll) {
            // STATE 1: TOP OF PAGE
            heroImg.style.opacity = '1';
            heroImg.style.visibility = 'visible';
            
            navImg.style.opacity = '0';
            navImg.style.visibility = 'hidden';
            
            clone.style.display = 'none';
        } else if (scrollTop >= endScroll) {
            // STATE 6: FINAL NAVBAR
            heroImg.style.opacity = '0';
            heroImg.style.visibility = 'hidden';
            
            navImg.style.opacity = '1';
            navImg.style.visibility = 'visible';
            
            clone.style.display = 'none';
        } else {
            // STATE 2 TO 5: FLIGHT TRANSITION
            const p = (scrollTop - startScroll) / scrollRange;
            
            const heroRect = heroImg.getBoundingClientRect();
            const navRect = navImg.getBoundingClientRect();
            
            if (heroRect.width === 0 || navRect.width === 0) return;
            
            // Make clone visible
            clone.style.display = 'block';
            
            // Fade out hero image gradually (completely hidden at p=0.45)
            if (p < 0.45) {
                heroImg.style.opacity = (1 - p / 0.45).toString();
                heroImg.style.visibility = 'visible';
            } else {
                heroImg.style.opacity = '0';
                heroImg.style.visibility = 'hidden';
            }
            
            // Navbar image remains hidden until clone arrives, then handoff
            if (p >= 0.85) {
                navImg.style.opacity = ((p - 0.85) / 0.15).toString();
                navImg.style.visibility = 'visible';
                clone.style.opacity = (1 - (p - 0.85) / 0.15).toString();
            } else {
                navImg.style.opacity = '0';
                navImg.style.visibility = 'hidden';
                clone.style.opacity = '1';
            }
            
            // Size interpolation
            const width = heroRect.width + (navRect.width - heroRect.width) * p;
            const height = heroRect.height + (navRect.height - heroRect.height) * p;
            
            // Coordinate vectors
            const startX = heroRect.left;
            const startY = heroRect.top;
            const endX = navRect.left;
            const endY = navRect.top;
            
            let targetX = startX + (endX - startX) * p;
            let targetY = startY + (endY - startY) * p;
            
            // STATE 5: Physical landing hop (p from 0.70 to 0.85)
            let hopOffset = 0;
            if (p >= 0.70 && p <= 0.85) {
                const t_hop = (p - 0.70) / 0.15; // 0 to 1
                if (t_hop < 0.25) {
                    hopOffset = (t_hop / 0.25) * 4; // overshoot down 4px
                } else if (t_hop < 0.6) {
                    const localP = (t_hop - 0.25) / 0.35;
                    hopOffset = 4 - localP * 14; // bounce up 10px
                } else if (t_hop < 0.8) {
                    const localP = (t_hop - 0.6) / 0.2;
                    hopOffset = -10 + localP * 12; // drop down to 2px
                } else {
                    const localP = (t_hop - 0.8) / 0.2;
                    hopOffset = 2 - localP * 2; // settle
                }
            }
            
            targetY += hopOffset;
            
            // Border-radius: morph rectangle (24px) to circle (50%)
            const br = 24 + (50 - 24) * p;
            const brVal = p >= 0.8 ? '50%' : `${br}px`;
            
            // Apply GPU-friendly transform3d
            clone.style.left = '0px';
            clone.style.top = '0px';
            clone.style.width = `${width}px`;
            clone.style.height = `${height}px`;
            clone.style.borderRadius = brVal;
            clone.style.transform = `translate3d(${targetX}px, ${targetY}px, 0)`;
        }
    };

    // Run theme sync on load
    applyTheme();
    
    // Periodically re-enforce the theme class to prevent resets when Streamlit reruns
    if (!window.themeIntervalSet) {
        window.themeIntervalSet = true;
        setInterval(applyTheme, 300);
    }

    // Scroll and resize event bindings attached to all possible scroll containers
    if (!window.scrollListenerSet) {
        window.scrollListenerSet = true;
        
        const scrollEvents = ['scroll', 'touchmove', 'mousewheel'];
        const attachTo = [
            parentDoc.defaultView,
            parentDoc,
            parentDoc.documentElement,
            parentDoc.body,
            parentDoc.querySelector('.main'),
            parentDoc.querySelector('[data-testid="stAppViewContainer"]'),
            parentDoc.querySelector('.block-container'),
            ...parentDoc.querySelectorAll('div, section, main')
        ];
        
        attachTo.forEach(el => {
            if (!el) return;
            scrollEvents.forEach(evt => {
                el.addEventListener(evt, () => {
                    if (!window.scrollTicking) {
                        window.requestAnimationFrame(() => {
                            window.updateImagePosition();
                            window.scrollTicking = false;
                        });
                        window.scrollTicking = true;
                    }
                }, { passive: true });
            });
        });
        
        setTimeout(window.updateImagePosition, 300);
        setInterval(window.updateImagePosition, 800);
    }
    </script>
    """, height=0, width=0)