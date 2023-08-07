import streamlit as st
from backend_layer import data_models, crud_operations, business_logic
from frontend_layer import dashboard, user_interactions

def main():
    st.title("Ship Crew Management System")

    menu = ["Dashboard", "Crew Management", "Ship Scheduling", "Position and Qualification Management", "Data Analytics and Visualization"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Dashboard":
        dashboard.show_dashboard()
    elif choice == "Crew Management":
        user_interactions.crew_management()
    elif choice == "Ship Scheduling":
        user_interactions.ship_scheduling()
    elif choice == "Position and Qualification Management":
        user_interactions.position_qualification_management()
    elif choice == "Data Analytics and Visualization":
        user_interactions.data_analytics_visualization()

if __name__ == "__main__":
    main()