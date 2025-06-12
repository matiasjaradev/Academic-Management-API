# Academic Management API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Nota**: Accede a la API en producción: [https://backend.matiasjara.dev](https://backend.matiasjara.dev)

# 📌 Descripción General
- Academic Management API es un sistema MVP desarrollado con FastAPI que permite gestionar información académica básica. Fue construido en aproximadamente 4 horas y actualmente se encuentra desplegado.
**Puedes visitar el APi en el siguiente enlace: [LINK](https://backend.matiasjara.dev)**

## 🌐 Despliegue
La API actualmente está desplegada en:  [LINK](https://backend.matiasjara.dev)

## 🔧 Características principales
- Gestión de entidades académicas básicas
- API RESTful con endpoints claramente definidos
- Autenticación y autorización JWT
- Integración con base de datos PostgreSQL
- Documentación automática interactiva
- Validación de datos con Pydantic v2

## 📋 Endpoints

### 🔐 Autenticación
| Método | Endpoint       | Descripción               | Requiere Auth | Parámetros |
|--------|----------------|---------------------------|---------------|------------|
| `POST` | `/register`    | Registrar nuevo usuario   | No            | `email`, `password` |
| `POST` | `/login`       | Iniciar sesión (JWT)      | No            | `email`, `password` |

### 👤 Usuarios
| Método | Endpoint          | Descripción                     | Requiere Auth | Permisos       |
|--------|-------------------|---------------------------------|---------------|----------------|
| `GET`  | `/users/me`       | Obtener usuario actual          | Sí            | Cualquier usuario |
| `GET`  | `/users/admin-only` | Ruta solo para administradores | Sí            | Rol: Admin     |

### 🎓 Estudiantes
| Método | Endpoint                  | Descripción                          | Requiere Auth | Parámetros |
|--------|---------------------------|--------------------------------------|---------------|------------|
| `GET`  | `/students/`              | Listar todos los estudiantes         | No            | -          |
| `POST` | `/students/`              | Crear nuevo estudiante               | Sí            | `name`, `email`, etc. |
| `GET`  | `/students/subject_id`    | Filtrar estudiantes por asignatura   | No            | `subject_id` |
| `GET`  | `/students/(id)`          | Obtener estudiante por ID            | No            | `id`       |
| `PUT`  | `/students/(id)`          | Actualizar estudiante                | Sí            | `id`, campos a actualizar |
| `DELETE` | `/students/(id)`        | Eliminar estudiante                  | Sí            | `id`       |

### 📚 Asignaturas
| Método | Endpoint                  | Descripción                   | Requiere Auth | Parámetros |
|--------|---------------------------|-------------------------------|---------------|------------|
| `GET`  | `/subjects/`              | Listar todas las asignaturas  | No            | -          |
| `GET`  | `/subjects/subjects/(id)` | Obtener asignatura por ID     | Sí            | `id`       |

## 📦 Requisitos y Dependencias
Entorno
- Python 3.7+
- PostgreSQL 

### Dependencias principales
```text
fastapi==0.115.12
uvicorn==0.34.3
SQLAlchemy==2.0.41
psycopg2-binary==2.9.10
pydantic==2.11.5
```
### Dependencias de seguridad
```text
bcrypt==4.3.0
python-jose==3.5.0
passlib==1.7.4
cryptography==45.0.3
```
### Dependencias Auxilares
```text
python-dotenv==1.1.0
python-multipart==0.0.20
```
-----------
## Instalación y configuración
- Clonar repositorio
```text
git clone [url-del-repositorio]
cd academic-management-api
```
- Crear y activar entorno virtual (recomendado):
```text
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
- Instalar dependencias:
```text
pip install -r requirements.txt
```
- Configurar variables de entorno:
```text
cp .env.example .env
# Editar el archivo .env con tus credenciales
```
- Ejecuta la aplicación
```text
uvicorn main:app --reload
```
## ⚙️ Configuración (.env)
- DATABASE_URL=postgresql://user:password@localhost/dbname
- SECRET_KEY=tu_clave_secreta_jwt
- ALGORITHM=HS256

## 🔒 Autenticación
La API usa JWT (JSON Web Tokens) para autenticación. Incluye:
- BCrypt para hashing de contraseñas
- Tokens de acceso con expiración
- Protección de endpoints sensibles

## 🗃️ Base de Datos
- PostgreSQL en producción
- SQLAlchemy ORM para manejo de base de datos

## 📚 Documentación interactiva
Accede a la documentación automática:
- Swagger UI: http://localhost:8000/docs

3. **Sección de Contribución**

## 🤝 Cómo contribuir
1. Haz fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Add some feature'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia
Copyright © 2025 Matías Jara
Distribuido bajo la licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más información.
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## ✉️ Contacto
- Matías Jara - engineer@matiasjara.dev
- Github: [Matias Jara Dev](https://github.com/matiasjaradev)
- Portafolio: [Pagina Web](https://matiasjara.dev)

## 🎥 Contenido Educativo

Si te interesa aprender más sobre desarrollo de APIs con FastAPI y otros temas de programación, te invito a visitar mi canal de YouTube donde comparto:

- 🎓 Cursos completos paso a paso
- 🚀 Demostraciones de proyectos reales
- 💡 Consejos y mejores prácticas
- 🛠️ Tutoriales técnicos detallados

👉 [Canal de YouTube](https://youtube.com/matiasjaradev) 
