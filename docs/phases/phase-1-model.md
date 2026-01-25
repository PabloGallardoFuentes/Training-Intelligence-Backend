# FASE 1 — Definición conceptual

## Objetivo de la fase
Representar la realidad con el mínimo número de conceptos posibles, sin anticipar el futuro.

## Pregunta núcleo
> Qué cosas existen de verdad en este sistema

Una sesión registrada a posteriori

## 1️⃣ Entidad centratl: TrainingSession
#### Modelo propuesto
```text
TrainingSession
- date
- sport
- duration_minutes
- intensity
```

Campor por campo

```date```
- Necesario y clave para agregación semanal
- La sesión pertenece a un único día, no puede cruzar media noche

```sport```
- Valores cerrados: swim, bike, run
- El sistema podrá comparar deportes.
- Aceptar cualquier cosa rompe señales futuras.
- Triatlón ≠ “actividad física genérica”

Enum desde el día 1.

```duration_minutes```
- Usando minutos obtengo suficiente precisión.
- Evitar floats raros
- Estable para agregación semanal

```intensity```
- Escala cerrada. RPE de 1-10
- Ordinal, no continua
- Subjetiva
- No depende de sensores

Mantiene un sistema robusto

## 2️⃣ Campos que NO añadimos (y por qué)

❌ ```load```
- Es derivable
- Meterlo ahora acopla fórmula y datos
- La fórmula **puede cambiar**

❌ ```week```
- Es una vista que se calcula

❌ ```notes```
- No se utilizan
- Introducen subjetividad no procesable

❌ ```completed / planned```
- No se modela la intención todavía

❌ ```athlete_id```
- Single-user system
- Premature abstraction

## 3️⃣ Primera métrica

```load = duration_minutes x intensity```
📌 Importante:
- no es un campo
- es una función pura
- vive en el dominio, no en la entidad

## 4️⃣ Script de la semana 1 
Qué hace (y qué NO)

✔️ Lee sesiones (CSV / JSON / hardcoded) **JSON en FASE 1**

✔️ Calcula carga diaria

✔️ Agrega por semana

✔️ Imprime algo interpretable


❌ No DB

❌ No API

❌ No framework

Ejemplo de output aceptable:
```text
Week 2026-03-04
Total load: 1340
Swim: 320
Bike: 540
Run: 480
```

## 5️⃣ Decisión crítica: definición de semana
>¿Cómo defines una semana?
Opciones:
- ISO week (lunes–domingo)
- rolling 7 days
- configurable

Para FASE 1:
ISO week, fija no configurable 

¿Por qué?
- reduce ambigüedad
- alinea con planificación real
- simplifica tests

## Estado final de la fase
✔️ Fase cerrada