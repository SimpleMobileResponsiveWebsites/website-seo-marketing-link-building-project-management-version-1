import streamlit as st
import pandas as pd

# Initialize a DataFrame to store user input
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Link Type", "Title", "URL", "Status", "Pursue? (Y/N)", "Home Page (Y/N)", "Resource (Y/N)"])

# Title of the application
st.title("Link Management App")

# Input fields for user data
with st.form(key='data_form'):
    link_type = st.text_input("Link Type")
    title = st.text_input("Title")
    url = st.text_input("URL")
    status = st.text_input("Status")
    pursue = st.selectbox("Pursue? (Y/N)", options=["Y", "N"])
    home_page = st.selectbox("Home Page (Y/N)", options=["Y", "N"])
    resource = st.selectbox("Resource (Y/N)", options=["Y", "N"])
    
    submit_button = st.form_submit_button(label='Add Entry')

# When the button is pressed, add to DataFrame
if submit_button:
    new_entry = {
        "Link Type": link_type,
        "Title": title,
        "URL": url,
        "Status": status,
        "Pursue? (Y/N)": pursue,
        "Home Page (Y/N)": home_page,
        "Resource (Y/N)": resource
    }
    st.session_state.data = st.session_state.data.append(new_entry, ignore_index=True)
    st.success("Entry added!")

# Display the DataFrame as a table in Streamlit
st.write("Current Entries:")
st.dataframe(st.session_state.data)

# Optional: Add a summary button
if st.button("Show Summary"):
    st.write(st.session_state.data.describe())
