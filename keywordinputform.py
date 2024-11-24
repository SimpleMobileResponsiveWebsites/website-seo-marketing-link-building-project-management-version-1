import streamlit as st

def main():
    # Title of the application
    st.title("Keyword Input Form")

    # Create a form for user input
    with st.form(key='keyword_form'):
        keyword = st.text_input(label="Keyword")
        currency = st.selectbox(label="Currency", options=['USD', 'EUR', 'GBP', 'AUD', 'CAD'])
        avg_monthly_searches = st.number_input(label="Avg. Monthly Searches (exact match only)", min_value=0)
        competition = st.slider(label="Competition", min_value=0.0, max_value=1.0, step=0.1)
        suggested_bid = st.number_input(label="Suggested Bid", min_value=0.0, format="%.2f")
        impr_share = st.slider(label="Impr. Share (%)", min_value=0, max_value=100, step=1)
        organic_impr_share = st.slider(label="Organic Impr. Share (%)", min_value=0, max_value=100, step=1)
        organic_avg_position = st.number_input(label="Organic Avg. Position", min_value=1)  # Assuming positions start from 1
        in_account = st.radio("In account?", options=['Yes', 'No'])
        in_plan = st.radio("In plan?", options=['Yes', 'No'])
        title = st.text_input(label="Title")
        description = st.text_area(label="Description")

        submit_button = st.button(label="Submit")

        if submit_button:
            # Display the input data back to the user
            st.write("### Submitted Data")
            st.write(f"**Keyword:** {keyword}")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Avg. Monthly Searches:** {avg_monthly_searches}")
            st.write(f"**Competition:** {competition:.1f}")
            st.write(f"**Suggested Bid:** {suggested_bid:.2f}")
            st.write(f"**Impr. Share:** {impr_share}%")
            st.write(f"**Organic Impr. Share:** {organic_impr_share}%")
            st.write(f"**Organic Avg. Position:** {organic_avg_position}")
            st.write(f"**In Account?:** {in_account}")
            st.write(f"**In Plan?:** {in_plan}")
            st.write(f"**Title:** {title}")
            st.write(f"**Description:** {description}")

if __name__ == "__main__":
    main()
