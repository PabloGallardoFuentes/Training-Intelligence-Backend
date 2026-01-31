# FASE 3 — Señales de carga y fatiga (Training Load Signals)

## Objetivo

Extender el sistema actual de carga semanal para **derivar señales simples pero útiles**
relacionadas con la fatiga y el riesgo de sobrecarga, manteniendo:

- Dominio limpio
- Arquitectura escalable
- Testabilidad
- Cero lógica en controllers o repositorios

Esta fase NO busca hacer predicción ni recomendaciones automáticas, sino **exponer métricas**.

---

## Contexto

Actualmente el sistema permite:

- Registrar sesiones de entrenamiento
- Calcular la carga semanal total y por deporte
- Soportar múltiples usuarios
- Semana ISO como unidad temporal

Esto sienta la base para cálculos longitudinales.

---

## Señales a implementar

### 1️⃣ Weekly Load
Ya existente.

- Definición:
`load = duration_minutes * intensity`

- Agregado semanal por usuario

---

### 2️⃣ Rolling Average Load (Acute Load)

- Media móvil de carga semanal
- Ventana configurable (por defecto: 4 semanas)
- Incluye la semana actual

Ejemplo:
`acute_load = mean(week_n, week_n-1, week_n-2, week_n-3)`

---

### 3️⃣ Chronic Load

- Media móvil más larga
- Ventana configurable (por defecto: 8 semanas)

Ejemplo:
`chronic_load = mean(last 8 weeks)`

---

### 4️⃣ Load Ratio (Acute : Chronic)

Indicador clásico de sobrecarga.

`load_ratio = acute_load / chronic_load`

- Si `chronic_load == 0` → ratio = null
- No se interpreta ni se clasifica todavía

---

### 5️⃣ Monotony (Monotonía)

Medida de variabilidad semanal.

Definición:
monotony = mean(daily_loads) / std(daily_loads)

- Calculada **dentro de una semana**
- Requiere agrupar sesiones por día
- Si `std == 0` → monotony = null

---

## Alcance técnico

### Incluido
- Servicios de dominio para cálculo de señales
- Reutilización de repositorios existentes
- Nuevos endpoints de lectura
- Tests exhaustivos (unitarios y de integración)
- Configuración de ventanas vía parámetros

### Excluido (explícitamente)
- Reglas médicas
- Recomendaciones ("reduce carga", "descansa")
- Clasificaciones (verde / amarillo / rojo)
- Persistencia de métricas derivadas
- Frontend

---

## Arquitectura

### Dominio
- Nuevos value objects / DTOs de salida:
  - `WeeklyLoadSignal`
  - `LoadTrend`
- Lógica matemática vive aquí

### Servicios
- `LoadTrendService`
  - Orquesta llamadas a repositorio
  - Calcula medias móviles
  - Devuelve estructura agregada

### Repositorios
- Se reutilizan
- Se amplían queries si es necesario (rango de semanas)

### Routes
- Nuevos endpoints:
GET /users/{id}/load-trends



- Sólo adaptan HTTP → service

---

## API (borrador)

### GET /users/{user_id}/load-trends

**Query params**
- `year`
- `week`
- `acute_window` (default 4)
- `chronic_window` (default 8)

**Response**
```json
{
"iso_year": 2026,
"iso_week": 10,
"weekly_load": 420,
"acute_load": 380,
"chronic_load": 310,
"load_ratio": 1.22,
"monotony": 1.8
}
```

## Tests
### Unitarios
- Cálculo de media móvil
- Ratio con edge cases
- Monotonía con std = 0
- Semanas incompletas

Integración
- DB SQLite in-memory
- Varias semanas simuladas
- Multiuser isolation

---

## Criterios de cierre
- [ ] Todos los cálculos cubiertos por tests
- [ ] Endpoint estable y documentado
- [ ] No lógica matemática en routes
- [ ] Dominio independiente de FastAPI y SQLAlchemy
- [ ] README de fase actualizado

---
## Futuras extensiones (NO ahora)
- Z-score por atleta
- Tendencias por deporte
- Alertas configurables
- Persistencia histórica de señales
---