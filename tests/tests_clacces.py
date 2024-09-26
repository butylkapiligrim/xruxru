import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def test_product() -> Product:
    return Product("Radiance", "фарм", 5200.0, 3)


def test_init(test_product: Product) -> None:
    assert test_product.name == "Radiance"
    assert test_product.description == "фарм"
    assert test_product.price == 4700.0
    assert test_product.quantity == 3


@pytest.fixture()
def test_category() -> Category:
    return Category("предметы", "антимаг", [1, 2, 3])


def test_init2(test_category: Category) -> None:
    assert test_category.name == "предметы"
    assert test_category.description == "антимаг"
    assert test_category.products == [1, 2, 3]
