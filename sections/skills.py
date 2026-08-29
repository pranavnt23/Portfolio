import streamlit as st

def render_skills():
    st.markdown("""
<div id="skills" class="about-section-box">
<div class="about-title">🛠 Tech Stack</div>

<div class="tech-category">
<div class="category-title">Languages</div>
<div class="tech-stack-grid">
<div class="tech-box tech-c"><div class="tech-icon">⚙️</div><div class="tech-name">C</div></div>
<div class="tech-box tech-cpp"><div class="tech-icon">💻</div><div class="tech-name">C++</div></div>
<div class="tech-box tech-python"><div class="tech-icon">🐍</div><div class="tech-name">Python</div></div>
<div class="tech-box tech-js"><div class="tech-icon">🌐</div><div class="tech-name">JavaScript</div></div>
<div class="tech-box tech-ts"><div class="tech-icon">🟦</div><div class="tech-name">TypeScript</div></div>
</div>
</div>

<div class="tech-category">
<div class="category-title">Frontend</div>
<div class="tech-stack-grid">
<div class="tech-box tech-html"><div class="tech-icon">📄</div><div class="tech-name">HTML</div></div>
<div class="tech-box tech-css"><div class="tech-icon">🎨</div><div class="tech-name">CSS</div></div>
<div class="tech-box tech-react"><div class="tech-icon">⚛️</div><div class="tech-name">React</div></div>
<div class="tech-box tech-nextjs"><div class="tech-icon">▲</div><div class="tech-name">Next.js</div></div>
</div>
</div>

<div class="tech-category">
<div class="category-title">Backend</div>
<div class="tech-stack-grid">
<div class="tech-box tech-node"><div class="tech-icon">🌲</div><div class="tech-name">Node.js</div></div>
<div class="tech-box tech-fastapi"><div class="tech-icon">⚡</div><div class="tech-name">FastAPI</div></div>
</div>
</div>

<div class="tech-category">
<div class="category-title">Databases</div>
<div class="tech-stack-grid">
<div class="tech-box tech-postgresql"><div class="tech-icon">🐘</div><div class="tech-name">PostgreSQL</div></div>
<div class="tech-box tech-mysql"><div class="tech-icon">🗄️</div><div class="tech-name">MySQL</div></div>
<div class="tech-box tech-mongodb"><div class="tech-icon">🍃</div><div class="tech-name">MongoDB</div></div>
</div>
</div>

<div class="tech-category">
<div class="category-title">AI / ML</div>
<div class="tech-stack-grid">
<div class="tech-box tech-rag"><div class="tech-icon">📚</div><div class="tech-name">RAG</div></div>
<div class="tech-box tech-llm"><div class="tech-icon">🧠</div><div class="tech-name">LLMs</div></div>
<div class="tech-box tech-vector"><div class="tech-icon">📐</div><div class="tech-name">Embeddings</div></div>
<div class="tech-box tech-vectordb"><div class="tech-icon">🔷</div><div class="tech-name">Vector Databases</div></div>
</div>
</div>

<div class="tech-category">
<div class="category-title">Cloud & Tools</div>
<div class="tech-stack-grid">
<div class="tech-box tech-aws"><div class="tech-icon">☁️</div><div class="tech-name">AWS</div></div>
<div class="tech-box tech-git"><div class="tech-icon">🐙</div><div class="tech-name">Git</div></div>
<div class="tech-box tech-docker"><div class="tech-icon">🐳</div><div class="tech-name">Docker</div></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)