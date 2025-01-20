import psycopg2

from scripts.postgres import insertBD134 as insertBD134
from scripts.postgres import insertBD25 as insertBD25

# Importamos todas las clases de filtrado de preguntas
from scripts.preguntas import pregunta_1 as pregunta1
from scripts.preguntas import pregunta_2 as pregunta2
from scripts.preguntas import pregunta_3 as pregunta3
from scripts.preguntas import pregunta_4 as pregunta4
from scripts.preguntas import pregunta_5 as pregunta5

class db():
    # Conexión a la base de datos
    conn = psycopg2.connect(
        database="tendenciasAIS",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )

    # Función que chekea la conexión a la base de datos
    def check_connection(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT 1")
            cur.close()
            print("Conexión exitosa")
            return True
        except(Exception, psycopg2.DatabaseError) as error:
            print("Conexión errada: ", error)
            return False

    def actualizarDB(self):
        # Chequeamos la conexión
        if self.check_connection():
            # Creamos un cursor
            cur = self.conn.cursor()
            # Creamos un objeto de la clase insertBD134 (para preguntas 1, 3 y 4)
            insert134 = insertBD134.insertBD134()
            self.actualizarDBPreguntas_134(cur, insert134)
            # Creamos un objeto de la clase insertBD25 (para preguntas 2 y 5)
            insert25 = insertBD25.insertBD25()
            self.actualizarDBPreguntas_25(cur, insert25)
            # Cerramos el cursor
            cur.close()

    # Función para actualizar la base de datos con las preguntas 1, 3 y 4
    def actualizarDBPreguntas_25(self, cur, insert25):
        # Cargamos los datos en la base de datos
        insert25.crearDataFrame(cur)

    # Función para actualizar la base de datos con las preguntas 1, 3 y 4
    def actualizarDBPreguntas_134(self, cur, insert134):
        # Creamos un diccionario con los datos de la tabla
        preguntas = ["pregunta_1", "pregunta_3", "pregunta_4", "categories"]
        # Cargamos los datos en la base de datos
        for pregunta in preguntas:
            insert134.crearDataFrame(pregunta, cur)

    def llamarBDSelectQuery(self, query):
        try:
            # Creamos un cursor
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            # Cerramos el cursor
            cur.close()
            return rows
        except psycopg2.Error as e:
            print(f"Error: {e}")
            return None

    # Diccionario de objetos de preguntas
    preguntas = {
        "pregunta_1": pregunta1.pregunta_1(),
        "pregunta_2": pregunta2.pregunta_2(),
        "pregunta_3": pregunta3.pregunta_3(),
        "pregunta_4": pregunta4.pregunta_4(),
        "pregunta_5": pregunta5.pregunta_5()
    }

    # Función para obtener la query de una pregunta y ejecutarlo en la bd
    def preguntarBD(self, pregunta):
        objeto = self.preguntas[pregunta]
        query = objeto.getQuery()
        try:
            # Creamos un cursor
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            # Obtener nombres de las columnas
            colnames = [desc[0] for desc in cur.description]
            df = self.preguntas[pregunta].filtrarJSONPregunta(rows,colnames)
            # Cerramos el cursor
            cur.close()
        except psycopg2.Error as e:
            print(f"Error: {e}")

        return df

    def dbPreguntar(self,pregunta):
        return self.preguntarBD(pregunta)

    # Función principal de la base de datos
    def main(self):
        print("Actualizando base de datos")
        print(self.preguntarBD("pregunta_1"))
        # self.actualizarDB()

if __name__ == "__main__":
    db_instance = db()
    db_instance.main()