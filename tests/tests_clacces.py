from src.category import Category
from src.product import Product


def test_product_creation() -> None:
    product = Product("Radiance", "Damage Aura", 4700.0, 5)
    assert product.name == "Radiance"
    assert product.description == "Damage Aura"
    assert product.price == 4700.0
    assert product.quantity == 5


def test_price_setter_getter() -> None:
    product = Product("Desolator", "+50 damage count", 3500.0, 8)
    product.price = 3500.0
    assert product.price == 3500.0
    product.price = -100
    assert product.price == 3500.0


def test_category_creation() -> None:
    category = Category("Предметы", "Лучший пик на Wraith King в 2024 году", [])
    assert category.name == "Предметы"
    assert category.description == "Лучший пик на Wraith King в 2024 году"
    assert len(category.products) == 0


def test_add_product_to_category() -> None:
    category = Category("Смартфоны", "Лучшие смартфоны 2023 года", [])
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


if __name__ == "__main__":
    test_product_creation()
    test_price_setter_getter()
    test_category_creation()
    test_add_product_to_category()

