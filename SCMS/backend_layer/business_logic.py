from database_layer.orm import Session
from backend_layer.data_models import CrewMember, Ship, DispositionSchedule
from datetime import datetime

def load_ship_schedules(ship_name, month):
    session = Session()
    ship = session.query(Ship).filter_by(ship_name=ship_name).first()
    if not ship:
        print(f"No ship found with name {ship_name}")
        return None
    schedules = session.query(DispositionSchedule).filter_by(ship_id=ship.ship_id).all()
    month_schedules = [schedule for schedule in schedules if schedule.date.month == month]
    session.close()
    return month_schedules

def check_availability(crew_member, date):
    if crew_member.contract_end_date < date or crew_member.on_vacation:
        return False
    return True

def assign_crew_member_to_ship(crew_member_id, ship_id, position):
    session = Session()
    crew_member = session.query(CrewMember).filter_by(crew_id=crew_member_id).first()
    ship = session.query(Ship).filter_by(ship_id=ship_id).first()
    if not crew_member or not ship:
        print("Invalid crew member or ship id")
        return None
    if not check_availability(crew_member, datetime.now()):
        print(f"Crew member {crew_member.crew_name} is not available")
        return None
    crew_member.ship_id = ship.ship_id
    crew_member.position = position
    session.commit()
    session.close()
    print(f"Crew member {crew_member.crew_name} assigned to ship {ship.ship_name} at position {position}")
    return crew_member