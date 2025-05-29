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

```bash
python3 chms.py add-member Juan Perez --email jperez@example.com --phone 555-1234
```

4. Liste los miembros registrados:

```bash
python3 chms.py list-members
```

5. Registre un estatus de crecimiento espiritual para un miembro:

```bash
python3 chms.py add-growth 1 "Bautizado" --status-date 2024-05-18
```

6. Cree un grupo y asigne un miembro:

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
