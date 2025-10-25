from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.database import Base, engine
from src.controller import donation_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Donation Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(donation_controller.router)

@app.get("/")
def root():
    return {"message": "🎁 Donation Management API running successfully!"}
