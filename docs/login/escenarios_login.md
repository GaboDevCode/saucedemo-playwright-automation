# Escenarios de Prueba

## Módulo: Login

| ID | Escenario | Requisito | Descripción | Tipo | Prioridad | Resultado esperado |
| --- | --- | --- | --- | --- | --- | --- |
| SC-LOGIN-001 | Login con credenciales válidas | REQ-LOGIN-01 | Validar el acceso al sistema utilizando credenciales válidas. | Positivo | P0 | El sistema permite el acceso y redirige al usuario a la página principal del catálogo. |
| SC-LOGIN-002 | Login con usuario y contraseña inválidos | REQ-LOGIN-02 | Validar el comportamiento del sistema cuando tanto el usuario como la contraseña proporcionados son inválidos. | Negativo | P1 | El sistema impide el acceso y muestra el mensaje de error correspondiente. |
| SC-LOGIN-003 | Login con usuario inexistente y contraseña válida | REQ-LOGIN-02 | Validar el comportamiento del sistema cuando el usuario proporcionado no existe y la contraseña es válida. | Negativo | P1 | El sistema impide el acceso y muestra el mensaje de error correspondiente. |
| SC-LOGIN-004 | Login con usuario válido y contraseña inválida | REQ-LOGIN-02 | Validar el comportamiento del sistema cuando el usuario es válido pero la contraseña proporcionada es incorrecta. | Negativo | P1 | El sistema impide el acceso y muestra el mensaje de error correspondiente. |
| SC-LOGIN-005 | Login con usuario y contraseña vacíos | REQ-LOGIN-03 | Validar el comportamiento del sistema cuando el usuario intenta iniciar sesión sin proporcionar credenciales. | Negativo | P1 | El sistema impide el acceso y muestra la validación correspondiente. |
| SC-LOGIN-006 | Login con usuario válido y contraseña vacía       | REQ-LOGIN-03 | Validar el comportamiento del sistema cuando el usuario proporciona un usuario válido pero deja vacía la contraseña. | Negativo | P1        | El sistema impide el acceso y muestra la validación correspondiente.                   |
| SC-LOGIN-007 | Login con usuario vacío y contraseña válida       | REQ-LOGIN-03 | Validar el comportamiento del sistema cuando el usuario deja vacío el usuario pero proporciona una contraseña válida. | Negativo | P1        | El sistema impide el acceso y muestra la validación correspondiente.                   |
| SC-LOGIN-008 | Login con usuario bloqueado                       | REQ-LOGIN-04 | Validar el comportamiento del sistema cuando un usuario bloqueado intenta iniciar sesión con credenciales correctas. | Negativo | P1 | El sistema impide el acceso y muestra el mensaje de usuario bloqueado.                 |
| SC-LOGIN-009 | Acceso directo a página interna sin sesión        | REQ-LOGIN-05 | Validar el comportamiento del sistema cuando un usuario sin sesión intenta abrir directamente una página interna.   | Negativo | P1 | El sistema redirige a la página de login y muestra el mensaje de acceso restringido.   |
| SC-LOGIN-010 | Cierre de sesión desde el menú                    | REQ-LOGIN-06 | Validar que el usuario con sesión iniciada pueda cerrarla y que el sistema finalice su sesión.                      | Positivo | P1 | El sistema redirige a la página de login y la sesión queda finalizada.                 |
