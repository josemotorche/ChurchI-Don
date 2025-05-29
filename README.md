# ChurchI-Don

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

3. Liste los miembros registrados:

```bash
python3 chms.py list-members
```

4. Registre un estatus de crecimiento espiritual:

```bash
python3 chms.py add-growth 1 "Bautizado" --status-date 2024-05-18
```

5. Cree un grupo y asigne un miembro:

```bash
python3 chms.py add-group "Grupo Juvenil" --zone Norte
python3 chms.py assign-member 1 1
```

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
