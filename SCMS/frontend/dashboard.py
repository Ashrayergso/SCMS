import streamlit as st
from frontend_layer import user_interactions, crew_management_page, crud_pages

def main():
    st.title("Ship Crew Management System")

    menu = ["Home", "Crew Management", "CRUD Operations"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Ship Crew Management System (SCMS). Please navigate using the sidebar.")
    elif choice == "Crew Management":
        crew_management_page.display()
    elif choice == "CRUD Operations":
        crud_pages.display()

if __name__ == "__main__":
    main()