import streamlit as st
from backend_layer.crud_operations import create_crew_member, update_crew_member, delete_crew_member, get_crew_member

def create_crew_member_interface():
    st.subheader("Create Crew Member")
    crew_id = st.text_input("Crew ID")
    crew_name = st.text_input("Crew Name")
    if st.button("Create"):
        create_crew_member(crew_id, crew_name)
        st.success("Crew Member Created Successfully")

def update_crew_member_interface():
    st.subheader("Update Crew Member")
    crew_id = st.text_input("Crew ID")
    crew_name = st.text_input("New Crew Name")
    if st.button("Update"):
        update_crew_member(crew_id, crew_name)
        st.success("Crew Member Updated Successfully")

def delete_crew_member_interface():
    st.subheader("Delete Crew Member")
    crew_id = st.text_input("Crew ID")
    if st.button("Delete"):
        delete_crew_member(crew_id)
        st.success("Crew Member Deleted Successfully")

def get_crew_member_interface():
    st.subheader("Get Crew Member Details")
    crew_id = st.text_input("Crew ID")
    if st.button("Get Details"):
        crew_member = get_crew_member(crew_id)
        st.write(crew_member)