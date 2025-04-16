# IMPORTS
import streamlit as st 
import pandas as pd 
import os
from io import BytesIO


# SET UP OUR APP
st.set_page_config(page_title ="DATA SWEEPER by QASIM" , layout="wide")
st.title("DATA SWEEPER by M.Qasim")
st.write("Transform your Files with build-in Data Cleaning and Visualization")
uploaded_files = st.file_uploader("Upload your File in CSV or Excel format" , type=["csv", "xlsx"],
accept_multiple_files = True)

if uploaded_files:
  for file in uploaded_files:
    file_ext = os.path.splitext(file.name)[-1].lower()
    
    if file_ext == ".csv":
      df = pd.read_csv(file)
    elif file_ext == ".xlsx":
      df = pd.read_excel(file)
    else:st.write("unsupported file type:{file_ext}")
    continue
  
  # displaying info about the file 
  st.write[f"**File Name:**{file.name}"]
  st.write(f"**File Size:**{file.size/ 1024} ")
  
  # show five rows of our data
  st.write("First five rows of your data")
  st.dataframe(df.head())
  
  # option for data cleaning
  st.subheader("Data Cleaning Option")
  if st.checkbox(f"Clean Data for {file.name}"):
    col1 ,col2 = st.columns(2)
    
    with col1:
      if st.button(f"Remove duplicates from {file.name}"):
        df.drop_duplicates(inplace= True)
        st.write("Duplicates Removed!")
    
    with col2:
     if st.button(f"Fill Missing values for {file.name}"):
       numeric_cols = df.select_dtypes(include=["number"]).columns
       df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
       st.write("Missing values filled!")    