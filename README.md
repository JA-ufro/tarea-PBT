# tarea-PBT

Implementacion de un CRUD en memoria para la entidad `Product`, validado con
Property-Based Testing.

## Objetivo

El proyecto practica la definicion de propiedades generales sobre una entidad
de dominio simple. No utiliza interfaz grafica, API ni base de datos.

## Entidad y CRUD

`Product` contiene `id`, `name` y `price`. `ProductRepository` ofrece:

- `create(name, price)`: crea un producto y asigna un ID unico.
- `get(product_id)`: obtiene el producto o devuelve `None` si no existe.
- `update(product_id, name, price)`: reemplaza los valores y conserva el ID.
- `delete(product_id)`: elimina el producto.

Actualizar o eliminar un ID inexistente genera `ProductNotFoundError`. El
precio debe ser un entero no negativo; de lo contrario se genera
`InvalidProductError`.

## Property-Based Testing

Las pruebas utilizan [Hypothesis](https://hypothesis.readthedocs.io/) para
generar automaticamente multiples entradas, incluidos textos Unicode, texto
vacio, cero y precios grandes. Cada prueba comienza con un repositorio nuevo,
por lo que no depende del orden de ejecucion.

## Propiedades probadas

### Create

Para cualquier nombre y precio validos generados, crear un producto y leer su
ID devuelve un producto equivalente al creado.

### Read

Leer repetidamente el ID de un producto creado devuelve el mismo valor y no
altera el producto almacenado.

### Update

Para cualquier producto y reemplazo generados, actualizar y leer el mismo ID
refleja los nuevos valores, manteniendo la identidad del producto.

### Delete

Para cualquier producto generado, despues de eliminarlo su ID deja de estar
disponible para lectura.

## Instalacion

Se requiere Python 3.10 o superior.

```text
python -m venv .venv
```

En Windows PowerShell:

```text
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

En macOS o Linux:

```text
source .venv/bin/activate
python -m pip install -e ".[test]"
```

## Ejecucion de pruebas

```text
python -m pytest
```

Las pruebas de ejemplo estan en `tests/test_crud.py` y las propiedades PBT en
`tests/test_properties.py`.
