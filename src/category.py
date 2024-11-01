from typing import Any


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name: Any, description: Any, products: Any) -> None:
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = len(self.__products)
        Category.category_count += 1

    def add_product(self, product: Any) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def productss(self) -> str:
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product._price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_list)
