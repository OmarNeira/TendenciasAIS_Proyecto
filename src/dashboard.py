from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import TabPanel, Tabs, ColumnDataSource, FactorRange, HoverTool, Div
from bokeh.layouts import column

import db as dbs

alto = 700
ancho = 1500

def graficarBarras(df_filteredX, df_filteredY, titulo, tooltips):
    source = ColumnDataSource(data=dict(x=df_filteredX, y=df_filteredY, tooltips=tooltips))
    p = figure(x_range=df_filteredX, height=alto, width=ancho, title=titulo, tools="")

    p.vbar(x='x', top='y', width=0.9, source=source)

    hover = HoverTool()
    hover.tooltips = [("Info", "@tooltips")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p

def graficarBarrasAgrupadas(brands, low_prices, high_prices, tooltips_low, tooltips_high, titulo):
    data = {'brands': brands, 'low_prices': low_prices, 'high_prices': high_prices, 'tooltips_low': tooltips_low, 'tooltips_high': tooltips_high}
    x = [(brand, 'Precio más bajo') for brand in brands] + [(brand, 'Precio más alto') for brand in brands]
    counts = low_prices + high_prices
    tooltips = tooltips_low + tooltips_high

    source = ColumnDataSource(data=dict(x=x, counts=counts, tooltips=tooltips))

    p = figure(x_range=FactorRange(*x), height=alto, width=ancho, title=titulo, tools="")

    p.vbar(x='x', top='counts', width=0.9, source=source)

    hover = HoverTool()
    hover.tooltips = [("Info", "@tooltips")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p

def pregunta_1(dbController):
    df_filtered_1 = dbController.dbPreguntar("pregunta_1")
    #print("Llego a MAIN ESTO:")
    #print(df_filtered_1)
    # Preparar datos para Bokeh
    df_filtered_1['x'] = df_filtered_1['tienda_name']
    df_filtered_1 = df_filtered_1.dropna(subset=['x', 'precio'])  # Ensure no null values in x and precio

    tooltips_1 = (df_filtered_1['producto_name']+" / "+df_filtered_1['precio'].astype(str)).tolist()
    p1 = graficarBarras(df_filtered_1['x'].tolist(), df_filtered_1['precio'].tolist(), "Pregunta 1", tooltips_1)
    return p1

def pregunta_3(dbController):
    df_filtered_3 = dbController.dbPreguntar("pregunta_3")
    #print("EJE X")
    #print(df_filtered_3['marca'].tolist())
    #print("EJE Y")
    #print(df_filtered_3['rango_precio'].tolist())

    brands = df_filtered_3['marca'].tolist()
    low_prices = df_filtered_3['rango_bajo'].tolist()
    high_prices = df_filtered_3['rango_alto'].tolist()
    tooltips_low = ("Precio más bajo: " + df_filtered_3['rango_bajo'].astype(str)).tolist()
    tooltips_high = ("Precio más alto: " + df_filtered_3['rango_alto'].astype(str)).tolist()

    p3 = graficarBarrasAgrupadas(brands, low_prices, high_prices, tooltips_low, tooltips_high, "Pregunta 3")
    return p3

def pregunta_4(dbController):
    df_filtered_4 = dbController.dbPreguntar("pregunta_4")
    #print("EJE X")
    #print(df_filtered_4['producto_name'].tolist())
    #print("EJE Y")
    #print(df_filtered_4['precio'].tolist())

    tooltips_4 = (df_filtered_4['producto_name'] + " / Stock: " + df_filtered_4['cantidad_disponible'].astype(str) +" / "+ df_filtered_4['precio'].astype(str)).tolist()
    p4 = graficarBarras(df_filtered_4['producto_name'].tolist(), df_filtered_4['precio'].tolist(), "Pregunta 4", tooltips_4)
    return p4


def main():
    #Objeto tipo db
    dbController = dbs.db()
    
    p1 = pregunta_1(dbController)

    p3 = pregunta_3(dbController)

    p4 = pregunta_4(dbController)
    
    # Crear descripciones
    descripcion1 = Div(text="<h3>Pregunta 1</h3><p>¿Cuáles son las tiendas con mayores ventas y mejores categorías de vendedor, cuáles son sus productos con más unidades disponibles en la categoría de computación?</p>")
    descripcion3 = Div(text="<h3>Pregunta 3</h3><p>¿Cuáles son los rangos de precios más frecuentes para laptops, agrupados por marca (5 marcas más caras)?</p>")
    descripcion4 = Div(text="<h3>Pregunta 4</h3><p>¿Qué productos en la categoría deportes tienen el mayor precio y stock disponible?</p>")

    # Crear pestañas
    tab1 = TabPanel(child=column(descripcion1, p1), title="Gráfico 1")
    tab3 = TabPanel(child=column(descripcion3, p3), title="Gráfico 3")
    tab4 = TabPanel(child=column(descripcion4, p4), title="Gráfico 4")

    # Crear el objeto Tabs
    tabs = Tabs(tabs=[tab1, tab3, tab4])

    # Mostrar el resultado
    show(tabs)

main()