import streamlit as st
from backend_layer import crud_operations

def crew_management_page():
    st.title("Crew Management Page")

    # Fetching all crew members
    crew_members = crud_operations.get_all_crew_members()

    # Displaying crew members in a table
    st.write(crew_members)

    # Form to add a new crew member
    with st.form(key='add_crew_form'):
        st.header("Add a new crew member")
        crew_name = st.text_input(label='Enter crew member name')
        crew_id = st.text_input(label='Enter crew member ID')
        submit_button = st.form_submit_button(label='Add Crew Member')

        if submit_button:
            # Add the new crew member
            crud_operations.add_crew_member(crew_id, crew_name)
            st.success(f"Crew member {crew_name} added successfully!")

    # Form to remove a crew member
    with st.form(key='remove_crew_form'):
        st.header("Remove a crew member")
        crew_id = st.text_input(label='Enter crew member ID')
        submit_button = st.form_submit_button(label='Remove Crew Member')

        if submit_button:
            # Remove the crew member
            crud_operations.remove_crew_member(crew_id)
            st.success(f"Crew member with ID {crew_id} removed successfully!")

    # Form to update a crew member
    with st.form(key='update_crew_form'):
        st.header("Update a crew member")
        crew_id = st.text_input(label='Enter crew member ID')
        new_crew_name = st.text_input(label='Enter new crew member name')
        submit_button = st.form_submit_button(label='Update Crew Member')

        if submit_button:
            # Update the crew member
            crud_operations.update_crew_member(crew_id, new_crew_name)
            st.success(f"Crew member with ID {crew_id} updated successfully!")