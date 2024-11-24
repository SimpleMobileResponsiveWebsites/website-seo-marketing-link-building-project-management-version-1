import streamlit as st
import pandas as pd
from datetime import datetime

def render_tasks_page():
    st.title("Tasks & Milestones")
    
    # Initialize session state for tasks if it doesn't exist
    if 'tasks' not in st.session_state:
        st.session_state.tasks = pd.DataFrame({
            'Description': [''] * 7,
            'Status': ['Not Started'] * 7,
            'Responsible_Party': [''] * 7,
            'Due_Date': [None] * 7,
            'Link': [''] * 7,
            'Notes': [''] * 7
        })

    # Status options
    status_options = ['Not Started', 'In Progress', 'Completed', 'Blocked', 'Delayed']
    
    # Custom CSS for styling
    st.markdown("""
        <style>
        .task-header {
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 5px;
            color: white;
            margin: 10px 0px;
        }
        .stSelectbox {
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Add new task button
    if st.button("+ Add New Task"):
        new_row = pd.DataFrame({
            'Description': [''],
            'Status': ['Not Started'],
            'Responsible_Party': [''],
            'Due_Date': [None],
            'Link': [''],
            'Notes': ['']
        })
        st.session_state.tasks = pd.concat([st.session_state.tasks, new_row], ignore_index=True)

    # Create task editor
    for idx in range(len(st.session_state.tasks)):
        with st.expander(f"Task {idx + 1}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.session_state.tasks.at[idx, 'Description'] = st.text_area(
                    "Description",
                    st.session_state.tasks.at[idx, 'Description'],
                    key=f"desc_{idx}",
                    height=100
                )
                
            with col2:
                st.session_state.tasks.at[idx, 'Status'] = st.selectbox(
                    "Status",
                    status_options,
                    index=status_options.index(st.session_state.tasks.at[idx, 'Status']),
                    key=f"status_{idx}"
                )

            col3, col4 = st.columns(2)
            
            with col3:
                st.session_state.tasks.at[idx, 'Responsible_Party'] = st.text_input(
                    "Responsible Party",
                    st.session_state.tasks.at[idx, 'Due_Date'],
                    key=f"resp_{idx}"
                )
                
            with col4:
                st.session_state.tasks.at[idx, 'Due_Date'] = st.date_input(
                    "Due Date",
                    value=datetime.today() if pd.isnull(st.session_state.tasks.at[idx, 'Due_Date']) 
                    else st.session_state.tasks.at[idx, 'Due_Date'],
                    key=f"date_{idx}"
                )

            col5, col6 = st.columns(2)
            
            with col5:
                st.session_state.tasks.at[idx, 'Link'] = st.text_input(
                    "Link",
                    st.session_state.tasks.at[idx, 'Link'],
                    key=f"link_{idx}"
                )
                
            with col6:
                st.session_state.tasks.at[idx, 'Notes'] = st.text_area(
                    "Notes",
                    st.session_state.tasks.at[idx, 'Notes'],
                    key=f"notes_{idx}",
                    height=100
                )

            if st.button("Delete Task", key=f"del_{idx}"):
                st.session_state.tasks = st.session_state.tasks.drop(idx).reset_index(drop=True)
                st.rerun()

    # Add save functionality
    if st.button("Save All Tasks"):
        # Here you would typically save to a database or file
        st.success("Tasks saved successfully!")
        
    # Add export functionality
    if st.button("Export to CSV"):
        csv = st.session_state.tasks.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="tasks_milestones.csv",
            mime="text/csv"
        )

    # Display tasks overview
    st.markdown("### Tasks Overview")
    st.dataframe(
        st.session_state.tasks,
        use_container_width=True,
        hide_index=True
    )

if __name__ == "__main__":
    render_tasks_page()
