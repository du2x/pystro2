from dataclasses import dataclass
from .exceptions import AddedInactiveItem, InvalidItemForOrder
from typing import Set


@dataclass(frozen=True)
class User:
    name: int
    email: str

@dataclass(frozen=True)
class Address:
    street: str
    number: str
    complement: str
    cep: str
    user_id: int
    restaurant_id: int

@dataclass(frozen=True)
class Product:
    id: int
    name: str
    picture: str
    restaurant_id: int
    price: float
    active: bool

@dataclass(frozen=True)
class OrderItem:
    order_id: int
    product_id: int
    qty: int
    obs: str

@dataclass(frozen=True)
class Restaurant:
    name: int
    address: str
    qty: int
    obs: str


class Order:
  
    def __init__(self, id: int, restaurant_id: int, user_id: int):
        self.id = id
        self.restaurant_id = restaurant_id
        self._status = 0
        self._items = set()  # type: set[OrderItem]

    def __repr__(self):
        return f'<Order {self.id}>'

    def add_item(self, item: OrderItem):
        if not item.product.id == self.restaurantid:
            raise InvalidItemForOrder()
        if not item.product.active:
            raise AddedInactiveItem()
        self._items.add(item)                    

    @property
    def price(self) -> float:
        return sum(item.qty * item.product.price for item in self._items)
