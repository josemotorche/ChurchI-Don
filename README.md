# ChurchI-Don


Este repositorio contiene un ejemplo de Sistema de Administración para Iglesias (Church Management System) de uso local.

El script `chms.py` implementa una base de datos SQLite y una interfaz de línea de comandos para registrar miembros, grupos, finanzas y certificados.

## Requisitos

- Python 3.8 o superior (incluye `sqlite3` y `argparse`). No se requieren dependencias externas.

## Uso

1. Inicialice la base de datos:

```bash
python3 chms.py init
```

2. Agregue una iglesia:

```bash
python3 chms.py add-church "Iglesia Central"
```

3. Agregue un miembro:


Este repositorio contiene un ejemplo de Sistema de Administración para Iglesias (Church Management System).

## Backend Express

Se incluye una API básica en `server/` implementada con Express y MongoDB. Debes instalar las dependencias con `npm install` dentro de esa carpeta y definir las variables de entorno `MONGO_URI` y `JWT_SECRET` en un archivo `.env`.

Para iniciar el servidor:

```bash
cd server
npm start
```

Las rutas principales son:

- `POST /api/auth/register` – registro de usuarios
- `POST /api/auth/login` – autenticación y obtención de token JWT
- `CRUD /api/members` – gestión de miembros protegida por JWT y verificación de iglesia

## CLI SQLite (opcional)

El script `chms.py` implementa una base de datos SQLite y una interfaz de línea de comandos para registrar miembros, grupos, finanzas y certificados.

### Requisitos

- Python 3.8 o superior (incluye `sqlite3` y `argparse`).

### Uso

1. Inicialice la base de datos:

```bash
python3 chms.py init
```

2. Agregue un miembro:


```bash
python3 chms.py add-member Juan Perez --email jperez@example.com --phone 555-1234
```


4. Liste los miembros registrados:

3. Liste los miembros registrados:


```bash
python3 chms.py list-members
```


5. Registre un estatus de crecimiento espiritual para un miembro:

4. Registre un estatus de crecimiento espiritual:


```bash
python3 chms.py add-growth 1 "Bautizado" --status-date 2024-05-18
```


6. Cree un grupo y asigne un miembro:
5. Cree un grupo y asigne un miembro:


```bash
python3 chms.py add-group "Grupo Juvenil" --zone Norte
python3 chms.py assign-member 1 1
```

7. Registre un ingreso o egreso:

```bash
python3 chms.py add-finance 1 income 1000 --description "Ofrenda"
```

8. Liste las finanzas de una iglesia:

```bash
python3 chms.py list-finances 1
```

9. Actualice una entrada financiera:

```bash
python3 chms.py update-finance 1 1 --amount 1200
```

10. Elimine una entrada financiera:

```bash
python3 chms.py delete-finance 1 1
```

11. Emita un certificado:

```bash
python3 chms.py certificate 1 Bautismo
```

La base de datos `chms.db` se guarda en el mismo directorio y puede ser consultada con cualquier cliente SQLite.

Este ejemplo es una base sencilla que puede ampliarse para incluir autenticación, interfaz web u otras funcionalidades propias de un ChMS completo.

6. Registre un ingreso o egreso:

```bash
python3 chms.py finance income 1000 --description "Ofrenda"
```

7. Emita un certificado:

```bash
python3 chms.py certificate 1 Bautismo
```

La base de datos `chms.db` se guarda en el mismo directorio y puede ser consultada con cualquier cliente SQLite.

Este ejemplo se puede ampliar para incluir más módulos o una interfaz web completa.

Este repositorio ahora incluye un ejemplo base de un sistema SaaS de administración de iglesias. Se provee un backend en Express/Mongo y un frontend en React con Tailwind.

## Estructura

- `server/` - API REST con autenticación JWT y modelos en MongoDB
- `client/` - Aplicación React con Vite y Tailwind CSS
- `chms.py` - Ejemplo previo de CLI con SQLite (opcional)

## Configuración del Backend

1. Copie `server/.env.example` a `server/.env` y ajuste las variables de conexión.
2. Desde la carpeta `server` ejecute:

```bash
npm install
npm run dev
```

La API quedará disponible en `http://localhost:5000`.

## Configuración del Frontend

1. Desde la carpeta `client` ejecute:

```bash
npm install
npm run dev
```

Esto inicia Vite y abre la app en `http://localhost:5173` (por defecto). La variable `VITE_API_URL` puede configurarse para apuntar al backend.

## Funcionalidades Iniciales

- Registro y login de usuarios con creación automática de la iglesia
- Almacén de usuarios con roles básicos (Admin, Pastor, Mentor, Miembro)
- Conexión básica entre frontend y backend usando fetch

Estas bases pueden ampliarse para incluir el resto de las entidades y paneles de administración descritos en la planificación del proyecto.
