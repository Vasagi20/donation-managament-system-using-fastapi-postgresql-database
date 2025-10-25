from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from src.utils.database import Base

class Donation(Base):
    __tablename__ = "donate"

    id = Column(Integer, primary_key=True, index=True)
    donor_name = Column(String, nullable=False)
    donation_type = Column(String, nullable=False)  # e.g., Money / Food / Clothes
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    remarks = Column(String, nullable=True)
