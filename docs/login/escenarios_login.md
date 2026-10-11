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
