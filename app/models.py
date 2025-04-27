from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    orders = relationship("Order", back_populates="owner")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client = Column(String, nullable=False)
    film_type = Column(String, nullable=False)
    width = Column(Float, nullable=False)
    thickness = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    component1 = Column(Float, nullable=False)
    component2 = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="orders")
