import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disable the warning about file uploader encoding
st.set_option('deprecation.showfileUploaderEncoding', False)

# Provide the URL of your hosted CSV file
file_url = "https://data.gov.in/files/ogdpv2dms/s3fs-public/Report-47-B-20042015020705263PM-2011-2012.csv"

# Load your CSV file
@st.cache  # Cache the data to avoid reloading on every interaction
def load_data():
    return pd.read_csv(file_url, encoding='ISO-8859-1')

data = load_data()

# Main app content
st.title("Women in the Workplace Insights - India")

# Show a preview of the loaded data
st.subheader("Data Preview")
st.write(data.head())

# Data exploration and analysis
st.subheader("Salary Distribution Analysis")
salary_col = st.selectbox("Select salary column", data.columns, index=0)
sns.histplot(data[salary_col].dropna(), kde=True)
st.pyplot()

st.subheader("Benefits Analysis")
maternity_col = st.selectbox("Select maternity benefits column", data.columns, index=0)
wellness_leaves_col = st.selectbox("Select wellness leaves column", data.columns, index=0)

st.write("Maternity Benefits Distribution:")
sns.countplot(data[maternity_col].dropna())
st.pyplot()

st.write("Wellness Leaves Distribution:")
sns.countplot(data[wellness_leaves_col].dropna())
st.pyplot()

st.subheader("Women-led Startups in India")
startup_col = st.selectbox("Select column indicating women-led startups", data)
