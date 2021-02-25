from src.domain.exceptions import AddedInactiveItem
from src.domain.model import Product, Order, OrderItem, InvalidItemForOrder
from pytest import raises

A_USER_ID = 1
A_RESTAURANT_ID = 1
OTHER_RESTAURANT_ID = 2

def test_cannot_add_product_from_other_restaurant():
    product = Product(1, "banana", "banana.png", A_RESTAURANT_ID, 10, True)
    item = OrderItem(1, product, 1, "")
    order = Order(1, OTHER_RESTAURANT_ID, A_USER_ID)
    with raises(InvalidItemForOrder):
        order.add_item(item)

def test_cannot_add_inactive_product_to_order():
    product = Product(1, "banana", "banana.png", A_RESTAURANT_ID, 10, False)
    item = OrderItem(1, product, 1, "")
    order = Order(1, A_RESTAURANT_ID, A_USER_ID)
    with raises(AddedInactiveItem):
        order.add_item(item)

def test_sucessful_add_item_to_order():
    product = Product(1, "banana", "banana.png", A_RESTAURANT_ID, 10, True)
    item = OrderItem(1, product, 1, "")
    order = Order(1, A_RESTAURANT_ID, A_USER_ID)
    order.add_item(item)
    assert order.price == product.price
