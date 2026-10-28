# Casos de Prueba

## Módulo: Login

---

### TC-LOGIN-001 — Login exitoso con credenciales válidas

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-001 |
| Requisito | REQ-LOGIN-01 |
| Prioridad | P0 |
| Tipo | Positivo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: `standard_user` · Contraseña: `secret_sauce` |
| Automatizar | Sí. Determinista, crítico (P0), forma parte del smoke |

**Pasos**
1. Abrir la pagina https://www.saucedemo.com/ 
2. Escribir el usuario en el campo de usuario.
3. Escribir la contraseña en el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- - La URL apunta a  `https://www.saucedemo.com/inventory.html`.
- Se muestra la lista de productos.
- No aparece ningún mensaje de error.

---

### TC-LOGIN-002 — Login con usuario y contraseña inválidos

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-002 |
| Requisito | REQ-LOGIN-02 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: `testing_saucedemo`· Contraseña: `new_userTesting`  |
| Automatizar | Sí. Determinista (mismo mensaje siempre), P1, se ejecuta en regresión, bajo costo de mantenimiento |

**Pasos**
1. Abrir la pagina https://www.saucedemo.com/ 
2. Escribir el usuario incorrecto en el campo de usuario.
3. Escribir la contraseña incorrecta en el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- El usuario permanece en la página de login.
- Se muestra el mensaje de error: `Epic sadface: Username and password do not match any user in this service`
- No se accede al inventario.




---

### TC-LOGIN-003 — Login con usuario inexistente y contraseña válida

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-003 |
| Requisito | REQ-LOGIN-02 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: `testing_saucedemo` · Contraseña: `secret_sauce` |
| Automatizar | Sí. Determinista, P1, regresión. Comparte comportamiento con TC-002 y TC-004: se implementa parametrizado |

**Pasos**
1. Abrir la página `https://www.saucedemo.com/`.
2. Escribir el usuario inexistente en el campo de usuario.
3. Escribir la contraseña válida en el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- La URL sigue siendo `https://www.saucedemo.com/`.
- Se muestra el mensaje de error: `Epic sadface: Username and password do not match any user in this service`

---

### TC-LOGIN-004 — Login con usuario válido y contraseña inválida

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-004 |
| Requisito | REQ-LOGIN-02 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: `standard_user` · Contraseña: `secret_user_demo` |
| Automatizar | Sí. Determinista, P1, regresión. Comparte comportamiento con TC-002 y TC-003: se implementa parametrizado |

**Pasos**
1. Abrir la página `https://www.saucedemo.com/`.
2. Escribir el usuario válido en el campo de usuario.
3. Escribir la contraseña inválida en el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- La URL sigue siendo `https://www.saucedemo.com/`.
- Se muestra el mensaje de error: `Epic sadface: Username and password do not match any user in this service`




---

### TC-LOGIN-005 — Login con usuario y contraseña vacíos

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-005 |
    | Requisito | REQ-LOGIN-03 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: *(vacío)* · Contraseña: *(vacía)* |
| Automatizar | Sí. Determinista, P1, regresión, bajo costo de mantenimiento. Se implementa como test independiente porque su mensaje de error es distinto al de TC-002/003/004 |

**Pasos**
1. Abrir la página `https://www.saucedemo.com/`.
2. Dejar vacío el campo de usuario.
3. Dejar vacío el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- La URL sigue siendo `https://www.saucedemo.com/`.
- Se muestra el mensaje de error: `Epic sadface: Username is required`



### TC-LOGIN-006 — Login con usuario válido y contraseña vacía

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-006 |
| Requisito | REQ-LOGIN-03 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: `standard_user` · Contraseña: *(vacía)* |
| Automatizar | Sí. Determinista, P1, regresión, bajo costo de mantenimiento. Cubre la validación de contraseña vacía, que TC-LOGIN-005 no ejercita porque la app valida primero el usuario |

**Pasos**
1. Abrir la página `https://www.saucedemo.com/`.
2. Ingresar `standard_user` en el campo de usuario.
3. Dejar vacío el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- La URL sigue siendo `https://www.saucedemo.com/`.
- Se muestra el mensaje de error: `Epic sadface: Password is required`.
- No se muestra el contenedor del inventario.

---

