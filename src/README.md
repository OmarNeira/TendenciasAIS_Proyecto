# 🌟 Tendencias Avanzadas en Ingeniería de Software: Proyecto ETL Dashboard 🌟

Este proyecto fue desarrollado como parte de la materia **Tendencias Avanzadas de Ingeniería de Software** y tiene como objetivo principal la creación de un **dashboard** para un proceso ETL.

---

## 🛠️ Herramientas Requeridas

- **Python** (última versión) 🐍  
- **PostgreSQL** (última versión) 🐘  
- IDE de desarrollo compatible con Python (recomendado: **VSCode**) 💻  

---

## 🚀 Pasos para Ejecutar el Programa

### 🗄️ Configuración de PostgreSQL
1. **Crear una base de datos:**
   - Nombre recomendado: `tendenciasAIS` (default, pero puede ser cambiado en el archivo `db.py`).
2. **Actualizar credenciales:**
   - Configura el archivo `db.py` con las credenciales de tu base de datos si las predeterminadas no aplican.

### 🐍 Configuración de Python
1. **Acceder a la carpeta del proyecto:**
   - Abre la terminal en modo administrador y navega al directorio `src` del proyecto con:
     ```bash
     cd ...path/TendenciasAIS_Proyecto/src
     ```
     *(Reemplaza `...path` con la ruta donde descargaste el proyecto).*
2. **Crear un entorno virtual:**
   - Ejecuta el siguiente comando:
     ```bash
     python -m venv .venv
     ```
3. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
4. **Instalar dependencias:**
   - Ejecuta:
     ```bash
     pip install -r requirements.txt
     ```

---

## 📊 Actualización de la Base de Datos

1. **Ejecutar el script de configuración:**
   - Corre el archivo `db.py` con el siguiente comando:
     ```bash
     python db.py
     ```
   **Nota:** Si tienes problemas al ejecutar desde la terminal, se recomienda usar la extensión de Python de **VSCode** para correr directamente el archivo desde el IDE.

---

## 📈 Ejecución del Dashboard

1. **Ejecutar el archivo principal:**
   - Corre el archivo `dashboard.py` con el siguiente comando:
     ```bash
     python dashboard.py
     ```
   **Nota:** Al igual que con `db.py`, si se presentan fallas, usa la extensión de Python de **VSCode** para ejecutar el archivo.

2. **Visualización del Dashboard:**
   - Al ejecutarse correctamente, se abrirá un navegador (recomendado: **Google Chrome**) con las gráficas generadas por el programa.

---

## 🧩 Notas Adicionales

- Si deseas cambiar el nombre de la base de datos o las credenciales, asegúrate de actualizar el archivo `db.py`.
- Asegúrate de tener las versiones más recientes de Python, PostgreSQL y las librerías requeridas para evitar errores de compatibilidad.

---

## 🎯 ¿Qué Hace Este Proyecto?

- **Extrae datos** de una base de datos PostgreSQL.
- **Transforma la información** para responder preguntas clave relacionadas con ventas y categorías.
- **Carga y visualiza los resultados** en un dashboard interactivo que incluye gráficas de barras.

---

## 📝 Autor(es)
Proyecto realizado como parte del curso **Tendencias Avanzadas en Ingeniería de Software**. 🎓