from typing import Any


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        return self.price + self.quantity + other.price * other.quantity

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, price: Any) -> None:
        if price > 0:
            self.__price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, parameters: Any) -> Any:
        n_product = cls(
            parameters["name"],
            parameters["description"],
            parameters["price"],
            parameters["quantity"],
        )
        return n_product
