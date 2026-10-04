# Plan de Pruebas (Test Plan)
 
| **Campo** | **Valor** |
| :--- | :--- |
| **Proyecto:** | Swag Labs (Sauce Demo) |
| **Autor:** | Eduardo Gabriel Bocanegra Toledo |
| **Fecha de creación:** | 2026-10-03 |
| **Última actualización:** | 2026-10-03 |
| **Versión del plan:** | v1.2 |
| **Estado:** | Vigente |
 
---
 
## 1. Introducción y Objetivos
 
### 1.1 Propósito
Definir la estrategia de pruebas (manuales y automatizadas) para los flujos de **autenticación, carrito, checkout y detalles de producto** de Swag Labs, con el fin de verificar que el flujo principal de compra funciona correctamente y de forma estable ante cualquier cambio, y de construir una base de automatización mantenible con criterios claros de qué se automatiza y qué no.
 
### 1.2 Objetivos
| # | Objetivo | Cómo se mide |
| :--- | :--- | :--- |
| O1 | Verificar los flujos críticos de Login, Carrito y Checkout | 100 % de los casos P0 ejecutados y aprobados |
| O2 | Contar con un smoke test rápido y confiable | Suite smoke ejecutable en menos de 2 minutos |
| O3 | Tener una suite de regresión automatizada y estable | Tasa de tests inestables (flaky) menor al 2 % |
| O4 | Documentar el razonamiento de diseño de pruebas | Cada caso trazado a un escenario y con justificación de automatizar o no |
 
### 1.3 Base de pruebas (Test Basis)
Swag Labs **no cuenta con documento de requisitos formal**. Por lo tanto, la base de pruebas será:
1. Exploración funcional de la aplicación.
2. Comportamiento observable y mensajes de error de la propia app.
3. Requisitos derivados y documentados por el autor (ID `REQ-XX`) a partir de la exploración.
Cualquier comportamiento que la aplicación muestre y que no se pueda contrastar contra un requisito se registrará como **observación**, no como defecto, hasta confirmarlo.
 
---
 
## 2. Alcance (Scope)
 
### 2.1 En alcance (In-Scope)
 
| Módulo | Funcionalidades cubiertas | Justificación |
| :--- | :--- | :--- |
| **A. Login** | Inicio de sesión válido e inválido, usuarios bloqueados, validaciones de campos, cierre de sesión, acceso sin sesión | Puerta de entrada; si falla, nada más es accesible |
| **B. Carrito** | Ver contenido, quitar productos, continuar comprando, persistencia del contenido | Paso obligatorio antes del pago; afecta el total de la compra |
| **C. Checkout** | Datos del cliente (paso 1), resumen y totales (paso 2), finalización (paso 3), cancelación | Flujo de mayor valor de negocio: es el que genera la compra |
| **D. Detalles de producto** | Visualizar los datos principales del producto: nombre, precio y descripción | El precio mostrado debe ser coherente con el del carrito y el checkout; es el origen de los datos de la compra |
 
> Agregar un producto al carrito se usa como **precondición** de los módulos B y C; su comportamiento propio se prueba solo en lo necesario para esos flujos.
 
### 2.2 Tipos de prueba
- **Funcionales:** comportamiento de cada módulo contra los requisitos derivados.
- **UI:** presencia, visibilidad y estado de los elementos clave (no incluye comparación visual pixel a pixel ni responsive).
- **Smoke:** verificación rápida del camino crítico.
- **Regresión:** re-ejecución de casos funcionales tras un cambio. *No es un tipo distinto de prueba, sino un propósito de ejecución.*
- **Exploratorias:** sesiones manuales para descubrir escenarios y alimentar el diseño.
### 2.3 Fuera de alcance (Out-of-Scope)
 
