# Swag Labs — QA Automation basado en diseño de pruebas

![Estado](https://img.shields.io/badge/estado-en%20construcci%C3%B3n-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Playwright](https://img.shields.io/badge/Playwright-Python-green)
![pytest](https://img.shields.io/badge/pytest-framework-orange)

Proyecto personal de QA que demuestra un flujo completo de trabajo: **analizar → diseñar pruebas → priorizar → decidir qué automatizar → implementar → ejecutar → reportar**.

La idea central es que **la automatización se construye a partir del diseño de pruebas**, no al revés. Por eso este repositorio documenta el proceso completo, no solo los scripts.

---

## Aplicación bajo prueba

| | |
|---|---|
| **Aplicación** | Swag Labs (SauceDemo) |
| **URL** | https://www.saucedemo.com/ |
| **Tipo** | E-commerce de demostración |

> Swag Labs es el medio para practicar habilidades transferibles de QA. El enfoque aplica a cualquier aplicación web.

---

## Stack


| Área | Herramienta |
|---|---|
| Lenguaje | Python |
| Framework de pruebas | pytest |
| Automatización UI | Playwright |
| Patrón de diseño | Page Object Model (POM) |
| Reportes | HTML / Allure (según evolución) |
| Control de versiones | Git + GitHub |

---

## Documentación

Todo el proceso de diseño de pruebas está en la carpeta [`docs/`](docs/):

| Documento | Qué responde |
|---|---|
| [Plan de pruebas](docs/plan-de-pruebas.md) | ¿Qué se prueba, qué no, cómo y por qué? |
| Escenarios de prueba | ¿Qué comportamientos se quieren validar? |
| Casos de prueba | ¿Cómo se valida cada comportamiento? |
| Matriz de cobertura | ¿Qué está cubierto y qué está automatizado? |
| Defectos | ¿Qué problemas se encontraron? |

> Los documentos sin enlace están **pendientes**; se agregan conforme avanza el proyecto.

---

## Alcance

### Dentro del alcance

| Módulo | Qué se valida |
|---|---|
| **Authentication** | Login válido e inválido, campos obligatorios, usuarios bloqueados, logout, acceso sin autenticación |
| **Products** | Catálogo, detalle de producto, ordenamiento por nombre y precio, agregar y quitar del carrito |
| **Cart** | Visualización, carrito vacío, indicador de cantidad, eliminar productos, continuar comprando |
| **Checkout** | Formulario, campos obligatorios, resumen de compra, precios, cancelación, confirmación de pedido |
| **Navigation** | Menú lateral, logout, navegación entre pantallas, Reset App State |

### Fuera del alcance

- Pruebas profundas de backend o base de datos
- Pruebas de API
- Seguridad avanzada y pruebas de penetración
- Carga, estrés y rendimiento a gran escala
- Integraciones reales con pasarelas de pago
- Pruebas exhaustivas en dispositivos móviles físicos

Estos puntos podrán incorporarse como extensiones del proyecto.

---

## Enfoque de trabajo

```
Funcionalidad
   ↓
Exploración de la aplicación
   ↓
Identificación de módulos
   ↓
Escenarios de prueba
   ↓
Casos de prueba
   ↓
Priorización
   ↓
Cobertura
   ↓
Selección de casos automatizables
   ↓
Implementación con Playwright
   ↓
Ejecución → Resultados → Reporte de defectos
```

### Tipos de pruebas

Funcional · Positivas · Negativas · Valores límite · Validación de campos · Manejo de errores · Smoke · Regresión · UI

### Criterio de automatización

Un caso es candidato a automatizarse cuando:

- Es repetitivo.
- Pertenece a una funcionalidad crítica.
- Se ejecuta con frecuencia en regresión.
- Tiene pasos y resultados claramente definidos.
- Es relativamente estable.
- Aporta un beneficio claro frente a la ejecución manual.

**No todo se automatiza.** Los casos que se quedan manuales también se documentan con su justificación.

### Priorización

| Nivel | Significado |
|---|---|
| **High** | Funcionalidad crítica o de alto impacto |
| **Medium** | Importante, pero no crítica |
| **Low** | Secundaria o de menor riesgo |

Se evalúa por impacto, criticidad, frecuencia de uso, riesgo de falla, valor para regresión y facilidad de automatización.

### Trazabilidad

```
Escenario → Caso de prueba → Test automatizado → Resultado de ejecución → Defecto (si aplica)
```

Cada defecto puede rastrearse hasta el caso que lo detectó.

---

## Estructura del repositorio

> Estructura objetivo. Algunas carpetas se crearán conforme avance el proyecto.

```
.
├── README.md
├── docs/                  # Diseño de pruebas
│   └── plan-de-pruebas.md
├── pages/                 # Page Objects
├── tests/                 # Tests automatizados
├── data/                  # Datos de prueba
├── conftest.py            # Fixtures de pytest
└── requirements.txt
```

---


## Posibles extensiones

Pruebas de API · Accesibilidad · Compatibilidad entre navegadores · CI/CD con GitHub Actions
