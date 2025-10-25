from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.database import Base, engine
from src.controller import donation_controller  # ✅ make sure this import works
from pydantic import BaseModel

class MyModel(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Donation Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register your router here
app.include_router(donation_controller.router)

@app.get("/")
def root():
    return {"message": "Donation Management System API running successfully!"}
