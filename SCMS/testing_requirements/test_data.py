import random
import pandas as pd
from faker import Faker

# Instantiate Faker
fake = Faker()

# Function to generate fake data for Crew Members
def generate_crew_members(n):
    data = {
        "crew_id": [fake.unique.random_number(digits=5) for _ in range(n)],
        "crew_name": [fake.name() for _ in range(n)],
        # Add more fields as per the schema
    }
    return pd.DataFrame(data)

# Function to generate fake data for Disposition Schedule
def generate_disposition_schedule(n):
    data = {
        "id": [fake.unique.random_number(digits=5) for _ in range(n)],
        "crew_id": [fake.random_number(digits=5) for _ in range(n)],
        "ship_code": [fake.random_number(digits=5) for _ in range(n)],
        # Add more fields as per the schema
    }
    return pd.DataFrame(data)

# Function to generate fake data for Training Records
def generate_training_records(n):
    data = {
        "training_id": [fake.unique.random_number(digits=5) for _ in range(n)],
        "training_name": [fake.catch_phrase() for _ in range(n)],
        # Add more fields as per the schema
    }
    return pd.DataFrame(data)

# Add similar functions for other tables

# Function to generate test data
def generate_test_data(n):
    crew_members = generate_crew_members(n)
    disposition_schedule = generate_disposition_schedule(n)
    training_records = generate_training_records(n)
    # Generate data for other tables

    return {
        "crew_members": crew_members,
        "disposition_schedule": disposition_schedule,
        "training_records": training_records,
        # Return data for other tables
    }