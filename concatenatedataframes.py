import streamlit as st
import pandas as pd
from io import StringIO

def main():
    st.title("Content Creation Tool")
    
    # File uploader for CSV files
    uploaded_file = st.file_uploader("Upload a CSV file (optional)", type="csv")
    
    # If a file is uploaded, read it into a DataFrame
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Contents of the uploaded file:")
        st.dataframe(df)

    # Inputs for keyword, title, and description
    keyword = st.text_input("Enter Keyword:")
    title = st.text_input("Enter Title:")
    description = st.text_area("Enter Description:")
    
    if st.button("Submit"):
        if keyword and title and description:
            # Create a DataFrame from the user input
            data = {
                "Keyword": [keyword],
                "Title": [title],
                "Description": [description]
            }
            df_input = pd.DataFrame(data)

            # Concatenate with the uploaded DataFrame if it exists
            if uploaded_file is not None:
                df = pd.concat([df, df_input], ignore_index=True)
            else:
                df = df_input
            
            # Convert DataFrame to CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Content",
                data=csv,
                file_name='content.csv',
                mime='text/csv'
            )
        else:
            st.error("Please fill out all fields.")

if __name__ == "__main__":
    main()
