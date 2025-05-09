# PTAI & SEIFA Dashboard

This repository contains all code, datasets, and resources used for the PTAI (Public Transport Accessibility Index) and SEIFA (IRSD) spatial analysis and dashboard.

## 📍 Project Overview

The dashboard allows users to:
- Select a suburb in Sydney
- View its boundary map
- Compare PTAI scores by transport mode vs suburb averages
- Analyze socio-economic disadvantage (IRSD score)
- Understand correlation between accessibility and equity

## 📁 Files Included

- `pta_app.py`: Main Streamlit dashboard code
- `sydney_sa2_pta_geom_modes.csv`: Cleaned dataset with PTAI + IRSD
- `gtfs_data/`: Extracted GTFS transit schedule files (e.g., stops.txt, routes.txt)
- `SA2_2021_AUST_GDA2020.*`: Shapefile for SA2 suburb boundaries
- `.ipynb` notebooks: Data cleaning, PTAI calculation, spatial joins, map generation
- `.png`: Figures used in the report
- `requirements.txt`: Python dependencies

## ▶️ How to Run

1. Clone the repo  
   `git clone https://github.com/YOUR_USERNAME/PTA_Dashboard.git`

2. Navigate to the folder  
   `cd PTA_Dashboard`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Run the dashboard  
   `streamlit run pta_app.py`

## 📌 Notes

- Ensure the shapefile and GTFS data remain in the same directory structure.
- Built using Python, Streamlit, Folium, and GeoPandas.

## 🔗 License

MIT License
