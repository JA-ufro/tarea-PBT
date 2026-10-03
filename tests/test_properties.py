from hypothesis import given, strategies as st

from tarea_pbt import ProductRepository


product_values = st.tuples(
    st.text(max_size=100),
    st.integers(min_value=0, max_value=1_000_000),
)


@given(product=product_values)
def test_create_then_read_returns_the_created_product(
    product: tuple[str, int],
) -> None:
    name, price = product
    repository = ProductRepository()

    created = repository.create(name, price)

    assert repository.get(created.id) == created


@given(product=product_values)
def test_reading_repeatedly_does_not_change_the_product(
    product: tuple[str, int],
) -> None:
    name, price = product
    repository = ProductRepository()
    created = repository.create(name, price)

    first_read = repository.get(created.id)
    second_read = repository.get(created.id)

    assert first_read == created
    assert second_read == first_read


@given(original=product_values, replacement=product_values)
def test_update_then_read_reflects_any_generated_replacement(
    original: tuple[str, int],
    replacement: tuple[str, int],
) -> None:
    repository = ProductRepository()
    created = repository.create(*original)

    updated = repository.update(created.id, *replacement)

    assert updated.id == created.id
    assert (updated.name, updated.price) == replacement
    assert repository.get(created.id) == updated


@given(product=product_values)
def test_delete_then_read_cannot_find_the_deleted_product(
    product: tuple[str, int],
) -> None:
    repository = ProductRepository()
    created = repository.create(*product)

    repository.delete(created.id)

    assert repository.get(created.id) is None