| Elemento | Razón |
| :--- | :--- |
| Catálogo de productos (ordenamiento, listado general) | Fase 2; no es parte del flujo de pago para esta versión. Solo se usa para llegar a los detalles de un producto |
| Menú lateral (excepto Logout) y enlaces a redes sociales | Bajo riesgo de negocio |
| Pruebas de rendimiento y carga | Sin objetivos de rendimiento definidos; requiere otro tipo de herramientas |
| Pruebas de seguridad / penetración | Fuera de la competencia y del objetivo del proyecto |
| Navegadores obsoletos (ej. Internet Explorer) | Sin soporte oficial por parte de las herramientas elegidas |
| Pruebas móviles nativas | La aplicación evaluada es web |
 
### 2.4 Supuestos y restricciones
- El entorno es un **sitio público de terceros**: no se controla su disponibilidad, datos ni despliegues.
- Las credenciales de los usuarios de prueba son públicas y están publicadas en la propia aplicación.
- Algunos usuarios (`problem_user`, `error_user`, `visual_user`, `performance_glitch_user`) presentan **defectos intencionales** como parte del diseño de la demo.
---
 
## 3. Estrategia de Pruebas
 
### 3.1 Flujo de trabajo
`Requisito derivado → Riesgo → Escenario → Caso de prueba → Matriz de cobertura → Ejecución manual → Candidato a automatización → Implementación → Análisis de resultados`
 
No se escribe código de automatización de un caso hasta que el caso está diseñado y justificado.
 
### 3.2 Técnicas de diseño de pruebas
| Técnica | Dónde se aplica |
| :--- | :--- |
| Partición de equivalencia | Credenciales y campos del formulario de checkout |
| Análisis de valores límite | Campos vacíos, un solo carácter, longitudes extremas |
| Tabla de decisión | Combinaciones de usuario/contraseña y estado del usuario |
| Transición de estados | Flujo del carrito y pasos del checkout |
| Pruebas exploratorias | Descubrimiento inicial y comportamiento de usuarios especiales |
 
### 3.3 Manual vs. automatizado
 
**Manual:** exploración inicial, comportamiento de usuarios con defectos intencionales, verificación visual subjetiva y validación de escenarios nuevos antes de automatizarlos.
 
**Automatizado:** smoke y regresión de los módulos en alcance.
 
**Criterio de decisión.** Un caso se automatiza cuando cumple la mayoría de estas condiciones:
 
| Criterio | Pregunta |
| :--- | :--- |
| Determinismo | ¿El resultado esperado es siempre el mismo? |
| Riesgo / criticidad | ¿Su falla afectaría el flujo principal? |
| Frecuencia | ¿Se ejecutará repetidamente? |
| Estabilidad | ¿La funcionalidad cambia poco? |
| Costo de mantenimiento | ¿Es barato de mantener a largo plazo? |
| Alternativa mejor | ¿Se puede validar mejor en otro nivel (por ejemplo, API)? |
 
Un caso que requiere juicio humano, es exploratorio o es muy inestable **permanece manual**, y se documenta la razón.
 
### 3.4 Entornos y herramientas
| Elemento | Detalle |
| :--- | :--- |
| **Entorno de pruebas** | https://www.saucedemo.com/ |
| **Navegadores** | Chromium y Firefox (motores incluidos en Playwright) |
| **Lenguaje y framework de pruebas** | Python + pytest |
| **Automatización web** | Playwright (Python) |
| **Arquitectura** | Page Object Model |
| **Reportes de ejecución** | pytest-html y/o Allure |
| **Control de versiones** | Git + GitHub |
| **Gestión de defectos** | GitHub Issues (etiquetas de severidad y prioridad) |
| **Evidencias** | Carpeta `evidence/` en el repositorio (capturas, trazas, videos) |
| **Integración continua** | GitHub Actions (planeado para una fase posterior) |
 
### 3.5 Datos de prueba
| Usuario | Uso previsto |
| :--- | :--- |
| `standard_user` | Flujo principal y regresión |
| `locked_out_user` | Escenario negativo de usuario bloqueado |
| `problem_user`, `error_user`, `visual_user`, `performance_glitch_user` | Pruebas exploratorias; automatización solo si se justifica |
 
