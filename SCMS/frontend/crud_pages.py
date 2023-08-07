import streamlit as st
from backend_layer.crud_operations import create_crew_member, update_crew_member, delete_crew_member, get_crew_member

def display_crud_pages():
    st.title("CRUD Operations")

    # Create
    st.subheader("Create Crew Member")
    crew_id = st.text_input("Enter Crew ID")
    crew_name = st.text_input("Enter Crew Name")
    if st.button("Create"):
        create_crew_member(crew_id, crew_name)
        st.success(f"Crew Member {crew_name} created successfully")

    # Read
    st.subheader("Read Crew Member")
    read_crew_id = st.text_input("Enter Crew ID to Read")
    if st.button("Read"):
        crew_member = get_crew_member(read_crew_id)
        st.write(crew_member)

    # Update
    st.subheader("Update Crew Member")
    update_crew_id = st.text_input("Enter Crew ID to Update")
    new_crew_name = st.text_input("Enter New Crew Name")
    if st.button("Update"):
        update_crew_member(update_crew_id, new_crew_name)
        st.success(f"Crew Member {update_crew_id} updated successfully")

    # Delete
    st.subheader("Delete Crew Member")
    delete_crew_id = st.text_input("Enter Crew ID to Delete")
    if st.button("Delete"):
        delete_crew_member(delete_crew_id)
        st.success(f"Crew Member {delete_crew_id} deleted successfully")