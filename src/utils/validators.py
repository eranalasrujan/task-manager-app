def validate_product_name(name):

    if not name:
        raise ValueError("Product name cannot be empty")


def validate_quantity(quantity):

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")