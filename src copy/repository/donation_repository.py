from sqlalchemy.orm import Session
from sqlalchemy import and_
from src.models.donation_model import Donation
from src.schema.donation_schema import DonationCreate, DonationUpdate
from datetime import datetime

def get_donations(db: Session, skip: int = 0, limit: int = 10,
                  donor_name: str = None, donation_type: str = None,
                  start_date: str = None, end_date: str = None):
    query = db.query(Donation)

    if donor_name:
        query = query.filter(Donation.donor_name.ilike(f"%{donor_name}%"))
    if donation_type:
        query = query.filter(Donation.donation_type.ilike(f"%{donation_type}%"))
    if start_date and end_date:
        query = query.filter(
            and_(Donation.date >= datetime.fromisoformat(start_date),
                 Donation.date <= datetime.fromisoformat(end_date))
        )

    return query.offset(skip).limit(limit).all()

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
