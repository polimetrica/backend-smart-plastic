from app import auth
from sqlalchemy.orm import Session
from app import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        client=order.client,
        film_type=order.film_type,
        width=order.width,
        thickness=order.thickness,
        weight=order.weight,
        component1=order.component1,
        component2=order.component2,
        owner_id=None
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()
