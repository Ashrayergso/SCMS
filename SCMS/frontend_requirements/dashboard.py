import streamlit as st
from frontend_layer import user_interactions

def main():
    st.title("Ship Crew Management System")
    st.sidebar.title("Navigation")
    pages = {
        "Crew Management": user_interactions.CrewManagementPage,
        "Ship Scheduling": user_interactions.ShipSchedulingPage,
        "Position and Qualification Management": user_interactions.PositionQualificationPage,
        "Data Management": user_interactions.DataManagementPage,
        "Data Analytics and Visualization": user_interactions.DataAnalyticsPage,
        "Security and Compliance": user_interactions.SecurityCompliancePage
    }

    choice = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[choice]
    page.app()

if __name__ == "__main__":
    main()