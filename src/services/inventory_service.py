from src.models.product import Product
from src.repositories.inventory_repository import save_product, get_products, find_product
from src.utils.validators import validate_product_name, validate_quantity


def create_product(product_id, name, quantity):

    validate_product_name(name)

    validate_quantity(quantity)

    product = Product(product_id, name, quantity)

    return save_product(product)


def list_products():

    return get_products()


def update_stock(product_id, quantity):

    product = find_product(product_id)

    if product is None:
        raise ValueError("Product not found")

    product.quantity += quantity

    return product