# FASE 0 — Definición conceptual

## Objetivo de la fase
Definir el problema real que el sistema intenta resolver antes de escribir código.

## Pregunta núcleo

> Cuando termina una semana de entrenamiento, ¿mi carga está evolucionando de forma coherente o estoy acumulando fatiga sin darme cuenta?

El sistema busca responder esta pregunta reduciendo ruido diario y evitando interpretaciones basadas únicamente en sensaciones o en métricas fisiológicas complejas.

## Decisiones tomadas
- Unidad temporal principal: semana
- No estimar métricas de rendimiento
- Foco en carga y señales tempranas

## Unidad de análisis

La **semana** es la unidad principal de verdad del sistema.

- Un día aislado (bueno o malo) no define un bloque de entrenamiento.
- Las señales relevantes emergen al observar tendencias semanales.
- El sistema tolera imperfecciones diarias siempre que la tendencia global sea coherente.

## Qué significa una “buena semana”

Para este sistema:
> Una semana buena es aquella cuya carga total es consistente con semanas anteriores y sigue la intención del bloque: progresiva en semanas de carga o regresiva en semanas de descarga.

No se evalúa el “éxito” de entrenamientos individuales, sino la coherencia de la carga agregada.

## Métrica base de carga

La carga de una sesión se define de forma simple como:

> load = duration_minutes × intensity

Esta métrica se elige porque:

- Es explicable sin modelos fisiológicos complejos.
- Permite comparar sesiones y deportes distintos bajo un marco común.
- Es estable a nivel semanal.
- Está suficientemente correlacionada con la fatiga acumulada cuando se observa de forma agregada.

La carga se utiliza como **proxy operativa**, no como representación exacta de fatiga fisiológica.

## Tradeoffs aceptados
- No se modela fatiga fisiológica real
- Se pierde sensibilidad diaria
- Se asume consistencia semanal como proxy válida

## Filosofía de diseño
- Señales antes que gráficos
- Explicabilidad antes que sofisticación
- Tendencias antes que valores puntuales
- Criterio antes que automatismo

El proyecto prioriza decisiones claras y defendibles frente a complejidad innecesaria.

## Decisiones aplazadas conscientemente
- Modelos fisiológicos
- Personalización por atleta
- Integración con sensores
- Carga de entrenamientos detallados

## Estado final de la fase
✔️ Fase cerrada