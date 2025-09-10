import streamlit as st
import pandas as pd

# Load the Excel file
@st.cache_data
def load_data():
    file_path = "data/final.xlsx"
    df = pd.read_excel(file_path, engine="openpyxl")
    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

df = load_data()

# Display logo and branding
st.image("data/logo.png", width=200)
st.markdown("### Powered by FM MOBILE PARTS")

st.title("📱 LCD Model Finder")

# Input for searching compatible model
query = st.text_input("Enter a compatible model to search:")

if query:
    # Search in compatible_models column
    results = df[df["compatible_models"].str.contains(query, case=False, na=False)]
    if not results.empty:
        st.success(f"✅ Found {len(results)} matching records.")
        st.write("### Compatible Original Models:")
        st.table(results[["models"]].drop_duplicates().reset_index(drop=True))
    else:
        st.error("❌ No matching model found.")

# Hide detected columns & sample rows: not displayed on the page
