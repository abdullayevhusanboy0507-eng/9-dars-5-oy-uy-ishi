from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from models_9_dars_uy import *
from schemas_9_dars_uy import * 

async def create_doctor(doctor : DoctorCreate , db : AsyncSession) -> DoctorResponse:
    db_doctor = Doctor(**doctor.model_dump())
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return DoctorResponse.model_validate(db_doctor)
    
async def reads_doctor(db : AsyncSession) -> list[DoctorResponse]:
    db_doctor = await db.execute(select(Doctor))
    return [DoctorResponse.model_validate(Doctor) for doctor in db_doctor.scalars().all()]

async def read_doctor(doctor_id : int , db: AsyncSession) -> DoctorResponse:
    db_doctor = await db.get(Doctor, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404 , detail="Doctor not faund")
    return DoctorResponse.model_validate(db_doctor)

async def update_doctor(doctor_id : int , doctor : DoctorCreate , db:AsyncSession) -> DoctorResponse:
    db_doctor = await db.get(Doctor, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404 , detail="Doctor not faund")
    for key , value in doctor:
        setattr(db_doctor , key , value)
    
    await db.commit()
    await db.refresh(db_doctor)
    return DoctorResponse.model_validate(db_doctor)

async def delete_doctor(doctor_id : int , db : AsyncSession) -> dict:
    db_doctor = await db.get(Doctor, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404 , detail="Doctor not faund")
    
    await db.delete(db_doctor)
    await db.commit()
    return {"message": "Doctor deleted successful"}