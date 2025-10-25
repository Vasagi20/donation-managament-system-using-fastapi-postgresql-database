from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.database import get_db
from src.service import donation_service
from src.schema.donation_schema import DonationCreate, DonationUpdate, DonationResponse

router = APIRouter(prefix="/api/donations", tags=["Donations"])

@router.get("/", response_model=list[DonationResponse])
def list_donations(db: Session = Depends(get_db)):
    return donation_service.list_donations(db)

@router.get("/{donation_id}", response_model=DonationResponse)
def get_donation(donation_id: int, db: Session = Depends(get_db)):
    donation = donation_service.get_donation(db, donation_id)
    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")
    return donation

@router.post("/", response_model=DonationResponse)
def create_donation(donation: DonationCreate, db: Session = Depends(get_db)):
    return donation_service.add_donation(db, donation)

@router.put("/{donation_id}", response_model=DonationResponse)
def update_donation(donation_id: int, donation: DonationUpdate, db: Session = Depends(get_db)):
    updated = donation_service.modify_donation(db, donation_id, donation)
    if not updated:
        raise HTTPException(status_code=404, detail="Donation not found")
    return updated

@router.delete("/{donation_id}")
def delete_donation(donation_id: int, db: Session = Depends(get_db)):
    deleted = donation_service.remove_donation(db, donation_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Donation not found")
    return {"message": "Donation deleted successfully"}
