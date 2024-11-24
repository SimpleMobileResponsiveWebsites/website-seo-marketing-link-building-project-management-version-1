import streamlit as st
import pandas as pd

# Sample DataFrames for demonstration (you can replace these with your data processing logic)
def load_sample_data():
    # Load or create sample data for demonstration purposes
    return pd.DataFrame({
        'Client': ['Client A', 'Client B'],
        'Project': ['Project 1', 'Project 2'],
        'Progress': [50, 70]
    })

def home():
    st.title("Home Page")
    st.write("Welcome to the Multi-Page Streamlit App!")
    st.write("Use the sidebar to navigate through different sections.")

def client_project_info():
    st.title("Client & Project Info")
    df = load_sample_data()
    st.write("Current Projects:")
    st.dataframe(df)
    
    # Input section for new client/project information
    with st.form("client_project_form"):
        client_name = st.text_input("Client Name")
        project_name = st.text_input("Project Name")
        progress = st.slider("Project Progress", 0, 100, 50)
        submitted = st.form_submit_button("Add Project")
        
        if submitted:
            st.success(f"Added project for {client_name}: {project_name} with {progress}% progress.")

def content_creation_tool():
    st.title("Content Creation Tool")
    # Simulated content creation tool (you can implement your logic)
    with st.form("content_form"):
        content_name = st.text_input("Content Name")
        content_description = st.text_area("Content Description")
        created = st.form_submit_button("Create Content")
        
        if created:
            st.success(f"Content '{content_name}' has been created!")
    
    # Display created content (replace with real content fetching)
    st.write("### Created Content:")
    st.write("1. Content Example 1")
    st.write("2. Content Example 2")

def keyword_input_form():
    st.title("Keyword Input Form")
    keywords = st.text_area("Enter Keywords (comma-separated)")
    
    if st.button("Submit Keywords"):
        keyword_list = [k.strip() for k in keywords.split(',')]
        st.write("Submitted Keywords:")
        st.write(keyword_list)

def keyword_search_tracker():
    st.title("Keyword Search Tracker")
    keyword_search_data = {
        'Keyword': ['Keyword1', 'Keyword2'],
        'Search Volume': [1500, 1000],
        'Ranking Position': [5, 10],
    }
    df = pd.DataFrame(keyword_search_data)
    st.write("Keyword Search Tracking Data:")
    st.dataframe(df)

def link_management():
    st.title("Link Management")
    with st.form("link_management_form"):
        link_name = st.text_input("Link Name")
        link_url = st.text_input("Link URL")
        added = st.form_submit_button("Add Link")
        
        if added:
            st.success(f"Added link: {link_name} - {link_url}")
    
    # Display list of links (replace with real link fetching)
    st.write("### Existing Links:")
    st.write("1. Example Link 1")
    st.write("2. Example Link 2")

def tasks_and_milestones():
    st.title("Tasks & Milestones")
    tasks = st.text_area("Enter Tasks (line-separated)")
    
    if st.button("Submit Tasks"):
        task_list = [task.strip() for task in tasks.split('\n')]
        st.write("Submitted Tasks:")
        st.write(task_list)

def conclusion():
    st.title("Conclusion")
    st.write("Thank you for using this application!")
    st.write("Your data has been processed successfully.")

def about():
    st.title("About This App")
    st.write("This application integrates several functionalities for managing projects, keywords, content, and links.")
    st.write("Created using Streamlit.")

# Sidebar for navigation
pages = {
    "Home": home,
    "Client & Project Info": client_project_info,
    "Content Creation Tool": content_creation_tool,
    "Keyword Input Form": keyword_input_form,
    "Keyword Search Tracker": keyword_search_tracker,
    "Link Management": link_management,
    "Tasks & Milestones": tasks_and_milestones,
    "Conclusion": conclusion,
    "About": about,
}

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Execute the selected page function
pages[selection]()
