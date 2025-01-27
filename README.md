# 📊 Proyecto Tendencias Avanzadas en Ingeniería de Software

Este proyecto utiliza diversas herramientas para construir un proceso ETL (Extract, Transform, Load) con datos obtenidos de la **API de Mercado Libre**, análisis de HTML mediante **web scraping**, y visualización de resultados en un **dashboard interactivo**.  

---

## 🌐 Integración con Mercado Libre API
- **Configuración de la aplicación:** Se creó una aplicación dentro de **Mercado Libre Devs** para autenticar y realizar peticiones a la API, utilizando el `APP ID` y el `cliente secreto`.
- **Recolección de datos:** 
  - Se desarrollaron aplicaciones para autorizar y comunicar con la API, manejando un token de usuario.
  - Se implementó un sistema con límite configurable de tiempo y peticiones por minuto para respetar las políticas de la API.
  - Los datos se recopilaron hasta un máximo de 1000 páginas y se almacenaron localmente en archivos JSON para un análisis posterior.

---

## 🕵️‍♂️ Web Scraping con Beautiful Soup
- **Enfoque offline:** Debido a las restricciones de seguridad y políticas de Mercado Libre, se descargaron manualmente los archivos HTML de las categorías principales.
- **Extracción y procesamiento:** 
  - Se utilizó **Beautiful Soup** para analizar los archivos HTML, identificando y extrayendo la información relevante mediante filtros como `find_all`.
  - Los datos resultantes se almacenaron en formato JSON para facilitar su manejo y análisis.

---

## 🗄️ Construcción del Data Warehouse
- **Almacenamiento en PostgreSQL:** 
  - La información extraída de los JSON se procesó con **Pandas** y se cargó en tablas diseñadas para representar productos, tiendas y categorías.
  - Las tablas fueron estructuradas para responder preguntas clave relacionadas con ventas y productos.
- **Automatización:** 
  - Se utilizó la librería `psycopg2` para conectar Python con PostgreSQL y cargar los datos en las tablas.

---

## 📈 Dashboard Interactivo
- **Preparación de datos:** 
  - Se consultaron y procesaron datos del data warehouse utilizando `psycopg2` y `Pandas` para aplicar filtros, agrupaciones y ordenamientos.
- **Visualización:** 
  - Se empleó la herramienta **Bokeh** para construir gráficas interactivas que se despliegan en el navegador, brindando una interfaz clara y dinámica para analizar la información.

---

Este proyecto integra múltiples tecnologías y enfoques para realizar un proceso ETL robusto, desde la recolección de datos hasta su visualización en un dashboard interactivo.
