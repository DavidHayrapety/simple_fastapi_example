from enum import Enum
from pydantic import BaseModel


class SpecialPage(str, Enum):
    about = "about"
    contact = "contact"
    career = "career"


class User(BaseModel):
    id: int = None
    name: str 
    email: str


class Product(BaseModel):
    
    id: int = None
    name: str
    size: int
    price: float


class Store(BaseModel):
    
    id: int = None
    address: str
    capacity: int = 200
    # products: dict[Product, int]
