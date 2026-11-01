# Requisito: Detalle de producto (Nombre y Descripción)

## ID del Requisito
REQ-DETAIL-01

## Descripción
Cuando el usuario selecciona un producto desde el catálogo, el sistema debe mostrar la vista de detalle de ese mismo producto, con su nombre y su descripción.

## Criterios de Aceptación
1. Al seleccionar el nombre de un producto en el catálogo, el sistema muestra la vista de detalle del producto.
2. El nombre mostrado en el detalle es igual al nombre del producto seleccionado en el catálogo.
3. La descripción mostrada en el detalle es igual a la descripción del producto seleccionado en el catálogo.
4. La descripción mostrada no está vacía.

## Precondiciones
- Sesión iniciada con `standard_user` / `secret_sauce`.
- El usuario se encuentra en la página del catálogo.

## Datos de entrada
- Al menos dos productos distintos del catálogo (por ejemplo, "Sauce Labs Backpack" y "Sauce Labs Bike Light").

## Prioridad
P1 (Alta)

**Justificación:** si el nombre o la descripción fallan, el usuario puede seguir iniciando sesión y completando una compra, por lo que no es P0. Sin embargo, mostrar información incorrecta del producto afecta la confianza del usuario y puede llevarlo a comprar algo distinto a lo que esperaba (ver 3.7 del Test Plan: "se muestra información incorrecta, pero se puede seguir comprando").

## Tipo de prueba
Funcional / Detalle de producto

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- Escenarios: SC-DETAIL-xxx (pendiente de definir)


# Requisito: Detalle de producto (precio)

## ID del Requisito
REQ-DETAIL-02

## Descripción
Cuando el usuario selecciona un producto desde el catálogo, el sistema debe mostrar en el detalle el mismo precio que el producto tenía en el catálogo.

## Criterios de Aceptación
1. El valor del precio mostrado en el detalle es igual al valor del precio del producto seleccionado en el catálogo.
2. El precio se muestra con el símbolo `$` seguido del valor con dos decimales, igual que en el catálogo.
3. La sección de precio no está vacía.

## Precondiciones
- Sesión iniciada con `standard_user` / `secret_sauce`.
- El usuario se encuentra en la página del catálogo.

## Datos de entrada
- Al menos dos productos con precios distintos (por ejemplo, "Sauce Labs Backpack" y "Sauce Labs Bike Light"). Precios distintos permiten detectar un defecto que muestre siempre el mismo precio sin importar el producto.

## Prioridad
P1 (Alta)

**Justificación:** si el precio falla, el usuario aún puede iniciar sesión y comprar, por lo que no es P0. Pero un precio distinto al visto en el catálogo es información incorrecta que afecta directamente lo que el usuario cree que va a pagar (ver 3.7 del Test Plan).

## Tipo de prueba
Funcional / Detalle de producto

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- Escenarios: SC-DETAIL-xxx (pendiente de definir)



# Requisito: Detalle de producto (agregar al carrito)

## ID del Requisito
REQ-DETAIL-03

## Descripción
Cuando el usuario agrega un producto al carrito desde la vista de detalle, el sistema debe reflejar que el producto fue agregado: cambiando el botón, actualizando el contador del carrito y registrando el producto en el carrito.

## Criterios de Aceptación
1. Al hacer clic en `Add to cart` en el detalle, el botón cambia a `Remove`.
2. Con el carrito vacío al inicio, el ícono del carrito muestra el número `1` tras agregar el producto.
3. Al abrir el carrito, el producto agregado aparece en él.

## Precondiciones
- Sesión iniciada con `standard_user` / `secret_sauce`.
- El carrito está vacío.
- El usuario se encuentra en la vista de detalle de un producto.

## Datos de entrada
- Un producto cualquiera del catálogo (por ejemplo, "Sauce Labs Backpack").

## Prioridad
P1 (Alta)

**Justificación:** si falla, el usuario no puede agregar desde el detalle, pero sí desde el catálogo y puede completar la compra, por lo que no es P0. Se asigna P1 y no P2 porque, ante la duda entre dos niveles, el Test Plan indica asignar el más alto, y un producto que no llega al carrito impide la compra desde esa vista.

## Tipo de prueba
Funcional / Detalle de producto

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- Escenarios: SC-DETAIL-xxx (pendiente de definir)


# Requisito: Detalle de producto (quitar del carrito)

## ID del Requisito
REQ-DETAIL-04

## Descripción
Cuando el usuario quita un producto del carrito desde la vista de detalle, el sistema debe reflejar que el producto fue quitado: restableciendo el botón, actualizando el contador del carrito y eliminando el producto del carrito.

## Criterios de Aceptación
1. Al hacer clic en `Remove` en el detalle, el botón vuelve a `Add to cart`.
2. Si el producto era el único en el carrito, el ícono del carrito deja de mostrar el contador.
3. Al abrir el carrito, el producto ya no aparece en él.

## Precondiciones
- Sesión iniciada con `standard_user` / `secret_sauce`.
- El producto ya fue agregado al carrito y es el único producto en él.
- El usuario se encuentra en la vista de detalle de ese producto.

## Datos de entrada
- Un producto cualquiera del catálogo (por ejemplo, "Sauce Labs Backpack").

## Prioridad
P1 (Alta)

**Justificación:** si falla, el usuario no puede quitar el producto desde el detalle, pero sí desde el carrito y puede completar la compra, por lo que no es P0. Se asigna P1 y no P2 porque un producto que el usuario quitó y sigue en el carrito altera el total de la compra.

## Tipo de prueba
Funcional / Detalle de producto

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- Escenarios: SC-DETAIL-xxx (pendiente de definir)