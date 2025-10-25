from sqlalchemy.orm import Session
from src.models.donation_model import Donation
from src.schema.donation_schema import DonationCreate, DonationUpdate

def get_all_donations(db: Session):
    return db.query(Donation).all()

def get_donation_by_id(db: Session, donation_id: int):
    return db.query(Donation).filter(Donation.id == donation_id).first()

def create_donation(db: Session, donation: DonationCreate):
    new_donation = Donation(**donation.dict())
    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)
    return new_donation

def update_donation(db: Session, donation_id: int, donation_data: DonationUpdate):
    db_donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not db_donation:
        return None
    for key, value in donation_data.dict(exclude_unset=True).items():
        setattr(db_donation, key, value)
    db.commit()
    db.refresh(db_donation)
    return db_donation

def delete_donation(db: Session, donation_id: int):
    db_donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not db_donation:
        return None
    db.delete(db_donation)
    db.commit()
    return db_donation
