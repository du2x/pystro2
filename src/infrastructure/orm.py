from sqlalchemy import MetaData
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, SmallInteger, String

from src.domain.model import Order, OrderItem, Product, Restaurant, User, Address


metadata = MetaData()

order = Table(
    'orders', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('restaurant_id', Integer, nullable=False),
    Column('user_id', Integer, nullable=False),    
    Column('status', Integer, default=0)    
)

restaurant = Table(
    'restaurants', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
)

user = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('email', String(255)),
)

address =  Table(
    'address', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('street', String(255)),
    Column('complement', String(255)),
    Column('number', String(255)),    
)

product =  Table(
    'products', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('picture', String(255)),
    Column('numberprice', Float),    
    Column('active', SmallInteger),    
)


order_item = Table(
    'order_items', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('order_id', Integer),
    Column('product_id', Integer),
    Column('qty', Integer),    
    Column('obs', String(255)),    
)


def start_mappers():
    order_mapper = mapper(Order, order)
    order_item_mapper = mapper(OrderItem, order_item)
    user_mapper = mapper(User, user)
    product_mapper = mapper(Product, product)
    restaurant_mapper = mapper(Restaurant, restaurant)
    address_mapper = mapper(Address, address)