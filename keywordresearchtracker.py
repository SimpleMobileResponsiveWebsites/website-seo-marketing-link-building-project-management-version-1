import streamlit as st
import pandas as pd
import base64

def create_keyword_research_app():
    st.set_page_config(page_title="Keyword Research Tracker", layout="wide")
    
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
            background-color: #4a90e2;
            color: white;
        }
        .section-header {
            background-color: #4a90e2;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .instructions {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
            border: 1px solid #dee2e6;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Keyword Research Tracker")
    
    # Instructions Section
    st.markdown('<div class="instructions">', unsafe_allow_html=True)
    st.markdown("### Instructions:")
    instructions = [
        "1. Determine Main KWs",
        "2. Scrape for Secondary KWs",
        "3. Gather data from KW tool",
        "4. Copy/Paste to KWs sheet"
    ]
    for instruction in instructions:
        st.markdown(f"- {instruction}")
    
    # Add video link button
    if st.button("Click for Video"):
        st.info("Video tutorial would open here")
    st.markdown('</div>', unsafe_allow_html=True)

    # Create tabs for Main KWs and Secondary KWs
    tabs = st.tabs(["Main KWs", "Secondary KWs"])

    # Initialize session state for both keyword types
    for kw_type in ['main', 'secondary']:
        if f'{kw_type}_keywords' not in st.session_state:
            st.session_state[f'{kw_type}_keywords'] = pd.DataFrame({
                'Ad group': [''] * 10,
                'Keyword': [''] * 10,
                'Currency': ['USD'] * 10,
                'Avg. Monthly Searches': [0] * 10,
                'Competition': [''] * 10,
                'Suggested Bid': [0.0] * 10,
                'Impr. share': [0.0] * 10,
                'Organic avg. position': [0.0] * 10,
                'In account?': [False] * 10,
                'In plan?': [False] * 10,
                'Extracted from': [''] * 10
            })

    # Function to create keyword input form
    def create_keyword_form(kw_type, tab):
        with tab:
            st.markdown(f'<div class="section-header">{kw_type.title()} Keywords</div>', 
                       unsafe_allow_html=True)
            
            # Add new row button
            if st.button(f"Add New {kw_type.title()} Keyword", key=f"add_{kw_type}"):
                new_row = pd.DataFrame({col: [''] if col not in ['In account?', 'In plan?'] else [False] 
                                      for col in st.session_state[f'{kw_type}_keywords'].columns}, 
                                     index=[0])
                st.session_state[f'{kw_type}_keywords'] = pd.concat(
                    [st.session_state[f'{kw_type}_keywords'], new_row], 
                    ignore_index=True
                )

            # Create form for each row
            for idx in range(len(st.session_state[f'{kw_type}_keywords'])):
                with st.expander(f"Keyword Entry #{idx + 1}", expanded=False):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Ad group'] = st.text_input(
                            "Ad Group",
                            st.session_state[f'{kw_type}_keywords'].at[idx, 'Ad group'],
                            key=f"adgroup_{kw_type}_{idx}"
                        )
                        
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Keyword'] = st.text_input(
                            "Keyword",
                            st.session_state[f'{kw_type}_keywords'].at[idx, 'Keyword'],
                            key=f"keyword_{kw_type}_{idx}"
                        )
                        
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Currency'] = st.selectbox(
                            "Currency",
                            ['USD', 'EUR', 'GBP', 'JPY'],
                            key=f"currency_{kw_type}_{idx}"
                        )
                    
                    with col2:
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Avg. Monthly Searches'] = st.number_input(
                            "Avg. Monthly Searches",
                            min_value=0,
                            value=int(st.session_state[f'{kw_type}_keywords'].at[idx, 'Avg. Monthly Searches']),
                            key=f"searches_{kw_type}_{idx}"
                        )
                        
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Competition'] = st.selectbox(
                            "Competition",
                            ['Low', 'Medium', 'High'],
                            key=f"competition_{kw_type}_{idx}"
                        )
                        
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Suggested Bid'] = st.number_input(
                            "Suggested Bid",
                            min_value=0.0,
                            value=float(st.session_state[f'{kw_type}_keywords'].at[idx, 'Suggested Bid']),
                            key=f"bid_{kw_type}_{idx}"
                        )
                    
                    with col3:
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Impr. share'] = st.number_input(
                            "Impression Share",
                            min_value=0.0,
                            max_value=100.0,
                            value=float(st.session_state[f'{kw_type}_keywords'].at[idx, 'Impr. share']),
                            key=f"share_{kw_type}_{idx}"
                        )
                        
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Organic avg. position'] = st.number_input(
                            "Organic Avg. Position",
                            min_value=0.0,
                            value=float(st.session_state[f'{kw_type}_keywords'].at[idx, 'Organic avg. position']),
                            key=f"position_{kw_type}_{idx}"
                        )
                        
                        col3_1, col3_2 = st.columns(2)
                        with col3_1:
                            st.session_state[f'{kw_type}_keywords'].at[idx, 'In account?'] = st.checkbox(
                                "In Account?",
                                value=bool(st.session_state[f'{kw_type}_keywords'].at[idx, 'In account?']),
                                key=f"account_{kw_type}_{idx}"
                            )
                        with col3_2:
                            st.session_state[f'{kw_type}_keywords'].at[idx, 'In plan?'] = st.checkbox(
                                "In Plan?",
                                value=bool(st.session_state[f'{kw_type}_keywords'].at[idx, 'In plan?']),
                                key=f"plan_{kw_type}_{idx}"
                            )
                        
                        st.session_state[f'{kw_type}_keywords'].at[idx, 'Extracted from'] = st.text_input(
                            "Extracted From",
                            st.session_state[f'{kw_type}_keywords'].at[idx, 'Extracted from'],
                            key=f"extracted_{kw_type}_{idx}"
                        )

    # Create forms in each tab
    for tab, kw_type in zip(tabs, ['main', 'secondary']):
        create_keyword_form(kw_type, tab)

    # Export Options
    st.markdown('<div class="section-header">Export Options</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Save Progress"):
            st.success("Progress saved successfully!")
            
    with col2:
        if st.button("Export to Excel"):
            st.success("Export completed!")

if __name__ == "__main__":
    create_keyword_research_app()
