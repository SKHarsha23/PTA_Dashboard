# pta_app.py

import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import numpy as np

st.set_page_config(page_title="PTAI & SEIFA Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("sydney_sa2_pta_geom_modes.csv")
    gdf = gpd.read_file("Assignment_Resources/SA2_2021_AUST_GDA2020.shp")
    return df, gdf

pta_data_raw, suburb_shapes = load_data()

pta_data = pta_data_raw.rename(columns={
    'pta_train': 'Train',
    'pta_bus': 'Bus',
    'pta_lightrail': 'Light Rail',
    'pta_metro': 'Metro'
})

suburb_list = sorted(pta_data['SA2_NAME_2011'].dropna().unique())
selected_suburb = st.sidebar.selectbox("Select Suburb", suburb_list, key="suburb_selectbox")
suburb_data = pta_data[pta_data['SA2_NAME_2011'].str.lower() == selected_suburb.lower()]
shape_row = suburb_shapes[suburb_shapes['SA2_NAME21'].str.lower() == selected_suburb.lower()]

if suburb_data.empty or shape_row.empty:
    st.warning("❌ Selected suburb not found in one of the datasets.")
    st.stop()

# ------------------ MAP ------------------
st.subheader("Suburb Boundary Map")
shape_row_wgs84 = shape_row.to_crs(epsg=4326)
centroid = shape_row_wgs84.geometry.centroid.iloc[0]
m = folium.Map(location=[centroid.y, centroid.x], zoom_start=13)
folium.GeoJson(shape_row_wgs84).add_to(m)
st_folium(m, width=700, height=500)

# ------------------ DATA TABLE ------------------
st.subheader("PTAI Scores and IRSD")

mode_cols = ['Train', 'Bus', 'Light Rail', 'Metro']
missing_cols = [col for col in mode_cols if col not in suburb_data.columns]
if missing_cols:
    st.error(f"❌ Mode-wise PTAI columns not found: {missing_cols}")
    st.stop()

score_table = suburb_data[mode_cols + ['pta_score', 'IRSD_SCORE']].rename(columns={
    'pta_score': 'Total PTAI',
    'IRSD_SCORE': 'IRSD Score'
})
st.dataframe(score_table.style.highlight_max(axis=1, color='lightgreen'), use_container_width=True)

# ------------------ PTAI PLOT ------------------
st.subheader("PTAI Modes vs IRSD Score")
scores = suburb_data[mode_cols].values.flatten()
irsd = suburb_data['IRSD_SCORE'].values[0]
avg_scores = pta_data[mode_cols].mean()

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=mode_cols, y=scores, ax=ax, palette='crest')

for i, mode in enumerate(mode_cols):
    ax.axhline(avg_scores[mode], color='gray', linestyle='--', linewidth=1)
    ax.text(i, avg_scores[mode] + 0.05 * max(scores.max(), 1), f"Avg: {avg_scores[mode]:.0f}", color='gray', ha='center', fontsize=8)

ax.set_ylabel("PTAI Score")
ax.set_title(f"{selected_suburb}: PTAI by Mode vs Suburb Averages")
st.pyplot(fig)

# ------------------ INTERPRETATION ------------------
interpretation = f"""
**Interpretation for {selected_suburb}:**
- Bus PTAI: {scores[1]:.0f} vs Avg {avg_scores['Bus']:.0f}
- Train PTAI: {scores[0]:.0f} vs Avg {avg_scores['Train']:.0f}
- Light Rail PTAI: {scores[2]:.0f}, Metro PTAI: {scores[3]:.0f}
- Total PTAI: {suburb_data['pta_score'].values[0]:.2f}, IRSD: {irsd:.0f}
"""
st.markdown(interpretation)

# ------------------ CORRELATION ANALYSIS ------------------
st.subheader("Correlation between PTAI Modes and IRSD Score")

cor_data = pta_data[['Train', 'Bus', 'Light Rail', 'Metro', 'pta_score', 'IRSD_SCORE']].dropna()
correlations = {}

for col in ['Train', 'Bus', 'Light Rail', 'Metro', 'pta_score']:
    r, _ = pearsonr(cor_data[col], cor_data['IRSD_SCORE'])
    correlations[col] = round(r, 3)

cor_df = pd.DataFrame(list(correlations.items()), columns=['PTAI Component', 'Correlation with IRSD'])
st.dataframe(cor_df, use_container_width=True)

st.markdown("""
**Correlation Insight:**
- Values closer to **+1 or -1** suggest stronger relationships.
- Weak correlations (near 0) indicate PTAI mode alone may not predict socio-economic advantage.
""")


