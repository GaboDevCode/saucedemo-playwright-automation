# Requisito: Login Exitoso

## ID del Requisito
REQ-LOGIN-01

## Descripción
El usuario debe poder iniciar sesión en la aplicación utilizando credenciales válidas (nombre de usuario y contraseña). Al iniciar sesión correctamente, el usuario debe acceder a la página principal de productos.

## Criterios de Aceptación
1. El usuario ingresa un nombre de usuario y contraseña válidos.
2. Al presionar el botón de login, se redirige al usuario a la página de inventario.
3. No se muestra ningún error ni advertencia.
4. La sesión se mantiene activa hasta que el usuario se desloguea.

## Datos de entrada
- Usuario: `standard_user`
- Contraseña: `secret_sauce`

## Prioridad
P0 (Crítico)

## Tipo de prueba
Funcional / Login

## Responsable
Gabriel Bocanegra

## Trazabilidad
- SC-LOGIN-001: Login con credenciales válidas 
    




## Requisito: [Login con credenciales inválidas]

### ID del Requisito
REQ-LOGIN-02    

### Descripción
El sistema debe impedir el acceso cuando las credenciales proporcionadas no sean válidas y debe informar al usuario mediante un mensaje de error.
### Criterios de Aceptación

1. El usuario ingresa un nombre de usuario y contraseña invalidos.
2. Al presionar el botón de login, se muestra un mensaje notificando al usuario que las credenciales son incorrectas 
3. El sistema no permite el acceso.


### Prioridad
P1 (Alta)

### Tipo de Prueba
Funcional / Login

### Responsable
Eduardo Gabriel Bocanegra Toledo

### Trazabilidad
- SC-LOGIN-002: Login con usuario y contraseña inválidos
- SC-LOGIN-003: Login con usuario inexistente y contraseña válida
- SC-LOGIN-004: Login con usuario válido y contraseña inválida


---



# Requisito: Campos obligatorios en el login

## ID del Requisito
REQ-LOGIN-03

## Descripción
El sistema debe exigir que el usuario y la contraseña estén completos antes de intentar la autenticación. Si falta alguno de los dos, debe impedir el acceso e informar al usuario cuál es el campo requerido.

## Criterios de Aceptación
1. Si el campo de usuario está vacío (con la contraseña vacía o completa), al presionar el botón de login se muestra un mensaje de error que indica que el usuario es obligatorio.
2. Si el usuario está informado y la contraseña está vacía, al presionar el botón de login se muestra un mensaje de error que indica que la contraseña es obligatoria.
3. En todos los casos, el usuario permanece en la página de login.
4. En todos los casos, el sistema no permite el acceso al inventario.

## Observaciones
- Con ambos campos vacíos, la aplicación informa primero el campo de usuario (`Username is required`). El orden de validación es comportamiento observado, no un requisito formal. Si cambia, se registra como observación hasta confirmarlo (Test Plan 1.3).

## Prioridad
P1 (Alta)

## Tipo de prueba
Funcional / Login / Validación de campos

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- SC-LOGIN-005: Login con usuario y contraseña vacíos
- SC-LOGIN-006: Login con usuario válido y contraseña vacía
- SC-LOGIN-007: Login con usuario vacío y contraseña válida




# Requisito: Login con usuario bloqueado

## ID del Requisito
REQ-LOGIN-04

## Descripción
El sistema debe impedir el acceso a un usuario cuya cuenta está bloqueada, aun cuando sus credenciales (usuario y contraseña) sean correctas, e informar el motivo mediante un mensaje de error.

## Criterios de Aceptación
1. El usuario bloqueado ingresa su nombre de usuario y su contraseña correcta.
2. Al presionar el botón de login, se muestra un mensaje indicando que el usuario ha sido bloqueado (texto observado: `Epic sadface: Sorry, this user has been locked out.`).
3. El usuario permanece en la página de login; no se redirige al inventario.
4. No se inicia sesión.

## Datos de entrada
- Usuario: `locked_out_user`
- Contraseña: `secret_sauce`

## Prioridad
P1 (Alta). Escenario negativo importante.

## Tipo de prueba
Funcional / Login

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- SC-LOGIN-008: Login con usuario bloqueado




# Requisito: Acceso a páginas internas sin sesión

## ID del Requisito
REQ-LOGIN-05

## Descripción
El sistema debe impedir el acceso a las páginas internas de la aplicación a un usuario que no ha iniciado sesión, redirigiéndolo a la página de login e informando el motivo mediante un mensaje de error.

## Criterios de Aceptación
1. El usuario, sin sesión activa, intenta abrir directamente una página interna escribiendo su URL en el navegador (por ejemplo, `https://www.saucedemo.com/inventory.html`).
2. El sistema redirige al usuario a la página de login.
3. Se muestra un mensaje de error indicando que solo se puede acceder a esa página con sesión iniciada (texto observado: `Epic sadface: You can only access '/inventory.html' when you are logged in.`).
4. No se muestra el contenido de la página interna.

## Datos de entrada / Precondiciones
- Sesión nueva, sin cookies; el usuario no ha iniciado sesión.
- URL directa: `https://www.saucedemo.com/inventory.html`

## Prioridad
P1 (Alta). Control de acceso importante.

## Tipo de prueba
Funcional / Login

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- SC-LOGIN-009: Acceso directo a página interna sin sesión



# Requisito: Cierre de sesión

## ID del Requisito
REQ-LOGIN-06

## Descripción
El sistema debe permitir al usuario con sesión iniciada cerrarla desde el menú de la aplicación, finalizando su sesión y regresándolo a la página de login.

## Criterios de Aceptación
1. El usuario inicia sesión con credenciales válidas.
2. El usuario abre el menú lateral y selecciona la opción **Logout**.
3. El sistema redirige al usuario a la página de login (`https://www.saucedemo.com/`).
4. Se muestra el formulario de login, sin mensaje de error.
5. La sesión queda finalizada: al intentar abrir directamente una página interna, el sistema aplica el control de acceso de REQ-LOGIN-05.

## Datos de entrada / Precondiciones
- Sesión iniciada con `standard_user` / `secret_sauce`.

## Prioridad
P1 (Alta). Función importante que cierra el ciclo de vida de la sesión (REQ-LOGIN-01)

## Tipo de prueba
Funcional / Login

## Responsable
Eduardo Gabriel Bocanegra Toledo

## Trazabilidad
- SC-LOGIN-010: Cierre de sesión desde el menú










