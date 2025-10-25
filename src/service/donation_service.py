from sqlalchemy.orm import Session
from src.repository import donation_repository
from src.schema.donation_schema import DonationCreate, DonationUpdate

def list_donations(db: Session):
    return donation_repository.get_all_donations(db)

def get_donation(db: Session, donation_id: int):
    return donation_repository.get_donation_by_id(db, donation_id)

def add_donation(db: Session, donation: DonationCreate):
    return donation_repository.create_donation(db, donation)

def modify_donation(db: Session, donation_id: int, donation: DonationUpdate):
    return donation_repository.update_donation(db, donation_id, donation)

def remove_donation(db: Session, donation_id: int):
    return donation_repository.delete_donation(db, donation_id)
