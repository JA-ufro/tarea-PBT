import pytest

from tarea_pbt import InvalidProductError, ProductNotFoundError, ProductRepository


def test_create_assigns_an_id_and_read_returns_the_product() -> None:
    repository = ProductRepository()

    created = repository.create("keyboard", 25000)

    assert created.id == 1
    assert repository.get(created.id) == created


def test_update_changes_values_but_preserves_identity() -> None:
    repository = ProductRepository()
    created = repository.create("keyboard", 25000)

    updated = repository.update(created.id, "mechanical keyboard", 45000)

    assert updated.id == created.id
    assert updated.name == "mechanical keyboard"
    assert updated.price == 45000
    assert repository.get(created.id) == updated


def test_delete_removes_the_product() -> None:
    repository = ProductRepository()
    created = repository.create("keyboard", 25000)

    repository.delete(created.id)

    assert repository.get(created.id) is None


def test_get_missing_product_returns_none() -> None:
    assert ProductRepository().get(999) is None


@pytest.mark.parametrize("operation", ["update", "delete"])
def test_mutating_a_missing_product_raises(operation: str) -> None:
    repository = ProductRepository()

    with pytest.raises(ProductNotFoundError):
        if operation == "update":
            repository.update(999, "missing", 1)
        else:
            repository.delete(999)


@pytest.mark.parametrize("price", [-1, True])
def test_invalid_prices_are_rejected(price: object) -> None:
    with pytest.raises(InvalidProductError):
        ProductRepository().create("invalid", price)  # type: ignore[arg-type]
