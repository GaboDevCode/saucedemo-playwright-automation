# Matriz de Trazabilidad

## Módulo: Login

| Requisito | Escenario | Caso de Prueba | Prioridad | ¿Automatizar? | Test Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-LOGIN-01 | SC-LOGIN-001 | TC-LOGIN-001 | P0 | Sí | `test_login_valid_credentials` | Automatizado |
| REQ-LOGIN-02 | SC-LOGIN-002 | TC-LOGIN-002 | P1 | Sí | `test_login_invalid_credentials` | Diseñado |
| REQ-LOGIN-02 | SC-LOGIN-003 | TC-LOGIN-003 | P1 | Sí | `test_login_invalid_credentials` | Diseñado |
| REQ-LOGIN-02 | SC-LOGIN-004 | TC-LOGIN-004 | P1 | Sí | `test_login_invalid_credentials` | Diseñado |
| REQ-LOGIN-03 | SC-LOGIN-005 | TC-LOGIN-005 | P1 | Sí | `test_login_empty_credentials` | Diseñado |


### Pendientes de cobertura
- REQ-LOGIN-01, criterio 4 (persistencia de sesión): sin escenario asignado.
- Usuario bloqueado (`locked_out_user`), usuario vacío, contraseña vacía, logout y acceso directo a `/inventory.html` sin sesión: previstos en el Test Plan, aún sin escenario.