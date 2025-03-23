import streamlit as st

# Set page config
st.set_page_config(page_title="ESCOPlus | Python", layout="centered")

# ---------- Top Navigation Bar ----------
with st.container():
    st.markdown("""
        <style>
            .topnav {
                background-color: #ffa733;
                overflow: hidden;
                padding: 10px 20px;
                font-family: 'Segoe UI', sans-serif;
                display: flex;
                align-items: center;
                justify-content: space-between;
                color: white;
                font-weight: 600;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            .topnav a {
                margin: 0 20px;
                text-decoration: none;
                color: white;
            }
            .menu {
                font-size: 1.5em;
                font-weight: bold;
            }
        </style>
        <div class="topnav">
            <div class="menu">EscoPlus⁺</div>
            <div>
                <a href="#">ESCOPlus Hub</a>
                <a href="#">Trends</a>
                <a href="#">New skills</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---------- Main Card Container ----------
with st.container():
    st.markdown("""
        <style>
            .card {
                background-color: #52697e;
                color: white;
                border-radius: 10px;
                padding: 25px;
                font-family: 'Segoe UI', sans-serif;
                margin-top: -10px;
            }
            .card h2 {
                text-align: center;
                margin-bottom: 0;
            }
            .section-title {
                font-size: 18px;
                margin-top: 30px;
                margin-bottom: 10px;
                font-weight: bold;
                border-bottom: 1px solid #d4a759;
                padding-bottom: 3px;
            }
            .label-container {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            .skill-label {
                background-color: #0d47a1;
                padding: 8px 14px;
                border-radius: 6px;
                color: white;
                font-size: 14px;
                font-weight: 500;
                display: inline-block;
            }
            .description {
                font-size: 15px;
                color: #ddd;
                margin-top: 10px;
            }
        </style>

        <div class="card">
            <h2>Python (Programming Language)</h2>
            <div class="description">
                The techniques and principles of software development, such as analysis, algorithms, coding, testing and compiling of programming paradigms in Python.
            </div>

            <div class="section-title">Alternative labels</div>
            <div class="label-container">
                <div class="skill-label">python-jira</div>
                <div class="skill-label">python3.10</div>
                <div class="skill-label">python-import</div>
            </div>

            <div class="section-title">New skills</div>
            <div class="label-container">
                <div class="skill-label">deep learning</div>
                <div class="skill-label">python-logging</div>
                <div class="skill-label">django</div>
                <div class="skill-label">pytest</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
