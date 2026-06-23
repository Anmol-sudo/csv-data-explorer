import streamlit as st
import pandas as pd
st.title("CSV File Uploader")

# 1. Create the file uploader widget

uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])


if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading csv file: {e}")

    st.subheader("Previewing Uploaded Data")
    if st.checkbox("Show full dataset"):
        st.dataframe(df)
    else:
        st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.error("No numeric columns found")
        st.stop()
    st.subheader("Select Columns for bar chart")
    column = st.selectbox(
        "Choose Column",
        numeric_cols
    )

    st.subheader("Bar Chart")
    st.bar_chart(data=df[column].value_counts())

    st.header("Scatter Chart")
    st.subheader("Select x and y axis for line chart")
    x = st.selectbox(
        "Select x",
        numeric_cols
    )
    y = st.selectbox(
        "Select y",
        numeric_cols
    )
    if x == y:
        st.warning("Please select different columns")
    else:
        st.scatter_chart(data=df,x=x,y=y,x_label=x,y_label=y)

    st.header("Correlation Matrix")
    st.dataframe(df.corr(numeric_only=True))

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