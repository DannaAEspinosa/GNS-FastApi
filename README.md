# API de Productos con FastAPI

## ¿Qué hace este proyecto?

Este proyecto es una API básica para gestionar productos usando **FastAPI**.  
Permite crear, consultar, actualizar (completo y parcial) y eliminar productos en un almacenamiento en memoria (diccionario Python).  

Ideal para entender el manejo de rutas REST y validación con **Pydantic**, perfecto para aprender o hacer prototipos rápidos.

---

## Estructura del proyecto
```bash
/GNS-FastApi
│
├── app
│ ├── init.py
│ ├── models.py # Define los modelos Product y ProductUpdate con Pydantic
│ ├── routes
│ │ ├── init.py
│ │ └── products.py # Define las rutas CRUD para productos
│ └── database.py # Base de datos en memoria (diccionario) simulando almacenamiento
│
├── main.py # Punto de entrada de la app FastAPI, incluye router
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo
```

## Cómo correrlo localmente (sin Docker)

1. Clona o descarga el proyecto.  
2. Abre la terminal en la carpeta raíz (`GNS`).  
3. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Linux / Mac
source venv/bin/activate
# Librerias
pip install -r requirements.txt
# Correr localmente
uvicorn main:app --reload
```
## Cómo correrlo localmente (Docker)
Construir la imagen
```bash
docker build -t fastapi-products .
```
Correr el contenedor
```bash
docker run -d -p 8000:8000 fastapi-products
```








