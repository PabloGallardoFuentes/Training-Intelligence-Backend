# FASE 2 - BACKEND

## Objetivo de la fase
Pasar de lógica en scripts a un backend persistente, manteniendo:
- dominio limpio
- reglas claras
- decisiones reversibles
- multiuser desde el diseño

No buscamos features.\
Buscamos **estructura correcta**.

## 1️⃣ Nueva entidad conceptual: `User`
```text
User
- id
```
Sin nombre, sin email, sin contraseña, sin autenticación todavía. \
El usuario **existe como concepto**, no como sistema de login.

## 2️⃣ `TrainingSession` cambia mínimamente
```text
TrainingSession
- id
- id_user
- date
- sport
- duration_minutes
- intensity
```
👉 Observa:
- id_user no rompe nada
- los tests actuales siguen siendo válidos
- la lógica de carga no cambia
- pero el sistema ya es real

## 3️⃣ Regla de oro: Toda query es por usuario. Siempre.

Incluso si ahora:
- solo hay un user
- el token es falso
- el user_id es fijo

Esto evita el peor refactor que existe:\
👉 añadir multiuser a posteriori

## Multi-user design

Although the system is used by a single user in early phases,
the data model and API are designed to support multiple users.

Authentication and authorization are intentionally out of scope.
User identification is assumed to be provided externally.

Although dependency injection will eventually be used to resolve the current user, the API exposes the user identifier explicitly in early phases to keep contracts clear and avoid premature authentication complexity.

## `id_user` llega en el PATH
```bash
POST /users/{user_id}/sessions
```
Motivos de esta decisión:
- hace visible el multiuser
- no requiere auth
- es REST claro
- evita magia

## Estructura del proyecto
```text
src/
├── models/
├── repositories/
├── services/
├── controllers/
├── routes/
└── main.py
```
> models contiene entidades de dominio, no modelos ORM

---
El sistema es single-tenant en FASE 1–2, \
pero multiuser desde el modelo.
---

#### ¿Por qué no meter ORM en models/?

Porque entonces:

- el dominio depende del framework
- los tests se vuelven lentos
- pierdes control conceptual

Separarlos te da:\
✔️ claridad \
✔️ flexibilidad

### Objetivo del servicio
¿Cómo fue esta semana de entrenamiento para este usuario, en términos de carga?

```text
WeeklyLoadService
-----------------
Input:
- user_id: int
- iso_year: int
- iso_week: int

Output:
- total_load: int
- load_by_sport: dict[sport, int]
```