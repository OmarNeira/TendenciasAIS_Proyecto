import psycopg2

#Clase que define las funciones generales para el manejo de la base de datos
class DBcontroller():
    #Funcion para crear la tabla si no existe
    def crearTabla(self, cursor, nombreTabla, diccionario):
        # Map Python types to SQL types
        type_mapping = {
            int: "INTEGER",
            float: "FLOAT",
            str: "TEXT",
            bool: "BOOLEAN",
            type(None): "TEXT"
        }
        
        # Determine column types based on the dictionary values
        columnas = {key: type_mapping.get(type(value), "TEXT") for key, value in diccionario.items()}
        
        # Ensure 'id' and 'seller_id' are always set as TEXT and included as the primary key
        columnas['id'] = 'TEXT'
        if 'seller_id' in diccionario:
            columnas['seller_id'] = 'TEXT'
        
        #Creamos la query para crear la tabla
        query = f"""
        CREATE TABLE IF NOT EXISTS {nombreTabla} (
            {', '.join([f"{col} {dtype}" for col, dtype in columnas.items()])},
            PRIMARY KEY (id)
        )
        """
        try:
            #Ejecutamos la query
            cursor.execute(query)
            #Guardamos los cambios
            cursor.connection.commit()
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
            cursor.connection.rollback()

    #Funcion para insertar datos en la DB con psycopg2 y pandas
    def insertarDatos(self, cursor, diccionario, nombreTabla):
        # Crear la tabla si no existe
        self.crearTabla(cursor, nombreTabla, diccionario)
        
        # Remove 'id' from the dictionary keys for the insert query
        keys = list(diccionario.keys())
        keys.remove('id')
        
        #Creamos la query
        query = f"""
        INSERT INTO {nombreTabla} (id, {', '.join(keys)}) 
        VALUES (%s, {', '.join(['%s' for _ in keys])})
        ON CONFLICT (id) DO NOTHING
        """
        try:
            #Ejecutamos la query
            cursor.execute(query, [diccionario['id']] + [diccionario[key] for key in keys])
            #Guardamos los cambios
            cursor.connection.commit()
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")
            cursor.connection.rollback()