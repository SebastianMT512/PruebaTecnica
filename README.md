# Prueba Tecnica UDNET Sebastian Morales Tarapues

# Conversor de Divisas API

Este es un **conversor de divisas** desarrollado con **Django Rest Framework (DRF)**.  
Permite gestionar monedas y tasas de cambio mediante una API RESTful.

---

## 🛠️ Stack Tecnológico

   **Backend:** Django 5 + Django Rest Framework  
   **Base de Datos:** PostgreSQL  
   **Documentación API:** DRF Spectacular (Swagger & ReDoc)  
   **Autenticación:** Django Default Auth  
   **Entorno Virtual:** Python `venv`  
   **ORM:** Django ORM  
   **Pruebas:** `unittest` con `APITestCase`

---

## 🏗️ Estructura del Proyecto

prueba_tecnica/
│── env/ # Entorno virtual
│── prueba_tecnica/ # Configuración principal de Django │
├── settings.py # Configuración global del proyecto │
├── urls.py # Enrutamiento principal │
├── wsgi.py # Servidor WSGI │
├── asgi.py # Servidor ASGI |
│── conversion/ # Aplicación principal │
├── migrations/ # Migraciones de base de datos │
├── serializer.py # Serializadores DRF │
├── urls.py # Rutas de la API │
├── views.py # Vistas (API) │
├── models.py # Modelos de datos │
├── tests.py # Pruebas │
│── manage.py # Script principal de Django
│── requirements.txt # Dependencias del proyecto
│── README.md # Documentación del proyecto
│── .gitignore # Archivos ignorados en Git

---

## 📄 Modelos de Datos

### ** Modelo `Currency` (Moneda)**

Representa una moneda con su código y nombre.

```python
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # Ejemplo: "USD", "EUR"
    name = models.CharField(max_length=50)  # Ejemplo: "Dólar estadounidense"

```

### ** Modelo ExchangeRate (Tasa de Cambio)**

Almacena la tasa de conversión entre dos monedas en una fecha específica.

```python

class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="base_rates")
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="target_rates")
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(auto_now_add=True)
```

## Características

 Gestión de monedas (`Currency`).  
 Gestión de tasas de cambio (`ExchangeRate`).  
 API documentada con **DRF Spectacular** (Swagger y ReDoc).  
 Base de datos en **PostgreSQL**.  
 Pruebas unitarias con `unittest`.

---

## Instalación y Configuración

### **Clonar el repositorio**

```sh
git clone https://github.com/SebastianMT512/PruebaTecnica.git
cd tu_repo
```

### **Crear entorno virtual e instalar dependencias**

```sh
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
pip install -r requirements.txt
```

### **Configurar variables de entorno** (`.env`)

Crea un archivo **`.env`** en la raíz del proyecto y agrega:

```ini
DB_NAME=tu_basedatos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=tu_clave_secreta
```

### **Aplicar migraciones y ejecutar servidor**

```sh
python manage.py migrate
python manage.py runserver
```

---

## Endpoints Principales

### **Monedas (`Currency`)**

| Método     | Endpoint                | Descripción               |
| ---------- | ----------------------- | ------------------------- |
| **GET**    | `/api/currencies/`      | Lista todas las monedas   |
| **POST**   | `/api/currencies/`      | Crea una moneda           |
| **GET**    | `/api/currencies/{id}/` | Ver una moneda específica |
| **PUT**    | `/api/currencies/{id}/` | Modificar una moneda      |
| **DELETE** | `/api/currencies/{id}/` | Eliminar una moneda       |

### **Tasas de Cambio (`ExchangeRate`)**

| Método     | Endpoint                    | Descripción                     |
| ---------- | --------------------------- | ------------------------------- |
| **GET**    | `/api/exchange-rates/`      | Lista todas las tasas de cambio |
| **POST**   | `/api/exchange-rates/`      | Crea una tasa de cambio         |
| **GET**    | `/api/exchange-rates/{id}/` | Ver una tasa específica         |
| **PUT**    | `/api/exchange-rates/{id}/` | Modificar una tasa              |
| **DELETE** | `/api/exchange-rates/{id}/` | Eliminar una tasa               |

---

## Documentación API

Puedes ver la documentación en estos endpoints:

-  **Swagger UI:** [https://pruebatecnica-sgak.onrender.com/api/docs/](https://pruebatecnica-sgak.onrender.com/api/docs/)
-  **ReDoc:** [https://pruebatecnica-sgak.onrender.com/api/redoc/](https://pruebatecnica-sgak.onrender.com/api/redoc/)
-  **Esquema OpenAPI (JSON):** [https://pruebatecnica-sgak.onrender.com/api/schema/](https://pruebatecnica-sgak.onrender.com/api/schema/)

---
