# Training Intelligence Backend

## Propósito del proyecto

Este proyecto **no intenta crear una aplicación completa de entrenamiento** ni mejorar el plan de un entrenador.

Su objetivo es **convertir entrenamientos diarios en señales semanales claras**, que permitan:

- entender la evolución de la carga
- detectar patrones de riesgo de forma temprana
- reducir autoengaño en la interpretación del entrenamiento

El foco está en **entender y medir**, no en prescribir ni optimizar.


---

## Estado del proyecto

- **Fase actual:** FASE 3 — Señales ✔️
- **Estado:** funcional, testeado y usable como backend
- **Siguiente fase (opcional):** FASE 4 — Observabilidad

El sistema ya:
- persiste sesiones de entrenamiento
- calcula carga semanal
- genera señales interpretables basadas en historial
- expone todo vía API HTTP


---

## Qué hace el sistema hoy

A partir de sesiones de entrenamiento simples (`date`, `sport`, `duration`, `intensity`), el sistema:

- calcula carga diaria y semanal
- agrega carga por deporte
- genera señales semanales como:
  - **Monotonía** (variabilidad diaria)
  - **Acute / Chronic Load Ratio** (relación entre carga reciente e histórica)
- devuelve **valores + interpretación humana**, no solo números

Todo el cálculo:
- es explicable
- es determinista
- está cubierto por tests


---

## Principios de diseño

- **Señales antes que gráficos**
- **Explicabilidad antes que sofisticación**
- **Dominio antes que framework**
- **Cálculo puro antes que orquestación**
- **Tendencias antes que valores puntuales**
- **Decisiones documentadas y reversibles**

La arquitectura prioriza:
- claridad conceptual
- separación de responsabilidades
- testabilidad
- evolución incremental


---

## Antiscope (qué NO hace este proyecto)

Este proyecto deliberadamente **NO**:

- ❌ Optimiza planes de entrenamiento
- ❌ Recomienda qué entrenar mañana
- ❌ Prescribe descansos o intensidades
- ❌ Predice rendimiento en competición
- ❌ Estima métricas fisiológicas (FTP, VO2max, ritmos críticos, etc.)
- ❌ Evalúa técnica o biomecánica
- ❌ Incluye frontend o visualizaciones avanzadas
- ❌ Sustituye el criterio de un entrenador

Estas decisiones son conscientes y están documentadas para evitar
**deriva de alcance (*scope creep*)**.


---

## Arquitectura (visión general)

El sistema sigue una arquitectura por capas clara:

- **Models (dominio):**
  - entidades puras (`TrainingSession`, `User`)
- **Repositories:**
  - acceso a datos (SQLAlchemy)
  - mapeo explícito ORM ↔ dominio
- **Services:**
  - cálculo de métricas
  - orquestación de señales
- **Routes:**
  - adaptadores HTTP (FastAPI)
- **Tests:**
  - unitarios, de servicio y de API

El dominio no depende de:
- FastAPI
- SQLAlchemy
- SQLite/PostgreSQL

---

## Fases del proyecto

- **FASE 0 — Definición conceptual** ✔️  
  Preguntas clave, alcance y antiscope.

- **FASE 1 — Modelo mínimo** ✔️  
  Entidades mínimas, carga simple y agregación semanal.

- **FASE 2 — Backend básico** ✔️  
  FastAPI, persistencia, repositorios, servicios y tests.

- **FASE 3 — Señales** ✔️  
  Señales semanales explicables basadas en historial.

- **FASE 4 — Observabilidad**
  Logging, validación avanzada, robustez operativa.


---

## Estado final de la FASE 3

Al cierre de esta fase, el proyecto puede considerarse:

> Un backend funcional y testeado que transforma datos de entrenamiento
> en señales semanales interpretables, sin prescripción ni predicción.

Este punto es **estable** y puede usarse como:
- base para producto
- proyecto demostrativo de nivel mid–senior
- sistema de análisis personal


---

## Nota final

Este proyecto prioriza **criterio técnico y claridad conceptual**
por encima de features o complejidad innecesaria.

Cada decisión está pensada para ser:
- justificable
- revisable
- reversible
