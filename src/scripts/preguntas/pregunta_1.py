import pandas as pd

#Clase que define un filtro de los JSON para la pregunta 1
#¿De las tiendas con mayores ventas y mejores categorías de vendedor, 
#cuál es el precio de sus productos con más unidades disponibles en la categoría de computación?

class pregunta_1():
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
                p.price AS precio,
                t.id AS tienda_id,
                t.name AS tienda_name,
                t.power_seller_status AS categoria,
                t.total_transacciones AS cant_ventas
            FROM 
                producto p
            INNER JOIN tienda t ON p.seller_id = t.id
        """
    
    categoria_computacion = 'MCO82067'
    categoria_orden = ["platinum", "gold", "silver", "none"]

    def filtrarJSONPregunta(self, rows, colnames):
        """
        Filtra el DataFrame para encontrar las top 5 tiendas con mayores ventas
        y mejores categorías de vendedor, mostrando sus productos con más unidades disponibles
        en la categoría de computación.

        Args:
            df (pd.DataFrame): DataFrame con las columnas de la consulta SQL.
            categoria_computacion (str): ID de la categoría de computación (como texto).

        Returns:
            pd.DataFrame: DataFrame filtrado con las top 5 tiendas y sus mejores productos.
        """
        try:
            print("Filtrando JSON para pregunta 1")
            df = pd.DataFrame(rows, columns=colnames)
            print(df.head(2))
            # Asegurarse de que 'categoria_id' sea de tipo string
            df['categoria_id'] = df['categoria_id'].astype(str)

            # Filtrar solo productos en la categoría de computación
            df_computacion = df[df['categoria_id'] == self.categoria_computacion]

            # Verificar si hay datos tras el filtrado
            if df_computacion.empty:
                print(f"No se encontraron productos en la categoría '{self.categoria_computacion}'.")
                return pd.DataFrame()

            # Reemplazar valores nulos en 'categoria' con 'none'
            df_computacion['categoria'] = df_computacion['categoria'].fillna('none')

            # Ordenar por categoría de vendedor (mejor categoría primero) y total de ventas
            df_computacion['categoria'] = pd.Categorical(df_computacion['categoria'], categories=self.categoria_orden, ordered=True)
            print("Ordenando por categoría...")
            print(df_computacion.head(2))
            df_computacion = df_computacion.sort_values(by=['categoria', 'cant_ventas'], ascending=[True, False])
            print("Ordenando por categoría y ventas...")
            print(df_computacion.head(10))

            # Encontrar el producto con más unidades disponibles por tienda sin perder el orden
            df_computacion['rank'] = df_computacion.groupby('tienda_id')['cantidad_disponible'].rank(method='first', ascending=False)
            top_productos_por_tienda = df_computacion[df_computacion['rank'] == 1].drop(columns=['rank'])

            # Seleccionar las 5 primeras tiendas
            top_5_tiendas = top_productos_por_tienda.head(5)
            print("Top 5 tiendas con productos de computación más disponibles:")
            print(top_5_tiendas)
            return top_5_tiendas

        except KeyError as e:
            print(f"Error: La columna {e} no se encuentra en el DataFrame. Verifica los nombres de las columnas.")
            return pd.DataFrame()

        except Exception as e:
            print(f"Error inesperado: {e}")
            return pd.DataFrame()