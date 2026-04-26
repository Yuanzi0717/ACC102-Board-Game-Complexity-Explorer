import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Board Game Complexity Explorer",
    page_icon="🎲",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0) !important;
    border-bottom: none !important;
    box-shadow: none !important;
    height: 0px !important; 
}

.block-container {
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}

.main {
    background-color: #f9fbff;
}

.hero-box {
    background-color: #ffffff;
    padding: 2.5rem 2rem 2rem 2rem; 
    border-radius: 16px;
    border: 1px solid #e0e6ed;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    margin-top: 0.5rem;  
    margin-bottom: 2rem;
}

.metric-container {
    background-color: white;
    padding: 1rem;
    border-radius: 12px;
    border-top: 4px solid #4A90E2;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    text-align: center;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.metric-container:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 22px rgba(0,0,0,0.12);
}

.metric-label {
    font-size: 0.9rem;
    color: #6b7280;
}

.metric-value {
    font-size: 1.6rem;
    font-weight: bold;
    color: #111827;
}

.interpretation-container {
    background-color: #ffffff;    
    padding: 1.5rem;              
    border-radius: 12px;           
    border: 1.5px solid #e0e6ed;   
    box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
    margin-top: 1.5rem;           
    margin-bottom: 1.5rem;
}

.recommendation-box {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1.5px solid #e0e6ed;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}

</style>
""", unsafe_allow_html=True)

# ---------- DATA LOADING ----------
@st.cache_data
def load_data():
    df = pd.read_csv("bgg_cleaned.csv")

    needed_cols = [
        "name",
        "year_published",
        "min_players",
        "max_players",
        "play_time",
        "rating_average",
        "complexity_average",
        "owned_users"
    ]

    df = df.dropna(subset=["complexity_average", "rating_average", "owned_users"])

    for col in needed_cols:
        if col not in df.columns:
            st.error(f"Missing required column: {col}")
            st.stop()

    return df

df = load_data()

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("📊 Control Panel")
    st.markdown("---")

    complexity_range = st.slider(
        "Select Complexity Range",
        float(df["complexity_average"].min()),
        float(df["complexity_average"].max()),
        (2.0, 3.8),
        0.1
    )

    min_rating = st.slider(
        "Minimum User Rating",
        float(df["rating_average"].min()),
        float(df["rating_average"].max()),
        6.0,
        0.1
    )

    min_owned_users = st.slider(
        "Minimum Owned Users",
        int(df["owned_users"].min()),
        int(df["owned_users"].max()),
        1000,
        100
    )

    recommendation_style = st.selectbox(
        "Recommendation Goal",
        [
            "Balanced Choice",
            "Highest Rated",
            "Most Popular",
            "Lower Complexity"
        ]
    )

    st.markdown("---")
    st.caption("ACC102 Mini Assignment | Interactive Data Analysis Tool")

# ---------- FILTERING ----------
filtered_df = df[
    (df["complexity_average"] >= complexity_range[0]) &
    (df["complexity_average"] <= complexity_range[1]) &
    (df["rating_average"] >= min_rating) &
    (df["owned_users"] >= min_owned_users)
].copy()

filtered_df = filtered_df.sort_values(by="rating_average", ascending=False)

# ---------- HERO SECTION ----------
st.markdown('<div class="hero-box">', unsafe_allow_html=True)
st.title("🎲 Board Game Complexity Explorer")
st.markdown("""
This interactive tool helps users compare board games across different complexity levels and identify a practical balance between **challenge**, **rating**, and **popularity**.

**Target audience:** board game buyers, casual players, and game designers.

Instead of only showing charts, this tool allows users to filter games and receive recommendations based on their preferred balance between complexity, quality, and market popularity.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- MAIN CONTENT ----------
if not filtered_df.empty:

    # ---------- METRICS ----------
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(
            f'<div class="metric-container"><div class="metric-label">Matching Games</div><div class="metric-value">{len(filtered_df)}</div></div>',
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            f'<div class="metric-container"><div class="metric-label">Average Rating</div><div class="metric-value">{filtered_df["rating_average"].mean():.2f}</div></div>',
            unsafe_allow_html=True
        )

    with m3:
        st.markdown(
            f'<div class="metric-container"><div class="metric-label">Average Complexity</div><div class="metric-value">{filtered_df["complexity_average"].mean():.2f}</div></div>',
            unsafe_allow_html=True
        )

    with m4:
        st.markdown(
            f'<div class="metric-container"><div class="metric-label">Average Owned Users</div><div class="metric-value">{filtered_df["owned_users"].mean():.0f}</div></div>',
            unsafe_allow_html=True
        )

    st.write("")

    # ---------- MAIN CHART ----------
    st.subheader("1. Complexity, Rating, and Popularity")

    fig = px.scatter(
        filtered_df,
        x="complexity_average",
        y="rating_average",
        size="owned_users",
        color="complexity_average",
        hover_name="name",
        trendline="ols",
        trendline_color_override="red",
        hover_data={
            "complexity_average": ":.2f",
            "rating_average": ":.2f",
            "owned_users": True,
            "year_published": True,
            "play_time": True
        },
        color_continuous_scale="Viridis",
        labels={
            "complexity_average": "Complexity Average",
            "rating_average": "Rating Average",
            "owned_users": "Owned Users"
        },
        template="plotly_white",
        height=650
    )

    fig.update_layout(
        title="Relationship between Complexity and Rating",
        xaxis_title="Complexity Average",
        yaxis_title="Rating Average",
        margin=dict(l=20, r=20, t=60, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------- INTERPRETATION ----------
    st.markdown('<div class="interpretation-container">', unsafe_allow_html=True)
    st.markdown("**🔍 Interpretation**")

    correlation = filtered_df["complexity_average"].corr(filtered_df["rating_average"])
    st.write(f"Correlation in this filtered range: **{correlation:.2f}**")

    if correlation > 0.4:
      st.write("The current selection shows a clear positive relationship between complexity and rating.")
    elif correlation > 0.2:
      st.write("The current selection shows a moderate positive relationship between complexity and rating.")
    elif correlation > 0:
      st.write("The current selection shows a weak positive relationship between complexity and rating.")
    else:
      st.write("The current selection does not show a positive relationship between complexity and rating.")

    st.write("Popularity is represented by bubble size, using owned users as an indicator.")
    st.write("This means a highly rated game is not always the most widely owned game. Users should consider both quality and market popularity before making a decision.")
    st.write("Medium-to-high complexity games may be more suitable for core board game players, but they may not always appeal to the broader mass market.")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- RECOMMENDATION SECTION ----------
    st.subheader("2. Recommended Games Based on Current Filters")

    recommendation_df = filtered_df.copy()

    # Normalized indicators for recommendation score
    recommendation_df["rating_score"] = (
        recommendation_df["rating_average"] - recommendation_df["rating_average"].min()
    ) / (
        recommendation_df["rating_average"].max() - recommendation_df["rating_average"].min() + 0.0001
    )

    recommendation_df["popularity_score"] = (
        recommendation_df["owned_users"] - recommendation_df["owned_users"].min()
    ) / (
        recommendation_df["owned_users"].max() - recommendation_df["owned_users"].min() + 0.0001
    )

    recommendation_df["complexity_score"] = (
        recommendation_df["complexity_average"] - recommendation_df["complexity_average"].min()
    ) / (
        recommendation_df["complexity_average"].max() - recommendation_df["complexity_average"].min() + 0.0001
    )

    if recommendation_style == "Balanced Choice":
        recommendation_df["recommendation_score"] = (
            recommendation_df["rating_score"] * 0.45 +
            recommendation_df["popularity_score"] * 0.35 +
            (1 - abs(recommendation_df["complexity_average"] - 2.8) / 2.8) * 0.20
        )
        recommendation_text = "This option recommends games with a strong balance of rating, popularity, and manageable complexity."

    elif recommendation_style == "Highest Rated":
        recommendation_df["recommendation_score"] = (
            recommendation_df["rating_score"] * 0.70 +
            recommendation_df["popularity_score"] * 0.20 +
            (1 - recommendation_df["complexity_score"]) * 0.10
        )
        recommendation_text = "This option prioritizes games with the highest user ratings."

    elif recommendation_style == "Most Popular":
        recommendation_df["recommendation_score"] = (
            recommendation_df["popularity_score"] * 0.70 +
            recommendation_df["rating_score"] * 0.20 +
            (1 - recommendation_df["complexity_score"]) * 0.10
        )
        recommendation_text = "This option prioritizes games owned by more users, which may reflect broader market acceptance."

    else:
        recommendation_df["recommendation_score"] = (
            (1 - recommendation_df["complexity_score"]) * 0.50 +
            recommendation_df["rating_score"] * 0.30 +
            recommendation_df["popularity_score"] * 0.20
        )
        recommendation_text = "This option recommends games that are easier to approach while still maintaining good ratings and popularity."

    recommended_games = recommendation_df.sort_values(
        by="recommendation_score",
        ascending=False
    ).head(10)

    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.markdown(f"**Recommendation Goal:** {recommendation_style}")
    st.write(recommendation_text)
    st.write("The recommendation score is calculated from rating, owned users, and complexity based on the selected goal.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.dataframe(
        recommended_games[
            [
                "name",
                "year_published",
                "min_players",
                "max_players",
                "play_time",
                "rating_average",
                "complexity_average",
                "owned_users",
                "recommendation_score"
            ]
        ].rename(columns={
            "name": "Game Title",
            "year_published": "Year Published",
            "min_players": "Min Players",
            "max_players": "Max Players",
            "play_time": "Play Time",
            "rating_average": "Average Rating",
            "complexity_average": "Average Complexity",
            "owned_users": "Owned Users",
            "recommendation_score": "Recommendation Score"
        }),
        use_container_width=True,
        hide_index=True
    )

    # ---------- TOP GAMES ----------
    st.subheader("3. Most Owned Games in the Current Selection")

    top_10 = filtered_df.nlargest(10, "owned_users")

    fig2 = px.bar(
        top_10,
        x="name",
        y="owned_users",
        color="rating_average",
        text="complexity_average",
        labels={
            "name": "Game Title",
            "owned_users": "Owned Users",
            "rating_average": "Rating Average",
            "complexity_average": "Complexity"
        },
        title="Top 10 Games by Owned Users"
    )

    fig2.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig2.update_layout(
        xaxis_tickangle=-35,
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ---------- DATA TABLE ----------
    st.subheader("4. Explore the Filtered Dataset")

    with st.expander("View Filtered Data"):
        st.dataframe(
            filtered_df[
                [
                    "name",
                    "year_published",
                    "min_players",
                    "max_players",
                    "play_time",
                    "rating_average",
                    "complexity_average",
                    "owned_users"
                ]
            ].rename(columns={
                "name": "Game Title",
                "year_published": "Year Published",
                "min_players": "Min Players",
                "max_players": "Max Players",
                "play_time": "Play Time",
                "rating_average": "Average Rating",
                "complexity_average": "Average Complexity",
                "owned_users": "Owned Users"
            }),
            use_container_width=True,
            hide_index=True
        )

else:
    st.error("No data found for the current filters. Please adjust the settings in the sidebar.")

# ---------- LIMITATION NOTE ----------
st.markdown("---")
st.caption(
    "Note: This tool is designed for exploratory comparison. It shows associations between complexity, rating, and popularity, but it does not imply causal relationships."
)
