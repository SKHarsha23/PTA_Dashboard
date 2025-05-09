# 📍 PTA & SEIFA Dashboard

This repository contains all code, datasets, and resources used for the **PTAI** (Public Transport Accessibility Index) and **SEIFA (IRSD)** spatial analysis and interactive Streamlit dashboard.

---

## 🎯 Project Overview

This dashboard enables users to:
- 🔍 Select a suburb in Sydney
- 🗺️ View its boundary on a map
- 🚆 Compare PTAI scores by **transport mode** vs **citywide suburb averages**
- 📊 Analyze socio-economic disadvantage (IRSD scores)
- 🤝 Understand correlations between transport accessibility and equity

---

## 📁 Files Included

| File / Folder | Description |
|---------------|-------------|
| `pta_app.py` | Main Streamlit dashboard code |
| `sydney_sa2_pta_geom_modes.csv` | Cleaned dataset with mode-wise PTAI + IRSD |
| `gtfs_data/` | Extracted GTFS transit schedule files (`stops.txt`, `routes.txt`, etc.) |
| `SA2_2021_AUST_GDA2020/` | Shapefile folder for SA2 suburb boundaries |
| `.ipynb` notebooks | Data processing, PTAI calculations, spatial joins, map generation |
| `.png` figures | High-quality maps and graphs used in the report |
| `requirements.txt` | All Python package dependencies |

---

## ⚙️ How to Run

### 📦 1. Clone the repository:
```bash
git clone https://github.com/SKHarsha23/PTA_Dashboard.git

cd PTA_Dashboard

pip install -r requirements.txt

streamlit run pta_app.py

This project is licensed under the MIT License.
Feel free to use, fork, and cite with attribution.
