# Swag Labs — QA Automation basado en diseño de pruebas

![Estado](https://img.shields.io/badge/estado-en%20construcci%C3%B3n-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Playwright](https://img.shields.io/badge/Playwright-Python-green)
![pytest](https://img.shields.io/badge/pytest-framework-orange)

Proyecto personal de QA que demuestra un flujo completo de trabajo:

**analizar → diseñar pruebas → priorizar → decidir qué automatizar → implementar → ejecutar → reportar**

La idea central es que **la automatización se construye a partir del diseño de pruebas**, no al revés. Por eso este repositorio documenta el proceso completo, desde el **Plan de Pruebas** hasta los resultados de ejecución.

---

## Aplicación bajo prueba

|                |                            |
| -------------- | -------------------------- |
| **Aplicación** | Swag Labs (SauceDemo)      |
| **URL**        | https://www.saucedemo.com/ |
| **Tipo**       | E-commerce de demostración |

> Swag Labs es el medio para practicar habilidades transferibles de QA. El enfoque aplica a cualquier aplicación web.

Swag Labs **no cuenta con documento de requisitos formal**. Los requisitos (`REQ-XX`) se derivan de la exploración funcional de la aplicación y de su comportamiento observable.

---

## Stack

| Área                    | Herramienta                                |
| ----------------------- | ------------------------------------------ |
| Lenguaje                | Python                                     |
| Framework de pruebas    | pytest                                     |
| Automatización UI       | Playwright (Python)                        |
| Navegadores             | Chromium y Firefox                         |
| Patrón de diseño        | Page Object Model (POM)                    |
| Gestión de dependencias | requirements.txt                           |
| Reportes                | pytest-html y/o Allure (según evolución)   |
| Gestión de defectos     | GitHub Issues (etiquetas de severidad)     |
| Control de versiones    | Git + GitHub                               |
| Integración continua    | GitHub Actions (planeado para una fase posterior) |

---

## Estado del proyecto

| Módulo                   | Diseño de pruebas | Automatización | Detalle                                                                 |
| ------------------------ | ----------------- | -------------- | ----------------------------------------------------------------------- |
| **Login**                | Completo          | Completa       | 10 casos (TC-LOGIN-001 a 010): login válido/inválido, usuario bloqueado, acceso sin sesión y logout |
| **Carrito**              | Pendiente         | Pendiente      | —                                                                       |
| **Checkout**             | Pendiente         | Pendiente      | —                                                                       |
| **Detalles de producto** | Pendiente         | Pendiente      | —                                                                       |
---

## Documentación

Todo el proceso de diseño de pruebas se encuentra en la carpeta [`docs/`](docs/):

| Documento                                                 | Qué responde                                                                      |
| --------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [Plan de pruebas](docs/TEST_PLAN.md)                      | ¿Qué se prueba, qué no, cómo y por qué?                                           |
| [Requisitos de Login](docs/login/requisitos_login.md)     | ¿Qué debe hacer el sistema? (requisitos derivados `REQ-XX`)                       |
| [Escenarios de Login](docs/login/escenarios_login.md)     | ¿Qué comportamientos se quieren validar?                                          |
| [Casos de prueba de Login](docs/login/test_case_Login.md) | ¿Cómo se valida cada comportamiento y por qué se automatiza?                      |
| [Matriz de trazabilidad](docs/trazabilidad.md)            | ¿Qué requisitos, escenarios y casos están cubiertos y cuáles están automatizados? |
| Defectos                                                  | ¿Qué problemas se encontraron durante las pruebas? Se registran en GitHub Issues  |

> Los documentos de los demás módulos se agregan conforme avanza el proyecto.

---

## Alcance

### Dentro del alcance

| Módulo                   | Qué se valida                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Login**                | Inicio de sesión válido e inválido, usuarios bloqueados, validaciones de campos, cierre de sesión y acceso sin sesión   |
| **Carrito**              | Ver contenido, quitar productos, continuar comprando y persistencia del contenido                                      |
| **Checkout**             | Datos del cliente, resumen y totales, finalización de la compra y cancelación                                          |
| **Detalles de producto** | Datos principales del producto (nombre, precio y descripción) y su coherencia con el carrito y el checkout             |

> Agregar un producto al carrito se usa como **precondición** de Carrito y Checkout; su comportamiento propio se prueba solo en lo necesario para esos flujos.

### Fuera del alcance

* Catálogo de productos (ordenamiento y listado general): solo se usa para llegar al detalle de un producto
* Menú lateral (excepto Logout) y enlaces a redes sociales
* Pruebas de rendimiento y carga
* Pruebas de seguridad y penetración
* Navegadores obsoletos (por ejemplo, Internet Explorer)
* Pruebas móviles nativas (la aplicación evaluada es web)

Algunos de estos puntos podrán incorporarse como extensiones del proyecto.

---

## Flujo de trabajo

El proyecto sigue un enfoque **QA-first**, donde el diseño de pruebas precede a la automatización. No se escribe código de automatización de un caso hasta que el caso está diseñado y justificado.

```text
        REQUISITO DERIVADO
                │
                ▼
             RIESGO
                │
                ▼
           ESCENARIO
                │
                ▼
        CASO DE PRUEBA
                │
                ▼
     MATRIZ DE TRAZABILIDAD
                │
                ▼
        EJECUCIÓN MANUAL
                │
                ▼
  CANDIDATO A AUTOMATIZACIÓN
                │
                ▼
   IMPLEMENTACIÓN (POM / PYTEST)
                │
                ▼
   ANÁLISIS DE RESULTADOS / REPORTES
```

### 1. Plan de pruebas

Define la estrategia general del proyecto:

* Objetivos medibles y base de pruebas
* Alcance y fuera de alcance
* Tipos de prueba y técnicas de diseño
* Criterios de automatización
* Datos de prueba, entornos y herramientas
* Gestión de defectos y prioridades
* Criterios de entrada, salida y suspensión
* Riesgos y métricas

### 2. Requisitos

Se identifican las funcionalidades y comportamientos que deben validarse. Se documentan con ID `REQ-<MÓDULO>-<NN>` (por ejemplo, `REQ-LOGIN-01`) y sirven como base para definir escenarios y casos.

### 3. Escenarios

Los escenarios describen **qué comportamiento o flujo se desea validar**, sin entrar en el detalle de pasos.

Ejemplo:

> **SC-LOGIN-001:** Login con credenciales válidas.

A partir de cada escenario pueden derivarse uno o varios casos de prueba.

### 4. Casos de prueba

Los casos de prueba definen **cómo se validará cada escenario**. Cada caso incluye:

* ID, escenario y requisito relacionado
* Prioridad y tipo (positivo o negativo)
* Precondiciones y datos de entrada
* Decisión de automatizar, con su justificación
* Pasos
* Resultado esperado

Ejemplo:

> **TC-LOGIN-001:** Login exitoso con usuario y contraseña válidos.

### 5. Matriz de trazabilidad

La matriz relaciona los diferentes niveles del proceso y permite conocer qué parte del sistema está cubierta:

```text
Requisito → Escenario → Caso de prueba → Test automatizado → Resultado → Defecto (si aplica)
```

Permite identificar:

* Qué funcionalidades están cubiertas.
* Qué casos están automatizados y cuáles permanecen manuales.
* Qué pruebas fallaron.
* Qué defectos fueron encontrados por cada prueba.

### 6. Tests con Playwright

Una vez diseñados y priorizados los casos, se automatizan los que cumplen los criterios de automatización. Se implementan con **Playwright + Python + pytest**.

La automatización no sustituye al diseño de pruebas; es la implementación técnica de los casos seleccionados.

### 7. POM / Fixtures

La estructura técnica utiliza:

* **Page Object Model (POM)** para encapsular la interacción con cada página.
* **Fixtures de pytest** para reutilizar configuración, contexto y recursos.
* **Parametrización** para casos que comparten pasos y solo cambian los datos.
* **Configuración** (variables de entorno o archivo) para credenciales y URL, sin escribirlas dentro de los tests.
* **Independencia entre tests**: cada uno parte de un estado conocido (sesión nueva, carrito vacío).

### 8. Reportes

Los resultados de ejecución se utilizan para comunicar:

* Pruebas ejecutadas, exitosas y fallidas.
* Evidencias (capturas, trazas y videos).
* Errores encontrados y defectos asociados.

La estrategia de reportes podrá evolucionar hacia **pytest-html y/o Allure**.

---

## Tipos de pruebas

| Tipo             | Descripción                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| **Funcionales**  | Comportamiento de cada módulo contra los requisitos derivados                                         |
| **UI**           | Presencia, visibilidad y estado de elementos clave (sin comparación visual pixel a pixel ni responsive) |
| **Smoke**        | Verificación rápida del camino crítico                                                                |
| **Regresión**    | Re-ejecución de casos funcionales tras un cambio. Es un propósito de ejecución, no un tipo distinto   |
| **Exploratorias**| Sesiones manuales para descubrir escenarios y alimentar el diseño                                     |

**Técnicas de diseño:** partición de equivalencia, análisis de valores límite, tabla de decisión, transición de estados y pruebas exploratorias.

---

## Criterio de automatización

Un caso se automatiza cuando cumple la mayoría de estas condiciones:

| Criterio                | Pregunta                                                     |
| ----------------------- | ------------------------------------------------------------ |
| **Determinismo**        | ¿El resultado esperado es siempre el mismo?                  |
| **Riesgo / criticidad** | ¿Su falla afectaría el flujo principal?                      |
| **Frecuencia**          | ¿Se ejecutará repetidamente?                                 |
| **Estabilidad**         | ¿La funcionalidad cambia poco?                               |
| **Costo de mantenimiento** | ¿Es barato de mantener a largo plazo?                     |
| **Alternativa mejor**   | ¿Se puede validar mejor en otro nivel (por ejemplo, API)?    |

**No todo se automatiza.** Un caso que requiere juicio humano, es exploratorio o es muy inestable permanece manual, y se documenta la razón. En cada caso de prueba, el campo **Automatizar** registra la decisión y su justificación.

---

## Priorización

La **prioridad** indica qué tan importante es probar un caso. No es lo mismo que la *severidad*, que aplica a los defectos.

| Nivel  | Definición                                                                                                  | Cuándo se ejecuta                         |
| ------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **P0** | Sin esto no se puede completar el flujo principal (iniciar sesión y comprar)                                | En cada cambio (suite **smoke**)          |
| **P1** | Funcionalidad importante, validaciones y escenarios negativos relevantes; el flujo principal puede continuar | En la suite de **regresión**              |
| **P2** | Funcionalidad secundaria, casos de borde poco probables o aspectos cosméticos                               | En la regresión completa o cuando hay tiempo |

Para asignar el nivel se evalúa *"¿qué pasaría si esto falla en producción?"*. Ante la duda entre dos niveles, se asigna el más alto. Que un caso sea P0 no implica automatizarlo de forma automática: la decisión sigue los criterios de automatización.

---

## Trazabilidad

La relación entre diseño, automatización y resultados sigue este modelo:

```text
Requisito → Escenario → Caso de prueba → Test automatizado → Resultado de ejecución → Defecto
```

La [matriz de trazabilidad](docs/trazabilidad.md) registra, para cada caso: requisito, escenario, prioridad, si se automatiza, nombre del test y estado.

---

## Estructura del repositorio

> Estructura actual y prevista. Los elementos marcados como *(planeado)* se crearán conforme avance el proyecto.

```text
.
├── README.md
├── pytest.ini               # Configuración de pytest y markers (smoke, regression)
├── requirements.txt         # Dependencias
├── docs/                    # Diseño y documentación de pruebas
│   ├── TEST_PLAN.md
│   ├── trazabilidad.md
│   └── login/
│       ├── requisitos_login.md
│       ├── escenarios_login.md
│       └── test_case_Login.md
│
├── pages/                   # Page Objects
│   └── login_page.py
├── tests/                   # Tests automatizados
│   └── login/
│       └── test_login.py
├── conftest.py              # Fixtures de pytest (planeado)
├── data/                    # Datos de prueba (planeado)
└── evidence/                # Capturas, trazas y videos (planeado)
```

---

## Ejecución

```bash
# Instalar dependencias y navegadores
pip install -r requirements.txt
playwright install

# Suite smoke (casos P0)
pytest -m smoke

# Suite de regresión
pytest -m regression

# Todos los tests
pytest
```

---
