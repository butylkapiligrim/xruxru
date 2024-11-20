class Product:
from abc import ABC, abstractmethod
class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __add__(self, other):
        pass
class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))
    def __repr__(self):
        params = ', '.join(f'{a}={b!r}' for a, b in self.__dict__.items())
        return f'{self.__class__.__name__}({params})'
class Product(MixinLog, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
‎tests/test_classes.py
+7
-1
Original file line number	Diff line number	Diff line change
@@ -4,6 +4,7 @@
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.product import BaseProduct


@pytest.fixture
@@ -86,7 +87,7 @@ def test_add(product_iphone):
    product = Product.new_product(
        {"name": "name1", "description": "-", "price": 140, "quantity": 3}
    )
    assert product_iphone + product == 442
    assert product_iphone + product == 492


def test_init3(smartphone):
@@ -108,3 +109,8 @@ def test_init4(lawn_grass):
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "1 week"
    assert lawn_grass.color == "Green"
def test_abstract_class() -> None:
    with pytest.raises(TypeError):
        prod = BaseProduct()
