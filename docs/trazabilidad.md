# Matriz de Trazabilidad
## Módulo: Login

| Requisito | Escenario | Caso de Prueba | Prioridad | ¿Automatizar? | Test Automatizado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-LOGIN-01 | SC-LOGIN-001 | TC-LOGIN-001 | P0 | Sí | `test_login_valid_credentials` | Automatizado |
| REQ-LOGIN-02 | SC-LOGIN-002 | TC-LOGIN-002 | P1 | Sí | `test_login_invalid_credentials[TC-LOGIN-002-invalid_user_invalid_password]` | Automatizado |
| REQ-LOGIN-02 | SC-LOGIN-003 | TC-LOGIN-003 | P1 | Sí | `test_login_invalid_credentials[TC-LOGIN-003-nonexistent_user_valid_password]` | Automatizado |
| REQ-LOGIN-02 | SC-LOGIN-004 | TC-LOGIN-004 | P1 | Sí | `test_login_invalid_credentials[TC-LOGIN-004-valid_user_invalid_password]` | Automatizado |
| REQ-LOGIN-03 | SC-LOGIN-005 | TC-LOGIN-005 | P1 | Sí | `test_login_rejected[TC-LOGIN-005-login_empty_credentials]`           | Automatizado |
| REQ-LOGIN-03 | SC-LOGIN-006 | TC-LOGIN-006 | P1 | Sí | `test_login_rejected[TC-LOGIN-006-login_valid_user_empty_password]`   | Automatizado |
| REQ-LOGIN-03 | SC-LOGIN-007 | TC-LOGIN-007 | P1 | Sí | `test_login_rejected[TC-LOGIN-007-login_empty_user_valid_password]`   | Automatizado |
| REQ-LOGIN-04 | SC-LOGIN-008 | TC-LOGIN-008 | P1 | Sí | `test_login_rejected[TC-LOGIN-008-login_locked_out_user]`             | Automatizado |
|REQ-LOGIN-05| SC-LOGIN-009 | TC-LOGIN-009 | P1 | Sí | `test_access_internal_page_without_session` | Automatizado |
|REQ-LOGIN-06| SC-LOGIN-010 | TC-LOGIN-010 | P1 | Sí | `test_logout_from_menu` | Desarrollo |
