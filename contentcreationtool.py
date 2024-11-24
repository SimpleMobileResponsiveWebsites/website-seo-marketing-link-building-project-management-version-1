import streamlit as st
import pandas as pd
from io import StringIO

def main():
    st.title("Content Creation Tool")
    
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
            df = pd.DataFrame(data)
            
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