- Credenciales y URL se gestionan por **configuración** (variables de entorno o archivo de configuración), no escritas dentro de los tests.
- Cada test debe ser **independiente**: parte de un estado conocido (sesión nueva, carrito vacío).
### 3.6 Gestión de defectos
| Severidad | Descripción |
| :--- | :--- |
| **Crítica** | Impide completar el flujo principal (login, compra) |
| **Alta** | Funcionalidad principal incorrecta con alternativa limitada |
| **Media** | Funcionalidad secundaria incorrecta |
| **Baja** | Defecto cosmético o menor |
 
Los comportamientos erróneos de los usuarios con defectos intencionales se etiquetan como `known-issue` para distinguirlos de defectos nuevos.
 
### 3.7 Prioridad de los casos de prueba
 
La **prioridad** indica qué tan importante es probar un caso. Se asigna al diseñar el caso (en la matriz de cobertura) y puede reevaluarse. *No es lo mismo que la severidad (3.6), que aplica a los defectos.*
 
| Nivel | Definición | Cuándo se ejecuta | Automatización |
| :--- | :--- | :--- | :--- |
| **P0** | Sin esto no se puede completar el flujo principal (iniciar sesión y comprar). Si falla, la aplicación no cumple su función | En cada cambio (forma la suite **smoke**) | Primera en automatizarse |
| **P1** | Funcionalidad importante, validaciones y escenarios negativos relevantes. El flujo principal puede continuar con una alternativa | En la suite de **regresión** | Se automatiza si cumple los criterios de 3.3 |
| **P2** | Funcionalidad secundaria, casos de borde poco probables o aspectos cosméticos | En la regresión completa o cuando hay tiempo | Solo si es barata de mantener; por defecto, manual |
 
**Cómo asignar el nivel.** Para cada caso se evalúa *"¿qué pasaría si esto falla en producción?"*:
 
| Si al fallar... | Prioridad |
| :--- | :--- |
| El usuario no puede entrar o no puede completar una compra | **P0** |
| Se rompe una función importante, se aceptan datos inválidos o se muestra información incorrecta, pero se puede seguir comprando | **P1** |
| Afecta algo secundario, cosmético o un borde que casi nadie encontraría | **P2** |
 
**Reglas:**
- P0 no significa automatizar de forma automática: la decisión de automatizar sigue los criterios de 3.3.
- Ante la duda entre dos niveles, se asigna el más alto y se justifica en el caso.
**Ejemplos aplicados:**
 
| Caso | Módulo | Prioridad | Razón |
| :--- | :--- | :--- | :--- |
| Login con usuario y contraseña válidos | Login | P0 | Sin esto no hay acceso |
| Completar la compra con datos válidos | Checkout | P0 | Es el flujo que genera la compra |
| Login con `locked_out_user` | Login | P1 | Escenario negativo importante; el flujo principal sigue funcionando con otro usuario |
| Checkout con el código postal vacío | Checkout | P1 | Validación que evita datos inválidos; el flujo válido no se ve afectado |
| El precio del detalle coincide con el del carrito | Detalles de producto | P1 | Información incorrecta afecta la confianza y el total |
| El botón "Cancel" del checkout regresa al carrito | Checkout | P2 | Navegación secundaria; hay otra forma de volver |
 
---
 
## 4. Criterios de Entrada y Salida
 
### 4.1 Criterios de entrada
- El sitio está disponible y accesible.
- Los escenarios del módulo están definidos.
- El entorno local de automatización funciona (dependencias instaladas y navegador ejecutable).
### 4.2 Criterios de salida
- 100 % de los casos P0 (ver 3.7) ejecutados y aprobados.
- Al menos 90 % de los casos P1 ejecutados.
- Sin defectos de severidad Crítica o Alta abiertos y no justificados.
- Matriz de cobertura actualizada.
- Test Summary Report emitido.
### 4.3 Criterios de suspensión
- Caída prolongada del sitio de pruebas.
- Cambio en la aplicación que invalide más del 30 % de los casos.
---
 
