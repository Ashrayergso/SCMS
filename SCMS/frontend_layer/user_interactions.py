import streamlit as st
from backend_layer import crud_operations

def display_crew_member_form():
    st.subheader("Add New Crew Member")
    crew_name = st.text_input("Crew Name")
    crew_id = st.text_input("Crew ID")
    if st.button("Add Crew Member"):
        crud_operations.add_crew_member(crew_id, crew_name)
        st.success("Crew Member Added Successfully")

def display_ship_schedule_form():
    st.subheader("Add New Ship Schedule")
    ship_code = st.text_input("Ship Code")
    arrival_time = st.text_input("Arrival Time")
    departure_time = st.text_input("Departure Time")
    if st.button("Add Ship Schedule"):
        crud_operations.add_ship_schedule(ship_code, arrival_time, departure_time)
        st.success("Ship Schedule Added Successfully")

def display_assignment_form():
    st.subheader("Assign Crew Member to Ship")
    crew_id = st.text_input("Crew ID")
    ship_code = st.text_input("Ship Code")
    if st.button("Assign Crew Member"):
        crud_operations.assign_crew_member(crew_id, ship_code)
        st.success("Crew Member Assigned Successfully")

def display_crew_member_filter():
    st.subheader("Filter Crew Members")
    crew_name = st.text_input("Crew Name")
    if st.button("Filter"):
        crew_members = crud_operations.filter_crew_members(crew_name)
        st.write(crew_members)

def display_ship_schedule_filter():
    st.subheader("Filter Ship Schedules")
    ship_code = st.text_input("Ship Code")
    if st.button("Filter"):
        ship_schedules = crud_operations.filter_ship_schedules(ship_code)
        st.write(ship_schedules)

def user_interactions():
    st.sidebar.title("SCMS User Interactions")
    page = st.sidebar.selectbox("Choose a page", ["Crew Member Form", "Ship Schedule Form", "Assignment Form", "Crew Member Filter", "Ship Schedule Filter"])

    if page == "Crew Member Form":
        display_crew_member_form()
    elif page == "Ship Schedule Form":
        display_ship_schedule_form()
    elif page == "Assignment Form":
        display_assignment_form()
    elif page == "Crew Member Filter":
        display_crew_member_filter()
    elif page == "Ship Schedule Filter":
        display_ship_schedule_filter()

if __name__ == "__main__":
    user_interactions()