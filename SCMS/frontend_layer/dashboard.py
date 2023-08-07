import streamlit as st
from frontend_layer import user_interactions

def main():
    st.title("Ship Crew Management System")

    menu = ["Home", "Crew Management", "Ship Scheduling", "Position and Qualification Management", "CRUD Operations", "Data Analytics and Visualization"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Ship Crew Management System (SCMS). Please navigate using the sidebar.")
    elif choice == "Crew Management":
        st.subheader("Crew Management")
        user_interactions.crew_management()
    elif choice == "Ship Scheduling":
        st.subheader("Ship Scheduling")
        user_interactions.ship_scheduling()
    elif choice == "Position and Qualification Management":
        st.subheader("Position and Qualification Management")
        user_interactions.position_qualification_management()
    elif choice == "CRUD Operations":
        st.subheader("CRUD Operations")
        user_interactions.crud_operations()
    elif choice == "Data Analytics and Visualization":
        st.subheader("Data Analytics and Visualization")
        user_interactions.data_analytics_visualization()

if __name__ == "__main__":
    main()