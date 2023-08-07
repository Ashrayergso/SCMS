import sqlite3

def create_tables():
    conn = sqlite3.connect('SCMS.db')
    c = conn.cursor()

    # Create table - Crew Members
    c.execute('''CREATE TABLE Crew_Members
                 (crew_id INTEGER PRIMARY KEY, crew_name TEXT)''')

    # Create table - Disposition Schedule
    c.execute('''CREATE TABLE Disposition_Schedule
                 (id INTEGER PRIMARY KEY, crew_id INTEGER, ship_code TEXT)''')

    # Create table - Training Records
    c.execute('''CREATE TABLE Training_Records
                 (training_id INTEGER PRIMARY KEY, training_name TEXT)''')

    # Create table - Ship Job Amounts
    c.execute('''CREATE TABLE Ship_Job_Amounts
                 (ship_job_key INTEGER PRIMARY KEY, ship_code TEXT)''')

    # Create table - Ships
    c.execute('''CREATE TABLE Ships
                 (ship_id INTEGER PRIMARY KEY, ship_name TEXT)''')

    # Create table - Ship Port Schedule
    c.execute('''CREATE TABLE Ship_Port_Schedule
                 (id INTEGER PRIMARY KEY, ship_code TEXT)''')

    # Create table - Ports
    c.execute('''CREATE TABLE Ports
                 (id INTEGER PRIMARY KEY, port_code TEXT)''')

    # Create table - Brand
    c.execute('''CREATE TABLE Brand
                 (id INTEGER PRIMARY KEY, brand_name TEXT)''')

    # Create table - Job Codes
    c.execute('''CREATE TABLE Job_Codes
                 (id INTEGER PRIMARY KEY, job_code TEXT)''')

    # Create table - Crew Training Records
    c.execute('''CREATE TABLE Crew_Training_Records
                 (id INTEGER PRIMARY KEY, crew_id INTEGER)''')

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

create_tables()