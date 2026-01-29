from pydantic import BaseModel


class DoctorCreate(BaseModel):
    full_name: str
    phone_number: str


class DoctorResponse(DoctorCreate):
    id: int

    class Config:
        from_attributes = True

class PatientCreate(BaseModel):
    full_name : str
    tashxis : str
    adres : str
    doctor_id : int
 
class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True
