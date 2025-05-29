# ChurchI-Don

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
