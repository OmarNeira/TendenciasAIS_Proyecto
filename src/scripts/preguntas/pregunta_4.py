import pandas as pd

#Clase que define un filtro de los JSON para la pregunta 4
#¿Qué productos en la categoría deportes tienen el mayor precio y stock disponible?

#Categoria deportes MCO441480

class pregunta_4():
    def getQuery(self):
        """
        Debe ser un filtro a lo recogido de la DB con Panda para que lo grafique Bokeh
        """
        return """
            SELECT 
                p.id AS producto_id,
                p.category_id AS categoria_id,
                p.available_quantity AS cantidad_disponible,
                p.name AS producto_name,
                p.price AS precio
            FROM 
                producto p
            WHERE p.category_id = 'MCO441480' -- ID de la categoría de deportes
        """
    
    def filtrarJSONPregunta(self, rows, colnames):
        """
        Filtra el DataFrame para encontrar los productos en la categoría deportes
        con el mayor precio y stock disponible.

        Args:
            df (pd.DataFrame): DataFrame con las columnas de la consulta SQL.

        Returns:
            pd.DataFrame: DataFrame filtrado con los productos en la categoría deportes.
        """
        try:
            print("Filtrando JSON para pregunta 4")
            df = pd.DataFrame(rows, columns=colnames)
            print(df.head(2))

            # Asegurarse de que 'precio' y 'cantidad_disponible' sean de tipo float
            df['precio'] = df['precio'].astype(float)
            df['cantidad_disponible'] = df['cantidad_disponible'].astype(float)

            # Ordenar por precio y cantidad disponible
            df = df.sort_values(by=['precio', 'cantidad_disponible'], ascending=[False, False])

            # Seleccionar los productos con mayor precio y stock disponible
            top_productos = df.head(10)
            print("Productos en la categoría deportes con mayor precio y stock disponible:")
            print(top_productos)
            return top_productos

        except KeyError as e:
            print(f"Error: La columna {e} no se encuentra en el DataFrame. Verifica los nombres de las columnas.")
            return pd.DataFrame()

        except Exception as e:
            print(f"Error inesperado: {e}")
            return pd.DataFrame()