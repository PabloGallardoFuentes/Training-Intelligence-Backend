# Training Intelligence Backend
## Propósito del proyecto

Este proyecto no intenta crear una aplicación completa de entrenamiento ni mejorar el plan de un entrenador.

Su objetivo es convertir entrenamientos diarios en señales semanales claras, que permitan entender la evolución de la carga y detectar posibles problemas antes de que se manifiesten como fatiga excesiva o abandono.

El foco está en entender y medir, no en prescribir ni optimizar.

## Pregunta que intenta responder

> Cuando termina una semana de entrenamiento, ¿mi carga está evolucionando de forma coherente o estoy acumulando fatiga sin darme cuenta?

El sistema busca responder esta pregunta reduciendo ruido diario y evitando interpretaciones basadas únicamente en sensaciones o en métricas fisiológicas complejas.

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

## Antiscope (qué NO hace este proyecto)

Este proyecto deliberadamente NO:
- ❌ Optimiza planes de entrenamiento
- ❌ Recomienda qué entrenar mañana
- ❌ Predice rendimiento en competición
- ❌ Estima métricas fisiológicas como FTP o ritmos críticos
- ❌ Evalúa técnica o biomecánica
- ❌ Incluye frontend o visualizaciones avanzadas
- ❌ Sustituye el criterio de un entrenador

Estas decisiones son conscientes y están documentadas para evitar deriva de alcance (*scope creep*).

## Filosofía de diseño
- Señales antes que gráficos
- Explicabilidad antes que sofisticación
- Tendencias antes que valores puntuales
- Criterio antes que automatismo

El proyecto prioriza decisiones claras y defendibles frente a complejidad innecesaria.

## Estado actual

#### FASE 0 — Definición conceptual
El modelo de datos, la API y las señales se desarrollarán en fases posteriores.