import pandas as pd

#Clase que define un filtro de los JSON para la pregunta 3
#¿Cuáles son los rangos de precios más frecuentes para laptops, 
# agrupados por marca (5 marcas más caras)?

#Categoria laptop MCO1652

class pregunta_3():
    def getQuery(self):
        """
        Debe ser un filtro a lo recogido de la DB con Panda para que lo grafique Bokeh
        """
        return """
            SELECT 
                p.id AS producto_id,
                p.category_id AS categoria_id,
                p.name AS producto_name,
                p.price AS precio,
                p.combined_attributes AS caracteristicas,
                t.id AS tienda_id,
                t.name AS tienda_name,
                t.power_seller_status AS categoria,
                t.total_transacciones AS cant_ventas
            FROM 
                producto p
            INNER JOIN tienda t ON p.seller_id = t.id
            WHERE p.category_id = 'MCO1652' -- ID de la categoría de laptops
        """
    
    def filtrarJSONPregunta(self, rows, colnames):
        """
        Filtra el DataFrame para encontrar los rangos de precios más frecuentes para laptops,
        agrupados por marca (5 marcas más caras) y características principales (marca – color – modelo).

        Args:
            df (pd.DataFrame): DataFrame con las columnas de la consulta SQL.

        Returns:
            pd.DataFrame: DataFrame filtrado con los rangos de precios más frecuentes.
        """
        try:
            print("Filtrando JSON para pregunta 3")
            df = pd.DataFrame(rows, columns=colnames)
            print(df.head(2))

            # Asegurarse de que 'precio' sea de tipo float
            df['precio'] = df['precio'].astype(float)

            # Agrupar por marca y calcular el precio promedio
            df['marca'] = df['caracteristicas'].apply(lambda x: x.split(',')[0])
            df_marca_precio = df.groupby('marca')['precio'].mean().reset_index()

            # Ordenar por precio promedio y seleccionar las 5 marcas más caras
            top_5_marcas = df_marca_precio.sort_values(by='precio', ascending=False).head(5)['marca'].tolist()

            # Filtrar el DataFrame original para incluir solo las 5 marcas más caras
            df_top_marcas = df[df['marca'].isin(top_5_marcas)]

            # Agrupar por marca y características principales, y contar la frecuencia de los rangos de precios
            df_top_marcas['rango_precio'] = pd.cut(df_top_marcas['precio'], bins=5) # Dividir en 5 rangos de precios
            df_rangos_frecuencia = df_top_marcas.groupby(['marca', 'caracteristicas', 'rango_precio']).size().reset_index(name='frecuencia') # Contar la frecuencia de cada rango de precios

            # Seleccionar un rango de precios por cada marca
            df_rangos_frecuencia = df_rangos_frecuencia.sort_values(by='frecuencia', ascending=False).drop_duplicates(subset=['marca'])

            # Crear columnas para los rangos de precios bajos y altos
            df_rangos_frecuencia['rango_bajo'] = df_rangos_frecuencia['rango_precio'].apply(lambda x: x.left)
            df_rangos_frecuencia['rango_alto'] = df_rangos_frecuencia['rango_precio'].apply(lambda x: x.right)

            print("Rangos de precios más frecuentes para laptops agrupados por marca y características principales:")
            print(df_rangos_frecuencia)
            return df_rangos_frecuencia

        except KeyError as e:
            print(f"Error: La columna {e} no se encuentra en el DataFrame. Verifica los nombres de las columnas.")
            return pd.DataFrame()

        except Exception as e:
            print(f"Error inesperado: {e}")
            return pd.DataFrame()