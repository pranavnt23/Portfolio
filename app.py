import streamlit as st
from sections.style import inject_css
from sections.navbar import render_navbar
from sections.hero import render_hero
from sections.about import render_about
from sections.skills import render_skills
from sections.projects import render_projects
from sections.certifications import render_certifications
from sections.contact import render_contact
from sections.education import render_education
from sections.responsibilities import render_responsibilities
from sections.experience import render_experience

st.set_page_config(page_title="Pranav's Portfolio", page_icon="💡", layout="wide")  # FIRST!

inject_css()  # Now inject CSS

def main():
    render_navbar()
    render_hero("assets/pic.jpg")
    render_about()
    render_skills()
    render_education()
    render_experience()
    render_responsibilities()
    render_projects() 
    render_certifications()
    render_contact()
    # ...other sections...



if __name__ == "__main__":
    main()