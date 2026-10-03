from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    price: int


class ProductNotFoundError(LookupError):
    def __init__(self, product_id: int) -> None:
        super().__init__(f"Product {product_id} was not found")


class InvalidProductError(ValueError):
    pass


class ProductRepository:
    """Small in-memory CRUD repository for products."""

    def __init__(self) -> None:
        self._products: dict[int, Product] = {}
        self._next_id = 1

    def create(self, name: str, price: int) -> Product:
        self._validate_values(name, price)
        product = Product(id=self._next_id, name=name, price=price)
        self._products[product.id] = product
        self._next_id += 1
        return product

    def get(self, product_id: int) -> Product | None:
        return self._products.get(product_id)

    def update(self, product_id: int, name: str, price: int) -> Product:
        if product_id not in self._products:
            raise ProductNotFoundError(product_id)
        self._validate_values(name, price)
        updated_product = Product(id=product_id, name=name, price=price)
        self._products[product_id] = updated_product
        return updated_product

    def delete(self, product_id: int) -> None:
        if product_id not in self._products:
            raise ProductNotFoundError(product_id)
        del self._products[product_id]

    @staticmethod
    def _validate_values(name: str, price: int) -> None:
        if not isinstance(name, str):
            raise InvalidProductError("Product name must be a string")
        if isinstance(price, bool) or not isinstance(price, int) or price < 0:
            raise InvalidProductError("Product price must be a non-negative integer")
