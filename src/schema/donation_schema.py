from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DonationBase(BaseModel):
    donor_name: str
    donation_type: str
    amount: float
    remarks: Optional[str] = None

class DonationCreate(DonationBase):
    pass

class DonationUpdate(BaseModel):
    donor_name: Optional[str]
    donation_type: Optional[str]
    amount: Optional[float]
    remarks: Optional[str]

class DonationResponse(DonationBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