## 5. Entregables
 
| Momento | Entregable |
| :--- | :--- |
| **Antes de la ejecución** | Test Plan, escenarios, casos de prueba y matriz de cobertura |
| **Durante la ejecución** | Defectos registrados en GitHub Issues, evidencias y reportes de ejecución |
| **Al finalizar** | Test Summary Report con métricas |
 
---
 
## 6. Roles y Responsabilidades
| Rol | Responsable | Responsabilidades |
| :--- | :--- | :--- |
| Diseño de pruebas | Eduardo Gabriel Bocanegra Toledo | Análisis, escenarios, casos, matriz |
| Automatización | Eduardo Gabriel Bocanegra Toledo | Framework, tests, mantenimiento |
| Ejecución y reporte | Eduardo Gabriel Bocanegra Toledo | Ejecución, defectos, informe final |
 
---
 
## 7. Cronograma
| Fase | Actividad | Resultado |
| :--- | :--- | :--- |
| 1 | Exploración funcional y requisitos derivados | Lista de `REQ-XX` |
| 2 | Escenarios, casos y matriz de cobertura | Casos diseñados y priorizados |
| 3 | Ejecución manual | Resultados y defectos iniciales |
| 4 | Análisis de candidatos a automatización | Lista justificada |
| 5 | Implementación (smoke y luego regresión) | Suite automatizada |
| 6 | Reportes y CI | Resumen final |
 
---
 
## 8. Gestión de Riesgos y Mitigación
 
| # | Riesgo | Prob. | Impacto | Mitigación |
| :--- | :--- | :--- | :--- | :--- |
| R1 | El sitio de terceros cambia o deja de estar disponible sin aviso | Media | Alto | Documentar la versión observada; guardar evidencias; reintentar y suspender según 4.3 |
| R2 | Defectos intencionales de ciertos usuarios se confunden con defectos reales | Alta | Medio | Etiqueta `known-issue`; priorizar `standard_user` en regresión |
| R3 | Tests inestables por tiempos (por ejemplo, `performance_glitch_user`) | Media | Alto | Esperas basadas en estado (auto-wait y aserciones web-first); sin esperas fijas |
| R4 | Estado compartido entre tests (carrito persistente) | Alta | Alto | Contextos de navegador aislados; cada test parte desde un estado limpio |
| R5 | Sobreautomatizar casos de bajo valor | Media | Medio | Aplicar los criterios de 3.3 y registrar la decisión |
| R6 | Ausencia de requisitos formales genera ambigüedad | Alta | Medio | Requisitos derivados `REQ-XX` y registro de observaciones |
| R7 | Disponibilidad de tiempo del autor (proyecto personal) | Media | Medio | Priorizar P0, entregar por fases |
 
---
 
## 9. Métricas
 
| Métrica | Fórmula / descripción |
| :--- | :--- |
| Ejecución de casos | Ejecutados / diseñados |
| Tasa de aprobación | Aprobados / ejecutados |
| Cobertura de requisitos | Requisitos con al menos un caso / total de requisitos |
| Defectos por severidad | Conteo por nivel |
| Porcentaje automatizado | Casos automatizados / casos totales |
| Tasa de inestabilidad (flaky) | Tests con resultados distintos sin cambios / tests totales |
| Duración de suite | Tiempo de ejecución de smoke y de regresión |
 
---
 
## 10. Historial de Versiones
 
| Versión | Fecha | Cambios |
| :--- | :--- | :--- |
| v1.0 | 2026-10-03 | Versión inicial |
| v1.1 | 2026-10-03 | Objetivos medibles, base de pruebas, justificación del alcance, criterios de automatización, datos de prueba, criterios de entrada/salida, roles, métricas, riesgos del proyecto real |
| v1.2 | 2026-10-03 | Se agrega el módulo D (Detalles de producto) y se corrige la contradicción con el fuera de alcance; se agrega la sección 3.7 con la definición de prioridades P0, P1 y P2 |
