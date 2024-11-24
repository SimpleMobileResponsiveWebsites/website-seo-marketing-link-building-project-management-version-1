import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Project Work Sheet",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Add custom CSS to match Excel-like styling
    st.markdown("""
        <style>
        .stTextInput, .stTextArea {
            background-color: white;
            border: 1px solid #cccccc;
        }
        .section-header {
            background-color: #2c3e50;
            padding: 5px 10px;
            border-radius: 5px;
            color: white;
            margin: 10px 0px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Main title
    st.title("Project Work Sheet")
    
    # Client Information Section
    st.markdown('<div class="section-header">Client Information</div>', unsafe_allow_html=True)
    
    # Create a form
    with st.form("client_info_form"):
        # Client Information fields
        client_name = st.text_input("Client Name:")
        phone = st.text_input("Phone:")
        email = st.text_input("eMail:")
        address = st.text_area("Address:")
        
        # Project Information Section
        st.markdown('<div class="section-header">Project Information</div>', unsafe_allow_html=True)
        
        # Add project information fields
        project_name = st.text_input("Project Name:")
        project_description = st.text_area("Project Description:")
        start_date = st.date_input("Start Date:")
        
        # Add a submit button
        submitted = st.form_submit_button("Save Information")
        
        if submitted:
            # You can add functionality here to save the form data
            st.success("Information saved successfully!")
            
            # Display submitted information in a formatted way
            st.write("### Submitted Information:")
            st.write(f"**Client Name:** {client_name}")
            st.write(f"**Phone:** {phone}")
            st.write(f"**Email:** {email}")
            st.write(f"**Address:** {address}")
            st.write(f"**Project Name:** {project_name}")
            st.write(f"**Project Description:** {project_description}")
            st.write(f"**Start Date:** {start_date}")

if __name__ == "__main__":
    main()