### TC-LOGIN-007 — Login con usuario vacío y contraseña válida

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-007 |
| Requisito | REQ-LOGIN-03 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: *(vacío)* · Contraseña: `secret_sauce` |
| Automatizar | Sí. Determinista, P1, regresión, bajo costo de mantenimiento. Ejercita la misma rama que TC-LOGIN-005, pero protege contra una regresión en la que la validación del usuario dependa de la contraseña. Candidato a parametrizar junto con TC-005 y TC-006 |


**Pasos**
1. Abrir la página `https://www.saucedemo.com/`.
2. Dejar vacío el campo de usuario.
3. Ingresar `secret_sauce` en el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- La URL sigue siendo `https://www.saucedemo.com/`.
- Se muestra el mensaje de error: `Epic sadface: Username is required`.
- No se muestra el contenedor del inventario.



### TC-LOGIN-008 — Login con usuario bloqueado

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-008 |
| Requisito | REQ-LOGIN-04 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Usuario: `locked_out_user` · Contraseña: `secret_sauce` |
| Automatizar | Sí. Resultado determinista y mensaje fijo; P1 en regresión; reutiliza `LoginPage`, por lo que el costo de mantenimiento es bajo. |

**Pasos**
1. Abrir la página `https://www.saucedemo.com/`.
2. Ingresar `locked_out_user` en el campo de usuario.
3. Ingresar `secret_sauce` en el campo de contraseña.
4. Pulsar el botón Login.

**Resultado esperado**
- La URL sigue siendo `https://www.saucedemo.com/`.
- Se muestra el mensaje de error: `Epic sadface: Sorry, this user has been locked out.`
- No se muestra el contenedor del inventario.

---

### TC-LOGIN-009 — Acceso directo a página interna sin sesión

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-009 |
| Requisito | REQ-LOGIN-05 |
| Prioridad | P1 |
| Tipo | Negativo |
| Precondiciones | Sesión nueva, sin cookies; sitio disponible |
| Datos de entrada | Una página interna por ejecución (ver tabla de datos) |
| Automatizar | Sí. Determinista; P1 en regresión; no requiere precondiciones y los datos se pueden parametrizar, por lo que el costo de mantenimiento es bajo. |

**Tabla de datos**

| Página interna | URL | Mensaje esperado |
| :--- | :--- | :--- |
| Inventario | `https://www.saucedemo.com/inventory.html` | `Epic sadface: You can only access '/inventory.html' when you are logged in.` |
| Carrito | `https://www.saucedemo.com/cart.html` | `Epic sadface: You can only access '/cart.html' when you are logged in.` |
| Checkout (paso 1) | `https://www.saucedemo.com/checkout-step-one.html` | `Epic sadface: You can only access '/checkout-step-one.html' when you are logged in.` |

**Pasos**
1. Abrir directamente la URL de la página interna (sin haber iniciado sesión).

**Resultado esperado**
- El sistema redirige a `https://www.saucedemo.com/`.
- Se muestra el mensaje de error correspondiente a la página solicitada (ver tabla de datos).
- No se muestra el contenedor del inventario.

---

### TC-LOGIN-010 — Cierre de sesión desde el menú

| Campo | Detalle |
| :--- | :--- |
| Escenario | SC-LOGIN-010 |
| Requisito | REQ-LOGIN-06 |
| Prioridad | P1 |
| Tipo | Positivo |
| Precondiciones | Usuario `standard_user` con sesión iniciada y posicionado en `https://www.saucedemo.com/inventory.html`; sitio disponible |
| Datos de entrada | Usuario: `standard_user` · Contraseña: `secret_sauce` (solo para la precondición) |
| Automatizar | Sí. Determinista; P1 en regresión; la precondición de sesión se resuelve con un fixture, por lo que el costo de mantenimiento es bajo. |

**Pasos**
1. Abrir el menú lateral (botón de menú, esquina superior izquierda).
2. Pulsar la opción Logout.
3. Intentar acceder directamente a `https://www.saucedemo.com/inventory.html`.

**Resultado esperado**
- Tras el paso 2: el sistema redirige a `https://www.saucedemo.com/` y se muestra el formulario de login (usuario, contraseña y botón Login).
- Tras el paso 3: el sistema redirige a `https://www.saucedemo.com/` y muestra el mensaje `Epic sadface: You can only access '/inventory.html' when you are logged in.`, lo que confirma que la sesión terminó.
- No se muestra el contenedor del inventario.


