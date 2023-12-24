from enum import Enum
from pydantic import BaseModel


class SpecialPage(str, Enum):
    about = "about"
    contact = "contact"
    career = "career"


class User(BaseModel):
    id: int = None
    name: str = None
    email: str = None


class Product(BaseModel):

    id: int = None
    name: str = None
    size: int = None
    price: float = None


class Store(BaseModel):

    id: int = None
    address: str = None
    capacity: int = 200
    products: dict[Product, int] = {}
