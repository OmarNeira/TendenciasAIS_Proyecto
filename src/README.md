**Tendencias Avanzadas de Ingeniería de Software: Dashboard ETL **
Descripción del Proyecto

Este proyecto, desarrollado como parte del curso de Tendencias Avanzadas de Ingeniería de Software, tiene como objetivo crear un dashboard interactivo  que visualice los resultados de un proceso ETL (Extract, Transform, Load).

Herramientas Requeridas

Python : Última versión estable.
PostgreSQL : Última versión estable.
IDE: Visual Studio Code (recomendado)
Configuración del Entorno

Base de Datos PostgreSQL:

Crear una base de datos llamada tendenciasAIS (o el nombre que prefieras).
Configurar las credenciales en el archivo db.py.
Entorno Virtual:

Windows:
Navegar al directorio del proyecto: cd ...path/TendenciasAIS_Proyecto/src
Crear el entorno: python -m venv .venv
Activar el entorno: .venv\Scripts\activate
Linux/macOS:
Los comandos son similares, pero las rutas pueden variar ligeramente.
Instalar Dependencias:

pip install -r requirements.txt
Ejecución del Proyecto

Actualizar la Base de Datos:

Recomendado: Ejecutar el archivo db.py directamente desde Visual Studio Code.
Alternativa: python db.py (ten en cuenta las posibles fallas mencionadas).
Iniciar el Dashboard:

Recomendado: Ejecutar el archivo dashboard.py directamente desde Visual Studio Code.
Alternativa: python dashboard.py (ten en cuenta las posibles fallas mencionadas).
Notas Importantes

Visual Studio Code: Se recomienda utilizar Visual Studio Code debido a su integración con Python y las herramientas de desarrollo de datos .
Fallas en la ejecución: Se han reportado algunas dificultades al ejecutar los scripts directamente desde la línea de comandos. Se sugiere utilizar Visual Studio Code para una experiencia más estable.
Salida: Al ejecutar el dashboard, se abrirá una ventana en tu navegador web mostrando las visualizaciones.