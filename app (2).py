import streamlit as st

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="IMDB Movie Intelligence App",
    layout="wide"
)

# -------------------------------
# CUSTOM CSS (DARK MODE SAFE)
# -------------------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    padding: 70px;
    border-radius: 20px;
    color: #ffffff;
    text-align: center;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 700;
}

.hero p {
    font-size: 20px;
    color: #d1d5db;
}

.card {
    padding: 28px;
    border-radius: 18px;
    background-color: #111827;   /* DARK CARD */
    color: #e5e7eb;               /* LIGHT TEXT */
    box-shadow: 0px 8px 24px rgba(0,0,0,0.6);
    height: 100%;
}

.card h3, .card h4 {
    color: #ffffff;
}

.card p {
    color: #d1d5db;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HERO SECTION
# -------------------------------
st.markdown("""
<div class="hero">
    <h1>🎬 IMDB Movie Intelligence System</h1>
    <p>Predict Movie Success • Design HIT Films • Data-Driven Decisions</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# WHAT THIS APP DOES
# -------------------------------
st.markdown("## 🚀 What Can You Do With This App?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>⭐ Predict IMDB Score</h3>
        <p>
        Enter movie details such as genre, cast, budget, and duration to predict
        the expected IMDB score <b>before the movie is released</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎯 Hit / Average / Flop</h3>
        <p>
        Automatically classify movies into <b>Hit, Average, or Flop</b>
        based on the predicted IMDB score.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Strategy Insights</h3>
        <p>
        Discover the <b>best actors, directors, genres, content ratings</b>,
        and optimal duration to create a HIT movie.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# HOW IT WORKS
# -------------------------------
st.markdown("## 🧠 How Does It Work?")

st.markdown("""
- Built using **Machine Learning (Random Forest Regressor)**
- Trained on real **IMDB movie metadata**
- Uses **genre intelligence, cast impact, and production features**
- Designed for **movie producers, analysts, and studios**
""")

# -------------------------------
# WHO IS THIS FOR
# -------------------------------
st.markdown("## 👥 Who Is This App For?")

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="card">
        <h4>🎥 Movie Producers</h4>
        <p>
        Plan films strategically to maximize IMDB ratings and audience impact.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h4>📈 Data & Business Analysts</h4>
        <p>
        Analyze trends that influence movie success and guide production decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# NAVIGATION HELP
# -------------------------------
st.markdown("## 🧭 How to Navigate")

st.info("""
👉 Use the **Sidebar (left)** to navigate:
- 🎬 **Movie Predictor** → Predict IMDB score & Hit/Flop
- 📊 **Movie Strategy Insights** → Best actors, directors, genres, ratings
""")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<hr style="border:1px solid #374151;">
<p style="text-align:center; color:#9ca3af;">
Built with ❤️ using <b>Python, Machine Learning & Streamlit</b><br>
IMDB Movie Intelligence – Capstone Project
</p>
""", unsafe_allow_html=True)
