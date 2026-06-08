# student-performance-dashboard
visualization project
# 🎓 Student Academic Performance Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-FF4B4B.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3f4f75.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)

## 📌 Overview
An end-to-end data exploration and visualization project analyzing the various factors that influence a student's academic performance. This project moves from raw data processing to a fully interactive web dashboard, allowing users to dynamically explore how lifestyle choices, demographics, and preparation impact final exam scores. 

## 🚀 Features
- **Interactive Exploratory Data Analysis (EDA):** Users can hover, zoom, and filter data points in real-time.
- **Statistical Visualizations:** Includes Correlation Heatmaps, Box Plots, Violin Plots, and Grouped Bar Charts to highlight data distributions and relationships.
- **KPI Tracking:** A top-level dashboard summarizing critical dataset metrics.
- **Containerized Architecture:** Fully dockerized for seamless, environment-agnostic deployment.

## 🛠️ Tech Stack
- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Interactive Visualization:** Plotly (Express & Graph Objects)
- **Web Framework:** Streamlit
- **Deployment & Containerization:** Docker

## 📂 Project Structure
```text
├── app.py                         # Main Streamlit application
├── student_performance_data.csv   # Dataset used for analysis
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Instructions for containerization
└── README.md                      # Project documentation