from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import *
from schemas import *
from auth import get_current_user

router = APIRouter()

