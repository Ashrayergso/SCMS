from backend_layer.data_models import CrewMember, DispositionSchedule, TrainingRecord, ShipJobAmount, Ship, ShipPortSchedule, Port, Brand, JobCode, CrewTrainingRecord

def validate_crew_member(crew_member):
    assert isinstance(crew_member, CrewMember), "Invalid data type for crew member"
    assert crew_member.crew_id is not None, "Crew ID cannot be None"
    assert crew_member.crew_name is not None, "Crew name cannot be None"
    # Add more validation rules as needed

def validate_disposition_schedule(disposition_schedule):
    assert isinstance(disposition_schedule, DispositionSchedule), "Invalid data type for disposition schedule"
    assert disposition_schedule.id is not None, "ID cannot be None"
    assert disposition_schedule.crew_id is not None, "Crew ID cannot be None"
    assert disposition_schedule.ship_code is not None, "Ship code cannot be None"
    # Add more validation rules as needed

def validate_training_record(training_record):
    assert isinstance(training_record, TrainingRecord), "Invalid data type for training record"
    assert training_record.training_id is not None, "Training ID cannot be None"
    assert training_record.training_name is not None, "Training name cannot be None"
    # Add more validation rules as needed

# Add similar validation functions for ShipJobAmount, Ship, ShipPortSchedule, Port, Brand, JobCode, CrewTrainingRecord