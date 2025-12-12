from fastapi import APIRouter
from app.dependencies import get_db, oauth2_scheme
from app.utils import get_password_hash, create_access_token
from app.schemas import Token, TokenData
from app.models import User, Data

router = APIRouter()

@router.post("/api/register")
async def register(username: str, email: str, password: str, db: SessionLocal = Depends(get_db)):
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/api/login")
async def login(username: str, password: str, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/api/data")
async def get_data(db: SessionLocal = Depends(get_db)):
    data = db.query(Data).all()
    return data

@router.post("/api/data")
async def create_data(name: str, db: SessionLocal = Depends(get_db)):
    data = Data(name=name)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@router.get("/api/data/{id}")
async def get_data_by_id(id: int, db: SessionLocal = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.put("/api/data/{id}")
async def update_data(id: int, name: str, db: SessionLocal = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    data.name = name
    db.commit()
    db.refresh(data)
    return data

@router.delete("/api/data/{id}")
async def delete_data(id: int, db: SessionLocal = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    db.delete(data)
    db.commit()
    return {"message": "Data deleted successfully"}
