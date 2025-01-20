#Clase para insertar la informacion de las preguntas 1, 3 y 4 en la base de datos
#Se usa pandas para leer los archivos json y psycopg2 para la conexion con la base de datos

import os
import pandas as pd

from scripts.postgres import DBcontroller as dbcontroller

class insertBD134():
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

        brand_name = None
        color_value = None
        model_value = None

        for attr in row['attributes']:
            if attr['id'] == 'BRAND':
                brand_name = attr['value_name']
            elif attr['id'] == 'COLOR':
                color_value = attr['value_name']
            elif attr['id'] == 'MODEL':
                model_value = attr['value_name']

        return {
            'id': row['id'],
            'name': row['title'],
            'available_quantity': row['available_quantity'],
            'category_id': row['category_id'],
            'price': row['price'],
            'seller_id': row['seller']["id"],
            'combined_attributes': f"{brand_name}, {color_value}, {model_value}"
        }

    def filtro_tienda(self, row):
        """
        Extrae la información requerida de una fila del DataFrame.

        Args:
            row: Una serie que representa una fila del DataFrame.

        Returns:
            Un diccionario con los campos extraídos.
        """

        try:
            total_transacciones = row['seller_reputation']['transactions']['total']
            power_seller_status = row['seller_reputation']['power_seller_status']
        except KeyError:
            total_transacciones = None 
            power_seller_status = None 

        return {
            'id': row['id'],
            'name': row['nickname'],
            'total_transacciones': total_transacciones,
            'power_seller_status': power_seller_status
        }

    def crearDataFrame(self,pregunta,cur):
        #Creamos un objeto de la clase DBcontroller
        dbc = dbcontroller.DBcontroller()
        #PREGUNTA 1
        if(pregunta == "pregunta_1"):
            for json in self.get_files(self.base_url + pregunta + '/'):
                #Obtenemos el nombre del archivo
                nombre = json.split('/')[-1]
                #Si el nombre contiene en alguna parte productoP1 lo imprimimos
                if 'productoP1' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Producto P1 encontrado")
                    filtered_products = df.apply(self.filtro_producto, axis=1).tolist()
                    filtered_products_df = pd.json_normalize(filtered_products)
                    print(filtered_products_df)
                    for _, row in filtered_products_df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "producto")
                elif 'tiendaP1' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Tienda P1 encontrada")
                    filtered_stores = df.apply(self.filtro_tienda, axis=1).tolist()
                    filtered_stores_df = pd.json_normalize(filtered_stores)
                    print(filtered_stores_df)
                    for _, row in filtered_stores_df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "tienda")
                else:
                    print(nombre, "no es un archivo JSON producto o tienda de p1")
        
        #PREGUNTA 3
        elif(pregunta == "pregunta_3"):
            for json in self.get_files(self.base_url + pregunta + '/'):
                #Obtenemos el nombre del archivo
                nombre = json.split('/')[-1]
                #Si el nombre contiene en alguna parte productoP1 lo imprimimos
                if 'productoP3' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Producto P3 encontrado")
                    filtered_products = df.apply(self.filtro_producto, axis=1).tolist()
                    filtered_products_df = pd.json_normalize(filtered_products)
                    print(filtered_products_df)
                    for _, row in filtered_products_df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "producto")
                else:
                    print(nombre, "no es un archivo JSON producto o tienda de p3")
        #PREGUNTA 4
        elif(pregunta == "pregunta_4"):
            for json in self.get_files(self.base_url + pregunta + '/'):
                #Obtenemos el nombre del archivo
                nombre = json.split('/')[-1]
                #Si el nombre contiene en alguna parte productoP1 lo imprimimos
                if 'productoP4' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Producto P4 encontrado")
                    filtered_products = df.apply(self.filtro_producto, axis=1).tolist()
                    filtered_products_df = pd.json_normalize(filtered_products)
                    print(filtered_products_df)
                    for _, row in filtered_products_df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "producto")
                else:
                    print(nombre, "no es un archivo JSON producto o tienda de p4")
        #CATEGORIAS
        elif(pregunta == "categories"):
            for json in self.get_files(self.base_url + pregunta + '/'):
                #Obtenemos el nombre del archivo
                nombre = json.split('/')[-1]
                #Si el nombre contiene en alguna parte productoP1 lo imprimimos
                if 'categories' in nombre:
                    # Leer el archivo JSON a partir de su direccion
                    df = pd.read_json(json)
                    print("Categorias encontradas")
                    df = pd.json_normalize(df.to_dict(orient='records'))
                    print(df)
                    for _, row in df.iterrows():
                        dbc.insertarDatos(cur, row.to_dict(), "categories")
                else:
                    print(nombre, "no es un archivo JSON de categorias")
        else:
            print("No se ha encontrado la pregunta")
            df = None

        print("Dataframe creado")