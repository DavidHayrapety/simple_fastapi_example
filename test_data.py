from schemas import *

users_data = [
    User(id=1, name="John Doe", email="john@doe.net"),
]
products_data = [
    Product(id=1, name="Rice", size=1, price=540.6),
    Product(id=2, name="Honey", size=3, price=1500.0)
]
stores_data = [
    Store(id=1, address='Kapan, Baxaberd 15', capacity=500, products={}),
    Store(id=2, address='Kapan, M. Stepanyan 18', capacity=1000, products={})
]
