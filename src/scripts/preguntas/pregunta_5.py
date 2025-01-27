import pandas as pd

#Clase que define un filtro de los JSON para la pregunta 5
#¿Cuáles son los 3 productos reacondicionados con más calificaciones en la categoría de electrodomésticos?

class pregunta_5():
    def getQuery(self):
        """
        Debe ser un filtro a lo recogido de la DB con Panda para que lo grafique Bokeh
        """
        return """
            SELECT 
                p.id AS producto_id,
                p.name AS producto_name,
                p.calificacion AS calificacion,
                p.cant_calificaciones AS cant_calificaciones,
                p.categoria AS categoria,
                p.subcategoria AS subcategoria,
                p.condicion AS condicion
            FROM 
                producto2 p
            WHERE p.categoria = 'Electrodomesticos' AND p.condicion = 'Reacondicionado' -- ID de la categoría de electrodomésticos
        """
    
    def filtrarJSONPregunta(self, rows, colnames):
        """
        Filtra el DataFrame para encontrar los 3 productos reacondicionados con más calificaciones
        en la categoría de electrodomésticos.

        Args:
            df (pd.DataFrame): DataFrame con las columnas de la consulta SQL.

        Returns:
            pd.DataFrame: DataFrame filtrado con los 3 productos reacondicionados con más calificaciones.
        """
        try:
            print("Filtrando JSON para pregunta 5")
            df = pd.DataFrame(rows, columns=colnames)
            print(df.head(2))

            # Asegurarse de que 'cant_calificaciones' y 'calificacion' sean de tipo float
            df['cant_calificaciones'] = pd.to_numeric(df['cant_calificaciones'], errors='coerce').fillna(0)
            df['calificacion'] = pd.to_numeric(df['calificacion'], errors='coerce').fillna(0)

            # Ordenar por cantidad de calificaciones y calificación
            df = df.sort_values(by=['cant_calificaciones', 'calificacion'], ascending=[False, False])

            # Seleccionar los 3 productos con más calificaciones
            top_productos = df.head(3)
            print("Top 3 productos reacondicionados con más calificaciones en la categoría de electrodomésticos:")
            print(top_productos)
            return top_productos

        except KeyError as e:
            print(f"Error: La columna {e} no se encuentra en el DataFrame. Verifica los nombres de las columnas.")
            return pd.DataFrame()

        except Exception as e:
            print(f"Error inesperado: {e}")
            return pd.DataFrame()