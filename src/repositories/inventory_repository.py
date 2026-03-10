products = []

def save_product(product):

    products.append(product)

    return product


def get_products():

    return products


def find_product(product_id):

    for product in products:
        if product.product_id == product_id:
            return product

    return None