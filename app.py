import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. PAGE SETUP & THEME
# ==========================================
# This must be the first Streamlit command
st.set_page_config(page_title="Student Analytics", layout="wide", initial_sidebar_state="expanded")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('student_performance_data.csv')

df = load_data()

# ==========================================
# 2. SIDEBAR & KPI METRICS
# ==========================================
with st.sidebar:
    st.title("📊 Student Analytics")
    st.write("An interactive dashboard exploring the factors that impact academic success.")
    st.divider()
    st.write("**Dataset Overview:**")
    st.write(f"Total Students: {len(df)}")
    st.write("Variables: Demographics, Lifestyle, Scores")

# Main Page Title
st.title("Academic Performance Dashboard")

# Top Row KPI Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Average Math Score", value=f"{df['Math_Score'].mean():.1f}/100")
with col2:
    st.metric(label="Average Reading Score", value=f"{df['Reading_Score'].mean():.1f}/100")
with col3:
    st.metric(label="Avg Study Hours/Wk", value=f"{df['Study_Hours_Per_Week'].mean():.1f} hrs")
with col4:
    st.metric(label="Avg Attendance", value=f"{df['Attendance_Percentage'].mean():.1f}%")

st.divider()

# ==========================================
# 3. INTERACTIVE VISUALIZATIONS (PLOTLY)
# ==========================================
# Create a 2-column layout for the top two charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("1. Correlation Heatmap")
    numerical_df = df[['Study_Hours_Per_Week', 'Attendance_Percentage', 'Math_Score', 'Reading_Score', 'Writing_Score']]
    corr_matrix = numerical_df.corr()
    
    # Plotly Heatmap
    fig_heat = px.imshow(corr_matrix, text_auto=".2f", aspect="auto", color_continuous_scale='RdBu_r')
    st.plotly_chart(fig_heat, use_container_width=True)

with chart_col2:
    st.subheader("2. Math Scores by Parental Education")
    # Plotly Interactive Box Plot
    fig_box = px.box(df, x='Parental_Education', y='Math_Score', color='Parental_Education',
                     category_orders={"Parental_Education": ["High School", "Associate", "Bachelor", "Master"]})
    st.plotly_chart(fig_box, use_container_width=True)

# Create a 2-column layout for the bottom two charts
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("3. Reading Density by Test Prep")
    # Plotly Interactive Violin Plot
    fig_violin = px.violin(df, x='Test_Prep_Course', y='Reading_Score', color='Test_Prep_Course', 
                           box=True, points="all", hover_data=df.columns)
    st.plotly_chart(fig_violin, use_container_width=True)

with chart_col4:
    st.subheader("4. Subject Comparison")
    # Melt dataframe for grouped bar chart
    melted_df = pd.melt(df, id_vars=['Gender'], value_vars=['Math_Score', 'Reading_Score', 'Writing_Score'],
                        var_name='Subject', value_name='Score')
    melted_df['Subject'] = melted_df['Subject'].str.replace('_Score', '')
    
    # Calculate averages for the bar chart
    avg_scores = melted_df.groupby(['Subject', 'Gender'])['Score'].mean().reset_index()
    
    # Plotly Grouped Bar Chart
    fig_bar = px.bar(avg_scores, x='Subject', y='Score', color='Gender', barmode='group')
    fig_bar.update_layout(yaxis_range=[0,100]) # Lock Y-axis to 100 for proper scale
    st.plotly_chart(fig_bar, use_container_width=True)