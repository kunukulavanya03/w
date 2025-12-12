from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from jose import jwt, JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/register")
async def register(username: str, email: str, password: str, db: SessionLocal = Depends(get_db)):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, email=email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/api/login")
async def login(username: str, password: str, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = jwt.encode({"sub": user.username}, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/data")
async def get_data(db: SessionLocal = Depends(get_db)):
    data = db.query(Data).all()
    return data

@app.post("/api/data")
async def create_data(name: str, db: SessionLocal = Depends(get_db)):
    data = Data(name=name)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@app.get("/api/data/{id}")
async def get_data_by_id(id: int, db: SessionLocal = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@app.put("/api/data/{id}")
async def update_data(id: int, name: str, db: SessionLocal = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    data.name = name
    db.commit()
    db.refresh(data)
    return data

@app.delete("/api/data/{id}")
async def delete_data(id: int, db: SessionLocal = Depends(get_db)):
    data = db.query(Data).filter(Data.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    db.delete(data)
    db.commit()
    return {"message": "Data deleted successfully"}

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)
