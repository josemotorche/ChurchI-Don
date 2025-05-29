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

2. Agregue un miembro:

```bash
python3 chms.py add-member Juan Perez --email jperez@example.com --phone 555-1234
```

3. Liste los miembros registrados:

```bash
python3 chms.py list-members
```

4. Registre un estatus de crecimiento espiritual para un miembro:

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

Este ejemplo es una base sencilla que puede ampliarse para incluir autenticación, interfaz web u otras funcionalidades propias de un ChMS completo.

## Servidor Express

Se incluye un servidor de ejemplo en `server/` que expone una API protegida con JWT para manejar registros financieros.

### Instalación

En la carpeta `server` instale las dependencias y arranque el servicio:

```bash
cd server
npm install
node index.js
```

### Endpoints de Finanzas

Todas las rutas requieren un token JWT obtenido desde `/api/login`.

- `POST /api/finances` – crea un registro financiero.
- `GET /api/finances` – lista los registros de la iglesia del usuario.
- `GET /api/finances/:id` – obtiene un registro específico.
- `PUT /api/finances/:id` – actualiza un registro.
- `DELETE /api/finances/:id` – elimina un registro.

La autenticación simple de demostración acepta `admin` / `password` y asigna `churchId` 1 al token.
