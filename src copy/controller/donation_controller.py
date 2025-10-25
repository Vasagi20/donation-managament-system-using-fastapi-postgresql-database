from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.database import get_db
from src.models.donation_model import Donation
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/donations", tags=["Donations"])

# --- Schema ---
class DonationSchema(BaseModel):
    donor_name: str
    donation_type: str
    amount: float
    remarks: str | None = None

    class Config:
        from_attributes = True


# --- Get all donations ---
@router.get("/", response_model=List[DonationSchema])
def get_donations(db: Session = Depends(get_db)):
    donations = db.query(Donation).all()
    return donations


# --- Add donation ---
@router.post("/", response_model=DonationSchema)
def add_donation(donation: DonationSchema, db: Session = Depends(get_db)):
    new_donation = Donation(
        donor_name=donation.donor_name,
        donation_type=donation.donation_type,
        amount=donation.amount,
        remarks=donation.remarks
    )
    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)
    return new_donation
