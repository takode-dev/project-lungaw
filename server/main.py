from fastapi import FastAPI

description: str = """
# Project Lung-aw - Fitness Tracker

## Health/Fitness Tracker
### Features
* Sleep Quality Tracker
* Daily Weight Tracker
* Water Intake Tracker
* Daily Goals
* Workout Tracker
* Caloric Intake Tracker
* Protein Intake Tracker
* Pedometer
* Stress Rate Tracker
* Fatigue Rate Tracker
* Hunger Rate Tracker

## Users
To be planned

## Authentication
To be planned
"""

contact: dict[str, str] = {
    "name": "notjl",
    "url": "https://github.com/notjl",
    "email": "takode@proton.me",
}

license_info: dict[str, str] = {
    "name": "Expat License (MIT)",
    "url": "https://mit-license.org/",
}

app: FastAPI = FastAPI(
    title="Project Lung-aw Server",
    version="AdamantInkling 0.1",
    description=description,
    contact=contact,
    license_info=license_info,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
