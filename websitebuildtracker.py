import streamlit as st
import pandas as pd
from datetime import datetime

def create_site_build_app():
    st.set_page_config(page_title="Website Build Tracker", layout="wide")
    
    # Custom CSS
    st.markdown("""
        <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #f0f2f6;
            padding: 10px 20px;
            border-radius: 4px 4px 0 0;
        }
        .stTabs [aria-selected="true"] {
            background-color: #2c3e50;
            color: white;
        }
        .section-header {
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .sub-header {
            background-color: #34495e;
            color: white;
            padding: 5px 10px;
            border-radius: 3px;
            margin: 5px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Project Timeline
    st.title("Website Build Tracker")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        begin_date = st.date_input("Begin Date:", key="begin_date")
    with col2:
        mid_term = st.date_input("Mid-Term:", key="mid_term")
    with col3:
        final_date = st.date_input("Final:", key="final_date")

    # Site Plan Layout Section
    st.markdown('<div class="section-header">Site Plan Layout Draft</div>', unsafe_allow_html=True)
    
    # Initialize session state for menu items
    if 'menu_items' not in st.session_state:
        st.session_state.menu_items = {
            'Main Menu (parent page)': [''] * 10,
            'Sub Menu #1 (child pages)': [''] * 10,
            'Sub Menu #2 (grandchild pages)': [''] * 10,
            'Sub Menu #3': [''] * 10,
            'Sub Menu #4': [''] * 10
        }

    # Create tabs for different menu levels
    menu_tabs = st.tabs([
        "Main Menu", "Sub Menu #1", "Sub Menu #2", "Sub Menu #3", "Sub Menu #4"
    ])

    # For each menu level
    for idx, (menu_name, tab) in enumerate(zip(st.session_state.menu_items.keys(), menu_tabs)):
        with tab:
            st.markdown(f'<div class="sub-header">{menu_name}</div>', unsafe_allow_html=True)
            cols = st.columns(5)
            for i in range(10):
                col_idx = i % 5
                with cols[col_idx]:
                    page_num = i + 1
                    st.text_input(
                        f"Page #{page_num}",
                        key=f"{menu_name}_page_{page_num}",
                        value=st.session_state.menu_items[menu_name][i]
                    )

    # Site Plan Edits Section
    st.markdown('<div class="section-header">Site Plan Edits Tracking</div>', unsafe_allow_html=True)
    
    # Create tabs for Mid-Term and Final edits
    edit_tabs = st.tabs(["Mid-Term Edits", "Final Edits"])

    for edit_type in edit_tabs:
        with edit_type:
            if f'edits_{edit_type}' not in st.session_state:
                st.session_state[f'edits_{edit_type}'] = pd.DataFrame({
                    'Page URL': [''] * 20,
                    'Edit': [''] * 20,
                    'Screen Shot': [''] * 20,
                    'Status': ['Not Started'] * 20
                })

            # Create edits table
            status_options = ['Not Started', 'In Progress', 'Review', 'Completed']
            
            for i in range(len(st.session_state[f'edits_{edit_type}'])):
                col1, col2, col3, col4 = st.columns([3, 3, 2, 2])
                
                with col1:
                    st.session_state[f'edits_{edit_type}'].at[i, 'Page URL'] = st.text_input(
                        "Page URL",
                        st.session_state[f'edits_{edit_type}'].at[i, 'Page URL'],
                        key=f"url_{edit_type}_{i}"
                    )
                
                with col2:
                    st.session_state[f'edits_{edit_type}'].at[i, 'Edit'] = st.text_area(
                        "Edit Description",
                        st.session_state[f'edits_{edit_type}'].at[i, 'Edit'],
                        key=f"edit_{edit_type}_{i}",
                        height=100
                    )
                
                with col3:
                    st.session_state[f'edits_{edit_type}'].at[i, 'Screen Shot'] = st.text_input(
                        "Screenshot Link",
                        st.session_state[f'edits_{edit_type}'].at[i, 'Screen Shot'],
                        key=f"screenshot_{edit_type}_{i}"
                    )
                
                with col4:
                    st.session_state[f'edits_{edit_type}'].at[i, 'Status'] = st.selectbox(
                        "Status",
                        status_options,
                        index=status_options.index(st.session_state[f'edits_{edit_type}'].at[i, 'Status']),
                        key=f"status_{edit_type}_{i}"
                    )

    # Export and Save Options
    st.markdown('<div class="section-header">Export Options</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Save Progress"):
            st.success("Progress saved successfully!")
            
    with col2:
        if st.button("Export to Excel"):
            # Create Excel export logic here
            st.success("Export completed!")

if __name__ == "__main__":
    create_site_build_app()
