# Swag Labs — QA Automation basado en diseño de pruebas

![Estado](https://img.shields.io/badge/estado-en%20construcci%C3%B3n-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Playwright](https://img.shields.io/badge/Playwright-Python-green)
![pytest](https://img.shields.io/badge/pytest-framework-orange)

Proyecto personal de QA que demuestra un flujo completo de trabajo:

**analizar → diseñar pruebas → priorizar → decidir qué automatizar → implementar → ejecutar → reportar**

La idea central es que **la automatización se construye a partir del diseño de pruebas**, no al revés. Por eso este repositorio documenta el proceso completo, desde el **Test Plan** hasta los resultados de ejecución.

---

## Aplicación bajo prueba

|                |                            |
| -------------- | -------------------------- |
| **Aplicación** | Swag Labs (SauceDemo)      |
| **URL**        | https://www.saucedemo.com/ |
| **Tipo**       | E-commerce de demostración |

> Swag Labs es el medio para practicar habilidades transferibles de QA. El enfoque aplica a cualquier aplicación web.

---

## Stack

| Área                    | Herramienta                     |
| ----------------------- | ------------------------------- |
| Lenguaje                | Python                          |
| Framework de pruebas    | pytest                          |
| Automatización UI       | Playwright                      |
| Patrón de diseño        | Page Object Model (POM)         |
| Gestión de dependencias | requirements.txt                |
| Reportes                | HTML / Allure (según evolución) |
| Control de versiones    | Git + GitHub                    |

---

## Documentación

Todo el proceso de diseño de pruebas se encuentra en la carpeta [`docs/`](docs/):

| Documento                                  | Qué responde                                                                      |
| ------------------------------------------ | --------------------------------------------------------------------------------- |
| [Plan de pruebas](docs/plan-de-pruebas.md) | ¿Qué se prueba, qué no, cómo y por qué?                                           |
| Escenarios de prueba                       | ¿Qué comportamientos se quieren validar?                                          |
| Casos de prueba                            | ¿Cómo se valida cada comportamiento?                                              |
| Matriz de trazabilidad                     | ¿Qué requisitos, escenarios y casos están cubiertos y cuáles están automatizados? |
| Defectos                                   | ¿Qué problemas se encontraron durante las pruebas?                                |

> Los documentos sin enlace están **pendientes**; se agregan conforme avanza el proyecto.

---

## Alcance

### Dentro del alcance

| Módulo             | Qué se valida                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| **Authentication** | Login válido e inválido, campos obligatorios, usuarios bloqueados, logout y acceso sin autenticación    |
| **Products**       | Catálogo, detalle de producto, ordenamiento por nombre y precio, agregar y quitar productos del carrito |
| **Cart**           | Visualización, carrito vacío, indicador de cantidad, eliminar productos y continuar comprando           |
| **Checkout**       | Formulario, campos obligatorios, resumen de compra, precios, cancelación y confirmación de pedido       |

### Fuera del alcance

* Pruebas profundas de backend o base de datos
* Pruebas de API
* Seguridad avanzada y pruebas de penetración
* Carga, estrés y rendimiento a gran escala
* Integraciones reales con pasarelas de pago
* Pruebas exhaustivas en dispositivos móviles físicos

Estos puntos podrán incorporarse como extensiones del proyecto.

---

## Flujo de trabajo

El proyecto sigue un enfoque **QA-first**, donde el diseño de pruebas precede a la automatización.

```text
                    TEST PLAN
                        │
                        ▼
                    REQUISITOS
                        │
                        ▼
                    ESCENARIOS
                        │
                        ▼
                   TEST CASES
                        │
                        ▼
             MATRIZ DE TRAZABILIDAD
                        │
                        ▼
                PLAYWRIGHT TESTS
                        │
                        ▼
                  POM / FIXTURES
                        │
                        ▼
                    REPORTES
```

Este flujo representa la relación entre las actividades de análisis, diseño, automatización y ejecución.

### 1. Test Plan

Define el alcance general del proyecto:

* Objetivo de las pruebas
* Alcance y fuera de alcance
* Módulos a validar
* Tipos de pruebas
* Riesgos
* Estrategia
* Criterios de entrada y salida
* Criterios de automatización

### 2. Requisitos

Se identifican las funcionalidades y comportamientos que deben validarse.

Para este proyecto, los requisitos se derivan de la funcionalidad observable de Swag Labs y sirven como base para definir los escenarios y casos de prueba.

### 3. Escenarios

Los escenarios describen **qué comportamiento o flujo se desea validar**, sin entrar todavía en el nivel detallado de pasos.

Ejemplo:

> **ESC-AUTH-001:** Validar el inicio de sesión con credenciales válidas.

A partir de cada escenario pueden derivarse múltiples casos de prueba.

### 4. Test Cases

Los casos de prueba definen **cómo se validará cada escenario**.

Incluyen elementos como:

* ID
* Escenario
* Objetivo
* Precondiciones
* Datos de entrada
* Pasos
* Resultado esperado
* Tipo de prueba
* Prioridad

Ejemplo:

> **TC-AUTH-001:** Login exitoso con usuario y contraseña válidos.

### 5. Matriz de trazabilidad

La matriz permite relacionar los diferentes niveles del proceso y conocer qué parte del sistema está cubierta.

```text
Requisito
    ↓
Escenario
    ↓
Caso de prueba
    ↓
Test automatizado
    ↓
Resultado
    ↓
Defecto (si aplica)
```

La trazabilidad permite identificar:

* Qué funcionalidades están cubiertas.
* Qué casos están automatizados.
* Qué casos permanecen manuales.
* Qué pruebas fallaron.
* Qué defectos fueron encontrados por cada prueba.

### 6. Playwright Tests

Una vez definidos y priorizados los casos de prueba, se seleccionan aquellos que aportan valor al ser automatizados.

Los casos automatizados se implementan utilizando **Playwright + Python + pytest**.

La automatización no sustituye al diseño de pruebas; representa la implementación técnica de los casos seleccionados.

### 7. POM / Fixtures

La estructura técnica utiliza:

* **Page Object Model (POM)** para encapsular la interacción con las páginas.
* **Fixtures de pytest** para reutilizar configuración, contexto y recursos de prueba.
* **Datos de prueba** separados de la lógica cuando sea necesario.

Esto permite mantener los tests legibles, reutilizables y fáciles de mantener.

### 8. Reportes

Los resultados de ejecución se utilizan para comunicar:

* Pruebas ejecutadas.
* Pruebas exitosas.
* Pruebas fallidas.
* Evidencias.
* Errores encontrados.
* Defectos asociados.

La estrategia de reportes podrá evolucionar hacia **HTML y/o Allure** conforme avance el proyecto.

---

## Tipos de pruebas

El proyecto contempla diferentes tipos de pruebas según el riesgo y comportamiento que se quiera validar:

**Funcionales · Positivas · Negativas · Valores límite · Validación de campos · Manejo de errores · Smoke · Regresión · UI**

---

## Criterio de automatización

Un caso es candidato a automatizarse cuando:

* Es repetitivo.
* Pertenece a una funcionalidad crítica.
* Se ejecuta con frecuencia en regresión.
* Tiene pasos y resultados claramente definidos.
* Es relativamente estable.
* Aporta un beneficio claro frente a la ejecución manual.

**No todo se automatiza.**

Los casos que permanecen manuales también se documentan y se justifica la decisión.

---

## Priorización

| Nivel      | Significado                                |
| ---------- | ------------------------------------------ |
| **High**   | Funcionalidad crítica o de alto impacto    |
| **Medium** | Funcionalidad importante, pero no crítica  |
| **Low**    | Funcionalidad secundaria o de menor riesgo |

La prioridad considera factores como:

* Impacto
* Criticidad
* Frecuencia de uso
* Riesgo de falla
* Valor para regresión
* Facilidad de automatización

---

## Trazabilidad

La relación entre diseño, automatización y resultados sigue el siguiente modelo:

```text
Requisito
   ↓
Escenario
   ↓
Caso de prueba
   ↓
Test automatizado
   ↓
Resultado de ejecución
   ↓
Defecto
```

Esto permite mantener una relación clara entre **qué se necesita validar, cómo se valida y qué resultado se obtuvo**.

---

## Estructura del repositorio

> Estructura objetivo. Algunas carpetas y archivos se crearán conforme avance el proyecto.

```text
.
├── README.md
├── docs/                    # Diseño y documentación de pruebas
│   ├── plan-de-pruebas.md
│   ├── requisitos.md
│   ├── escenarios.md
│   ├── casos-de-prueba.md
│   ├── matriz-de-trazabilidad.md
│   └── defectos.md
│
├── pages/                   # Page Objects
├── tests/                   # Tests automatizados
├── data/                    # Datos de prueba
├── conftest.py              # Fixtures de pytest
└── requirements.txt         # Dependencias
```

---

## Posibles extensiones

El proyecto podrá evolucionar incorporando:

* Pruebas de API
* Accesibilidad
* Compatibilidad entre navegadores
* Datos de prueba externos
* Reportes Allure
* CI/CD con GitHub Actions
* Ejecución paralela
* Integración con herramientas de gestión de pruebas
* Pruebas adicionales de regresión

