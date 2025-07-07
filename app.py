import streamlit as st
from sections.style import inject_css
from sections.navbar import render_navbar
from sections.hero import render_hero
from sections.about import render_about
from sections.skills import render_skills
from sections.projects import render_projects
from sections.certifications import render_certifications
from sections.contact import render_contact

st.set_page_config(page_title="Pranav's Portfolio", page_icon="💡", layout="wide")  # FIRST!

inject_css()  # Now inject CSS

def main():
    render_navbar()
    render_hero("assets/pic.jpg")
    render_about()
    render_skills()
    render_projects() 
    render_certifications()
    render_contact()
    # ...other sections...

    # Optional: Smooth scroll JS
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
                            top: target.getBoundingClientRect().top + window.pageYOffset - 30,
                            behavior: 'smooth'
                        });
                    }
                }
            });
        });
    });
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()