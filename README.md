# Cancha Libre

// Descripción del proyecto

Cancha Libre es un sistema web desarrollado en Python utilizando el framework Django, cuyo objetivo es facilitar la gestión de reservas de canchas deportivas.

El sistema permite administrar clientes, canchas, actividades deportivas, reservas, pagos y cancelaciones.

Este proyecto fue desarrollado para la materia **Análisis y Metodologías de Sistemas**, correspondiente al segundo trabajo parcial.

// Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- GitHub

// Funcionalidades del sistema

- Registro y consulta de clientes.
- Registro y administración de canchas deportivas.
- Registro de actividades deportivas.
- Creación y consulta de reservas.
- Validación para evitar reservas superpuestas en una misma cancha, fecha y horario.
- Cancelación de reservas.
- Liberación de horarios al cancelar una reserva.
- Registro y consulta de pagos.
- Persistencia de datos mediante una base de datos SQLite.

// Arquitectura del sistema

El proyecto utiliza la arquitectura Modelo-Vista-Controlador (MVC), adaptada a la estructura de Django.

- **Modelo:** representa las entidades y permite interactuar con la base de datos.
- **Vista:** muestra la información mediante páginas HTML.
- **Controlador:** procesa las solicitudes, ejecuta las validaciones y administra las operaciones del sistema.

// Instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Crear un entorno virtual:

```bash
python -m venv .venv
```

4. Activar el entorno virtual en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

6. Aplicar las migraciones:

```bash
python manage.py migrate
```

7. Ejecutar el servidor:

```bash
python manage.py runserver
```

8. Abrir en el navegador:

http://127.0.0.1:8000/

// Metodología de trabajo

El desarrollo del proyecto se organizó utilizando un tablero Kanban en Trello, con seguimiento de las tareas y funcionalidades.

Se trabajó de manera iterativa, mediante sprints semanales, contemplando el desarrollo, las validaciones y las pruebas del sistema.

//Autor

Rodolfo Pedrouzo

// Materia

Análisis y Metodologías de Sistemas – Trabajo Parcial 2.