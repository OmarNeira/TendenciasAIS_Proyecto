import pandas as pd

#Clase que define un filtro de los JSON para la pregunta 2
#¿Qué porcentaje de productos ofrece envío gratis por categoría (tecnología)?

class pregunta_2():
    def getQuery(self):
        """
        Debe ser un filtro a lo recogido de la DB con Panda para que lo grafique Bokeh
        """
        return """
            SELECT 
                p.id AS producto_id,
                p.name AS producto_name,
                p.envio AS tipo_envio,
                p.categoria AS categoria,
                p.subcategoria AS subcategoria
            FROM 
                producto2 p
            WHERE p.categoria = 'Tecnologia' -- ID de la categoría de tecnologia
        """
    
    def filtrarJSONPregunta(self, rows, colnames):
        """
        Filtra el DataFrame para encontrar el porcentaje de productos que ofrecen envío gratis
        por subcategoría en la categoría de tecnología y devuelve el top 5 subcategorías con el mayor porcentaje.
        También cuenta el total de envíos gratis con respecto a los que no tienen envío gratis.

        Args:
            df (pd.DataFrame): DataFrame con las columnas de la consulta SQL.

        Returns:
            dict: Diccionario con dos DataFrames, uno para el top 5 subcategorías y otro para el total de envíos gratis y no gratis.
        """
        try:
            print("Filtrando JSON para pregunta 2")
            df = pd.DataFrame(rows, columns=colnames)
            print(df.head(2))

            # Contar el total de productos por subcategoría
            total_por_subcategoria = df.groupby('subcategoria').size().reset_index(name='total_productos')

            # Contar el total de productos con envío gratis por subcategoría
            envio_gratis_por_subcategoria = df[df['tipo_envio'] == 'gratis'].groupby('subcategoria').size().reset_index(name='envio_gratis')

            # Unir los DataFrames para calcular el porcentaje de envío gratis por subcategoría
            df_porcentaje_envio_gratis = pd.merge(total_por_subcategoria, envio_gratis_por_subcategoria, on='subcategoria', how='left')
            df_porcentaje_envio_gratis['envio_gratis'] = df_porcentaje_envio_gratis['envio_gratis'].fillna(0)
            df_porcentaje_envio_gratis['porcentaje_envio_gratis'] = (df_porcentaje_envio_gratis['envio_gratis'] / df_porcentaje_envio_gratis['total_productos']) * 100

            # Seleccionar el top 5 subcategorías con el mayor porcentaje de envío gratis
            top_5_subcategorias = df_porcentaje_envio_gratis.sort_values(by='porcentaje_envio_gratis', ascending=False).head(5)
            print("Top 5 subcategorías con el mayor porcentaje de envío gratis:")
            print(top_5_subcategorias)

            # Contar el total de envíos gratis y no gratis
            total_envios = df['tipo_envio'].value_counts().reset_index()
            total_envios.columns = ['tipo_envio', 'cantidad']
            print("Total de envíos gratis y no gratis:")
            print(total_envios)

            return {
                'top_5_subcategorias': top_5_subcategorias,
                'total_envios': total_envios
            }

        except KeyError as e:
            print(f"Error: La columna {e} no se encuentra en el DataFrame. Verifica los nombres de las columnas.")
            return {}

        except Exception as e:
            print(f"Error inesperado: {e}")
            return {}