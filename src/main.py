from flask import Flask, render_template

# Crear la app Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    #Ejemplo de flask
    return render_template('index.html')