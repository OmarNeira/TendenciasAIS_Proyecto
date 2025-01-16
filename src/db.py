import psycopg2
import json

#Conexión a la base de datos
conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="",
    port=""
)

#Funcion que chekea la conexion a la base de datos
def check_connection():
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        print("Conexión exitosa")
        return True
    except(Exception, psycopg2.DatabaseError) as error:
        print("Conexión errada: ",error)
        return False

#Funcion que toma los json de una direccion predeterminada
def get_json(direccion):
    #Obtenemos los archivos de la direccion para iterar
    files = get_files(direccion)
    #Iteramos los archivos
    for file in files:
        #Abrimos el archivo
        with open(file) as json_file:
            data = json.load(json_file)
            #Iteramos el json
            for p in data['people']:
                print('Name: ' + p['name'])
                print('Website: ' + p['website'])
                print('From: ' + p['from'])
                print('')

#Funcion que recoge todos los archivos de una direccion y los retorna como un arreglo
def get_files(direccion):
    files = []
    with open(direccion) as file:
        for line in file:
            files.append(line)
    return files


check_connection()