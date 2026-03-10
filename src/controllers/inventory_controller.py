from src.services.inventory_service import create_product, list_products, update_stock


def create_product_endpoint(product_id, name, quantity):

    return create_product(product_id, name, quantity)


def list_products_endpoint():

    return list_products()


def update_stock_endpoint(product_id, quantity):

    return update_stock(product_id, quantity)