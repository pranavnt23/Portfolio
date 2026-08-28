import streamlit as st

def render_skills():
    st.markdown("""
    <div id="skills" class="about-section-box">
        <div class="about-title">🛠 Tech Stack</div>
        <div class="tech-category">
            <div class="category-title">Languages</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-cpp"><div class="tech-icon">💻</div><div class="tech-name">C++</div></div>
                <div class="tech-box tech-python"><div class="tech-icon">🐍</div><div class="tech-name">Python</div></div>
                <div class="tech-box tech-r"><div class="tech-icon">📊</div><div class="tech-name">R</div></div>
                <div class="tech-box tech-java"><div class="tech-icon">☕</div><div class="tech-name">Java</div></div>
            </div>
        </div>
        <div class="tech-category">
            <div class="category-title">Frameworks</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-node"><div class="tech-icon">🌲</div><div class="tech-name">Node.js</div></div>
                <div class="tech-box tech-react"><div class="tech-icon">⚛️</div><div class="tech-name">React</div></div>
                <div class="tech-box tech-express"><div class="tech-icon">🚂</div><div class="tech-name">Express.js</div></div>
                <div class="tech-box tech-fastapi"><div class="tech-icon">⚡</div><div class="tech-name">FastAPI</div></div>
                <div class="tech-box tech-flutter"><div class="tech-icon">📱</div><div class="tech-name">Flutter</div></div>
            </div>
        </div>
        <div class="tech-category">
            <div class="category-title">Tools</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-vscode"><div class="tech-icon">📝</div><div class="tech-name">VS Code</div></div>
                <div class="tech-box tech-github"><div class="tech-icon">🐙</div><div class="tech-name">GitHub</div></div>
                <div class="tech-box tech-postman"><div class="tech-icon">📬</div><div class="tech-name">Postman</div></div>
                <div class="tech-box tech-streamlit"><div class="tech-icon">🎈</div><div class="tech-name">Streamlit</div></div>
                <div class="tech-box tech-docker"><div class="tech-icon">🐳</div><div class="tech-name">Docker</div></div>
                <div class="tech-box tech-aws"><div class="tech-icon">☁️</div><div class="tech-name">AWS</div></div>
            </div>
        </div>
        <div class="tech-category">
            <div class="category-title">Database</div>
            <div class="tech-stack-grid">
                <div class="tech-box tech-mongodb"><div class="tech-icon">🍃</div><div class="tech-name">MongoDB</div></div>
                <div class="tech-box tech-sql"><div class="tech-icon">🗄️</div><div class="tech-name">SQL</div></div>
                <div class="tech-box tech-postgresql"><div class="tech-icon">🐘</div><div class="tech-name">PostgreSQL</div></div>
                <div class="tech-box tech-dynamodb"><div class="tech-icon">🔷</div><div class="tech-name">DynamoDB</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)