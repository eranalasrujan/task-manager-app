from src.services.inventory_service import create_product


def test_create_product():

    product = create_product(1, "Keyboard", 10)

    assert product.name == "Keyboard"
    assert product.quantity == 10