from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    client: str
    film_type: str
    width: float
    thickness: float
    weight: float
    component1: float
    component2: float

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
