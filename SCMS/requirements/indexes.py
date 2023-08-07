from sqlalchemy import create_engine, MetaData, Table, Index

# Create a connection to the database
engine = create_engine('sqlite:///scms.db')
metadata = MetaData()

# Load the tables
crew_members = Table('crew_members', metadata, autoload_with=engine)
disposition_schedule = Table('disposition_schedule', metadata, autoload_with=engine)
training_records = Table('training_records', metadata, autoload_with=engine)
ship_job_amounts = Table('ship_job_amounts', metadata, autoload_with=engine)
ships = Table('ships', metadata, autoload_with=engine)
ship_port_schedule = Table('ship_port_schedule', metadata, autoload_with=engine)
ports = Table('ports', metadata, autoload_with=engine)
brand = Table('brand', metadata, autoload_with=engine)
job_codes = Table('job_codes', metadata, autoload_with=engine)
crew_training_records = Table('crew_training_records', metadata, autoload_with=engine)

# Create indexes for performance optimization
Index('idx_crew_members_id', crew_members.columns.crew_id)
Index('idx_disposition_schedule_id', disposition_schedule.columns.id)
Index('idx_training_records_id', training_records.columns.training_id)
Index('idx_ship_job_amounts_key', ship_job_amounts.columns.ship_job_key)
Index('idx_ships_id', ships.columns.ship_id)
Index('idx_ship_port_schedule_id', ship_port_schedule.columns.id)
Index('idx_ports_id', ports.columns.id)
Index('idx_brand_id', brand.columns.id)
Index('idx_job_codes_id', job_codes.columns.id)
Index('idx_crew_training_records_id', crew_training_records.columns.id)

print("Indexes created successfully.")