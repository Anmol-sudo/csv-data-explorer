import streamlit as st
import pandas as pd
st.title("CSV File Uploader")

# 1. Create the file uploader widget
try:
    uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])
except Exception as e:
    st.error(f"Error reading file: {e}")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Previewing Uploaded Data")
    if st.checkbox("Show full dataset"):
        st.dataframe(df)
    else:
        st.dataframe(df.head())

    st.subheader("Number of rows and columns")
    rows, cols = df.shape
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", rows)
    with col2:
        st.metric("Columns",cols)

    st.subheader("Missing values")
    st.write(df.isnull().sum())

    st.subheader("Summary Statistics")
    st.table(df.describe())