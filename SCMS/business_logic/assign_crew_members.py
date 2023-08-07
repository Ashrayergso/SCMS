from backend_layer.data_models import Crew, Ship, Assignment
from backend_layer.crud_operations import get_all, add_record, update_record
from backend_layer.pandas_integration import filter_by_availability, filter_by_qualification

def assign_crew_members():
    # Get all available crew members
    available_crew = get_all(Crew)
    available_crew = filter_by_availability(available_crew)

    # Get all ships
    ships = get_all(Ship)

    for ship in ships:
        # Get required positions for the ship
        required_positions = ship.required_positions

        for position in required_positions:
            # Filter crew members by required qualifications for the position
            qualified_crew = filter_by_qualification(available_crew, position.required_qualifications)

            if qualified_crew:
                # Assign the first available and qualified crew member to the position
                crew_member = qualified_crew[0]

                # Create a new assignment
                assignment = Assignment(ship_id=ship.id, crew_id=crew_member.id, position_id=position.id)

                # Add the assignment to the database
                add_record(assignment)

                # Update the crew member's status to 'assigned'
                crew_member.status = 'assigned'
                update_record(crew_member)

                # Remove the assigned crew member from the available crew list
                available_crew.remove(crew_member)

            else:
                print(f"No available and qualified crew members for position {position.name} on ship {ship.name}")