import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. PAGE SETUP & DATA LOADING
# ==========================================
st.set_page_config(page_title="Academic Performance Dashboard", layout="wide")
st.title("Student Academic Performance Dashboard")
st.write("Explore how lifestyle factors and demographics affect student exam scores.")

# Apply seaborn theme for better looking web charts
sns.set_theme(style="whitegrid")

# Load the dataset (cached so it doesn't reload on every interaction)
@st.cache_data
def load_data():
    try:
        return pd.read_csv('student_performance_data.csv')
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure 'student_performance_data.csv' is in the same directory.")
        st.stop()

df = load_data()

# ==========================================
# 2. CORRELATION MATRIX (Heatmap)
# ==========================================
st.header("1. Correlation Matrix")
st.write("Visualizing the mathematical relationships between continuous variables.")

fig1, ax1 = plt.subplots(figsize=(8, 6))
numerical_df = df[['Study_Hours_Per_Week', 'Attendance_Percentage', 'Math_Score', 'Reading_Score', 'Writing_Score']]
corr_matrix = numerical_df.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax1)
ax1.set_title('Correlation Matrix of Numerical Factors', fontsize=14, pad=15)
st.pyplot(fig1)

st.divider() # Adds a clean visual break between sections

# ==========================================
# 3. BOX PLOT
# ==========================================
st.header("2. Math Scores by Parental Education")
st.write("Identifying the spread and outliers in scores across different education levels.")

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Parental_Education', y='Math_Score', palette='Set2', ax=ax2)
ax2.set_title('Math Score Distribution by Parental Education', fontsize=14)
ax2.set_xlabel('Parental Education Level')
ax2.set_ylabel('Math Score')
st.pyplot(fig2)

st.divider()

# ==========================================
# 4. VIOLIN PLOT
# ==========================================
st.header("3. Reading Score Density by Test Prep")
st.write("Analyzing the volume and distribution of scores based on course completion.")

fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.violinplot(data=df, x='Test_Prep_Course', y='Reading_Score', palette='muted', split=False, ax=ax3)
ax3.set_title('Reading Score Density by Test Prep Course', fontsize=14)
ax3.set_xlabel('Test Preparation Course')
ax3.set_ylabel('Reading Score')
st.pyplot(fig3)

st.divider()

# ==========================================
# 5. SUBJECT-WISE COMPARISON CHART
# ==========================================
st.header("4. Subject Performance Comparison")
st.write("Comparing average performance across disciplines, split by gender.")

# Melt the dataframe
melted_df = pd.melt(df, 
                    id_vars=['Gender'], 
                    value_vars=['Math_Score', 'Reading_Score', 'Writing_Score'],
                    var_name='Subject', 
                    value_name='Score')

# Clean up the subject names for the plot labels
melted_df['Subject'] = melted_df['Subject'].str.replace('_Score', '')

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(data=melted_df, x='Subject', y='Score', hue='Gender', palette='pastel', errorbar=None, ax=ax4)
ax4.set_title('Average Subject Scores Compared by Gender', fontsize=14)
ax4.set_xlabel('Subject')
ax4.set_ylabel('Average Score')
ax4.legend(title='Gender')
st.pyplot(fig4)