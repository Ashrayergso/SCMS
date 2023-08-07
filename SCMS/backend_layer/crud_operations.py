from sqlalchemy.orm import Session
from . import models, schemas

def get_crew(db: Session, crew_id: int):
    return db.query(models.Crew).filter(models.Crew.id == crew_id).first()

def get_crews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Crew).offset(skip).limit(limit).all()

def create_crew(db: Session, crew: schemas.CrewCreate):
    db_crew = models.Crew(**crew.dict())
    db.add(db_crew)
    db.commit()
    db.refresh(db_crew)
    return db_crew

def update_crew(db: Session, crew: schemas.CrewUpdate):
    db_crew = db.query(models.Crew).filter(models.Crew.id == crew.id).first()
    if db_crew is None:
        return None
    for var, value in vars(crew).items():
        setattr(db_crew, var, value) if value else None
    db.add(db_crew)
    db.commit()
    db.refresh(db_crew)
    return db_crew

def delete_crew(db: Session, crew_id: int):
    db_crew = db.query(models.Crew).filter(models.Crew.id == crew_id).first()
    if db_crew is None:
        return None
    db.delete(db_crew)
    db.commit()
    return db_crew