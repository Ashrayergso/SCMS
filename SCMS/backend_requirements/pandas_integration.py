import pandas as pd
from backend_layer.data_models import CrewMembers, DispositionSchedule, TrainingRecords, ShipJobAmounts, Ships, ShipPortSchedule, Ports, Brand, JobCodes, CrewTrainingRecords

def load_data():
    # Load data from SQLite database into pandas DataFrame
    crew_members = pd.read_sql_query("SELECT * from CrewMembers", conn)
    disposition_schedule = pd.read_sql_query("SELECT * from DispositionSchedule", conn)
    training_records = pd.read_sql_query("SELECT * from TrainingRecords", conn)
    ship_job_amounts = pd.read_sql_query("SELECT * from ShipJobAmounts", conn)
    ships = pd.read_sql_query("SELECT * from Ships", conn)
    ship_port_schedule = pd.read_sql_query("SELECT * from ShipPortSchedule", conn)
    ports = pd.read_sql_query("SELECT * from Ports", conn)
    brand = pd.read_sql_query("SELECT * from Brand", conn)
    job_codes = pd.read_sql_query("SELECT * from JobCodes", conn)
    crew_training_records = pd.read_sql_query("SELECT * from CrewTrainingRecords", conn)

    return crew_members, disposition_schedule, training_records, ship_job_amounts, ships, ship_port_schedule, ports, brand, job_codes, crew_training_records

def analyze_data(crew_members, disposition_schedule, training_records, ship_job_amounts, ships, ship_port_schedule, ports, brand, job_codes, crew_training_records):
    # Perform data analysis using pandas
    # This is a placeholder function, actual analysis will depend on the specific requirements

    # Example: Find the average contract duration for each crew member
    avg_contract_duration = crew_members['contract_duration'].mean()

    # Example: Find the total number of ships each crew member has been assigned to
    total_ships_assigned = disposition_schedule.groupby('crew_id')['ship_code'].nunique()

    return avg_contract_duration, total_ships_assigned