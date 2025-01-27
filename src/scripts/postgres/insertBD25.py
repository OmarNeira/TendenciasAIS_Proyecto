#Clase para insertar la informacion de las preguntas 2 y 5 en la base de datos
#Se usa pandas para leer los archivos json y psycopg2 para la conexion con la base de datos

import os
import pandas as pd

from scripts.postgres import DBcontroller as dbcontroller

class insertBD25():
    base_url = './src/repository/'

    #Funcion que recoge todos los archivos de una direccion y los retorna como un arreglo de direcciones
    def get_files(self,direccion):
        #Obtenemos los archivos de la direccion
        files = []
        for file in os.listdir(direccion):
            if file.endswith('.json'):
                files.append(direccion + file)
        return files
    
    def filtro_producto(self, row):
        """
        Extrae la información requerida de una fila del DataFrame.

        Args:
            row: Una serie que representa una fila del DataFrame.

        Returns:
            Un diccionario con los campos extraídos.
        """

        return {
            'id': row['id'],
            'name': row['nombre'],
            'envio': row['envio'],
            'calificacion': row['calificacion'],
            'cant_calificaciones': row['cant_calificaciones'],
            'condicion': row['condicion'],
            'categoria': row['categoria'],
            'subcategoria': row['subcategoria']
        }
    
    def crearDataFrame(self,pregunta,cur):
        #Creamos un objeto de la clase DBcontroller
        dbc = dbcontroller.DBcontroller()
        #PREGUNTA 2
        if(pregunta == "pregunta_2"):
            for json in self.get_files(self.base_url + pregunta + '/'):
                #Obtenemos el nombre del archivo
                nombre = json.split('/')[-1]
                #Si el nombre contiene en alguna parte productoP2 lo imprimimos
                if 'productoP2' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Producto P2 encontrado")
                    filtered_products = df.apply(self.filtro_producto, axis=1).tolist()
                    filtered_products_df = pd.json_normalize(filtered_products)
                    print(filtered_products_df)
                    for _, row in filtered_products_df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "producto2")
                else:
                    print(nombre, "no es un archivo JSON producto de p2")
        
        #PREGUNTA 5
        elif(pregunta == "pregunta_5"):
            for json in self.get_files(self.base_url + pregunta + '/'):
                #Obtenemos el nombre del archivo
                nombre = json.split('/')[-1]
                #Si el nombre contiene en alguna parte productoP2 lo imprimimos
                if 'productoP5' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Producto P5 encontrado")
                    filtered_products = df.apply(self.filtro_producto, axis=1).tolist()
                    filtered_products_df = pd.json_normalize(filtered_products)
                    print(filtered_products_df)
                    for _, row in filtered_products_df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "producto2")
                else:
                    print(nombre, "no es un archivo JSON producto de p5")
        else:
            print("Pregunta no encontrada")
            df = None

        print("Dataframe 2 creado")