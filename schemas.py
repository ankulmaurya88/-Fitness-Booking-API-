
from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

    @validator("client_name")
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Client name cannot be blank")
        return v

