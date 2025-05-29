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

## Servidor Express (API)

El directorio `server/` contiene una implementación sencilla de una API REST en Node.js/Express con MongoDB. Incluye autenticación JWT y verificación del `iglesiaId` del usuario.

Para ejecutar el servidor primero cree un archivo `.env` con las variables `JWT_SECRET` y `MONGO_URL`:

```bash
cd server
# cree .env con sus valores
# JWT_SECRET=clave-secreta
# MONGO_URL=mongodb://localhost:27017/chms
```

Luego inicie el servidor:

```bash
npm start
```

Las rutas de miembros (`/api/members`) requieren un token JWT. El token debe incluir el campo `iglesiaId`. Cada operación crea, lee, actualiza o elimina miembros de la iglesia a la que pertenece el usuario autenticado.

