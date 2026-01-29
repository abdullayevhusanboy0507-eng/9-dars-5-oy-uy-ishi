from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI , Depends
import uvicorn

from database_9_dars_uy import Base ,  engine , get_db
from schemas_9_dars_uy import * 
import crud_uy 

app = FastAPI()

async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        
@app.on_event("startup")
async def startup_event():
    await init_db()
    
@app.post("/doctor",response_model=DoctorResponse)
async def create_doctor_end(doctor : DoctorCreate, db:AsyncSession = Depends(get_db)):
    return await crud_uy.create_doctor(doctor , db)

@app.get("/doctor",response_model=list[DoctorResponse])
async def reads(db:AsyncSession = Depends(get_db)):
    return await crud_uy.reads_doctor(db)

@app.get("/doctor/{doctor_id}",response_model=DoctorResponse)
async def read(doctor_id : int ,db:AsyncSession = Depends(get_db)):
    return await crud_uy.read_doctor(doctor_id , db)

@app.put("/doctor/{doctor_id}",response_model=DoctorResponse)
async def update(doctor_id : int, doctor : DoctorCreate ,db:AsyncSession = Depends(get_db)):
    return await crud_uy.update_doctor(doctor_id, doctor , db)

@app.delete("/doctor/{doctor_id}",response_model=dict)
async def delete(doctor_id : int ,db:AsyncSession = Depends(get_db)):
    return await crud_uy.delete_doctor(doctor_id , db)


if __name__ == "__main__":
    uvicorn.run(app)