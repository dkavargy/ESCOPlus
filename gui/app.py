# app.py

import streamlit as st
import pandas as pd

# Load the proposed skills data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/processed/proposed_skills.csv")
    except FileNotFoundError:
        st.error("Data file not found. Please make sure 'proposed_skills.csv' exists.")
        return pd.DataFrame()
    return df

# App layout
st.set_page_config(page_title="ESCOPlus Viewer", layout="wide")

st.title("🚀 ESCOPlus Framework GUI")
st.markdown("""
Explore proposed **alternative** and **new skills** detected from Stack Overflow and integrated into the ESCOPlus taxonomy.
""")

# Load data
df = load_data()

if not df.empty:
    # Sidebar filters
    st.sidebar.header("🔍 Filter Options")

    label_filter = st.sidebar.multiselect(
        "Select Label(s):",
        options=df["Label"].unique(),
        default=df["Label"].unique()
    )

    cluster_filter = st.sidebar.multiselect(
        "Select Cluster(s):",
        options=df["Cluster"].unique(),
        default=df["Cluster"].unique()
    )

    confidence_threshold = st.sidebar.slider(
        "Minimum Confidence Score:",
        min_value=0.0, max_value=1.0, value=0.6, step=0.05
    )

    similarity_threshold = st.sidebar.slider(
        "Minimum Similarity Score:",
        min_value=0.0, max_value=1.0, value=0.7, step=0.05
    )

    # Apply filters
    filtered_df = df[
        (df["Label"].isin(label_filter)) &
        (df["Cluster"].isin(cluster_filter)) &
        (df["Confidence Score"].fillna(1.0) >= confidence_threshold) &
        (df["Similarity Score"].fillna(1.0) >= similarity_threshold)
    ]

    st.subheader("📋 Filtered Skill Suggestions")
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

else:
    st.warning("No data loaded yet. Please process and export the proposed skills first.")
