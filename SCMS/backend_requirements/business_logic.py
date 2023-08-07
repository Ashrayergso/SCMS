from backend_layer.data_models import CrewMember, ShipSchedule
from backend_layer.crud_operations import get_all, update
from datetime import datetime

def filter_crew_members(availability_status):
    """
    Function to filter crew members based on their availability status.
    """
    crew_members = get_all(CrewMember)
    available_crew_members = [crew_member for crew_member in crew_members if crew_member.availability_status == availability_status]
    return available_crew_members

def manage_ship_schedules(ship_name, month):
    """
    Function to manage ship schedules based on ship name and month.
    """
    ship_schedules = get_all(ShipSchedule)
    filtered_schedules = [schedule for schedule in ship_schedules if schedule.ship_name == ship_name and schedule.month == month]
    return filtered_schedules

def assign_crew_member_to_ship(crew_member_id, ship_id):
    """
    Function to assign a crew member to a specific ship.
    """
    crew_member = get_all(CrewMember, filters={"id": crew_member_id})[0]
    if crew_member.availability_status == "Available":
        crew_member.ship_id = ship_id
        crew_member.availability_status = "Assigned"
        update(crew_member)
        return True
    else:
        return False

def check_crew_member_availability(crew_member_id):
    """
    Function to check the availability of a crew member.
    """
    crew_member = get_all(CrewMember, filters={"id": crew_member_id})[0]
    return crew_member.availability_status == "Available"

def check_ship_schedule(ship_id, date):
    """
    Function to check the schedule of a ship.
    """
    ship_schedules = get_all(ShipSchedule, filters={"ship_id": ship_id})
    for schedule in ship_schedules:
        if datetime.strptime(schedule.date, '%Y-%m-%d').date() == date:
            return True
    return False