# 🧾 Plataforma Interna de Tareas (Flask + PostgreSQL)

## 🚀 Descripción
Aplicación interna para una PyME que permite a los empleados gestionar tareas, visualizar su estado y generar reportes simples.

## 🛠️ Tecnologías
- **Flask (Python)** – Backend API
- **PostgreSQL** – Base de datos relacional
- **SQLAlchemy** – ORM para conexión con la base
- **Adminer** – Visualización y administración de datos
- **Docker Compose** – Orquestación de contenedores

## ⚙️ Instalación y ejecución

1. Clonar el repositorio o copiar los archivos del proyecto.

2. Crear el archivo `.env` con las variables de entorno:
   ```bash
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=tasks_db
   API_PORT=5000

3. Levantar los servicios:
    docker compose up -d --build

4. Acceder a:
    API Flask: http://localhost:5000
    Adminer: http://localhost:8080
    Sistema: PostgreSQL
    Servidor: db
    Usuario: postgres
    Contraseña: postgres
    Base de datos: tasks_db

5. Para detener los contenedores:
    docker compose down

6. Para probar persistencia:
    docker compose down
    docker compose up -d
Los datos se conservarán gracias al volumen db_data.

## REINICIAR APP:
    docker compose down
    docker compose up --build -d

## 🧪 Endpoint de prueba
Crear tarea:
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"Revisión de reportes","status":"ToDo"}'

Listar tareas:
curl http://localhost:5000/tasks

---

## 📄 ** Documento de decisiones tecnológicas**

# 📘 Decisiones Tecnológicas y Justificación

## 🧱 Stack elegido: Flask + PostgreSQL + Adminer + Docker Compose

### Flask
- Framework liviano y modular de Python.
- Permite crear rápidamente una API REST con pocas dependencias.
- Fácil integración con SQLAlchemy para acceso a bases de datos.

### PostgreSQL
- Base de datos relacional avanzada, estable y gratuita.
- Compatible con estándares SQL y ORMs de Python.
- Ideal para datos estructurados y persistencia en contenedores.

### Adminer
- Herramienta de administración liviana, ideal para entornos Docker.
- Facilita la inspección de tablas y registros sin instalar pgAdmin.

### Docker Compose
- Simplifica el despliegue multi-contenedor.
- Garantiza portabilidad entre entornos (desarrollo, testing, producción).
- Permite declarar redes y volúmenes en un único archivo YAML.

### Decisiones clave
- Se usó un archivo `.env` para aislar credenciales y puertos.
- Se creó un volumen `db_data` para persistencia de información.
- Se usó una red `bridge` llamada `app-network` para aislar los servicios.

---

## 🏁 **Conclusiones**
- El sistema cumple con la modularidad y persistencia requeridas.  
- El stack elegido permite escalar o migrar a producción sin cambios significativos.  
- La estructura con Docker Compose facilita la corrección, reutilización y portabilidad del proyecto.
