from bokeh.plotting import figure, show
from bokeh.models import TabPanel, Tabs, ColumnDataSource, FactorRange, HoverTool, Div
from bokeh.layouts import column
from bokeh.palettes import Category20c, Spectral6, viridis
from bokeh.transform import cumsum, factor_cmap

import pandas as pd
from cmath import pi

import db as dbs

alto = 700
ancho = 1500

def graficarTorta(data_dict, titulo):
    data = pd.Series(data_dict).reset_index(name='value').rename(columns={'index': 'bar'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = viridis(len(data_dict))

    p = figure(height=alto, title=titulo, toolbar_location=None,
               tools="hover", tooltips="@bar: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='bar', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    return p

def graficarBarras(df_filteredX, df_filteredY, titulo, tooltips):
    source = ColumnDataSource(data=dict(x=df_filteredX, y=df_filteredY, tooltips=tooltips))
    p = figure(x_range=df_filteredX, height=alto, width=ancho, title=titulo, tools="")

    p.vbar(x='x', top='y', width=0.9, source=source, fill_color=factor_cmap('x', palette=Spectral6, factors=df_filteredX))

    hover = HoverTool()
    hover.tooltips = [("Info", "@tooltips")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = pi / 4
    p.yaxis.formatter.use_scientific = False

    return p

def graficarBarrasAgrupadas(brands, low_prices, high_prices, tooltips_low, tooltips_high, titulo):
    data = {'brands': brands, 'low_prices': low_prices, 'high_prices': high_prices, 'tooltips_low': tooltips_low, 'tooltips_high': tooltips_high}
    x = [(brand, 'Precio más bajo') for brand in brands] + [(brand, 'Precio más alto') for brand in brands]
    counts = low_prices + high_prices
    tooltips = tooltips_low + tooltips_high

    source = ColumnDataSource(data=dict(x=x, counts=counts, tooltips=tooltips))

    p = figure(x_range=FactorRange(*x), height=alto, width=ancho, title=titulo, tools="")

    p.vbar(x='x', top='counts', width=0.9, source=source, fill_color=factor_cmap('x', palette=Spectral6, factors=x))

    hover = HoverTool()
    hover.tooltips = [("Info", "@tooltips")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = pi / 4
    p.yaxis.formatter.use_scientific = False

    return p

def pregunta_1(dbController):
    df_filtered_1 = dbController.dbPreguntar("pregunta_1")
    # Preparar datos para Bokeh
    df_filtered_1['x'] = df_filtered_1['tienda_name']
    df_filtered_1 = df_filtered_1.dropna(subset=['x', 'precio'])  # Ensure no null values in x and precio

    tooltips_1 = (df_filtered_1['producto_name']+" / "+df_filtered_1['precio'].astype(str)).tolist()
    p1 = graficarBarras(df_filtered_1['x'].tolist(), df_filtered_1['precio'].tolist(), "Pregunta 1", tooltips_1)
    return p1

def pregunta_2(dbController):
    df_filtered_2 = dbController.dbPreguntar("pregunta_2")
    # Convertir total_envios a diccionario
    total_envios_dict = df_filtered_2['total_envios'].set_index('tipo_envio')['cantidad'].to_dict()
    p1 = graficarTorta(total_envios_dict, "Pregunta 2")

    top_5_subcategorias = df_filtered_2['top_5_subcategorias']
    p2 = graficarBarras(top_5_subcategorias['subcategoria'].tolist(), top_5_subcategorias['porcentaje_envio_gratis'].tolist(), "Pregunta 2", (top_5_subcategorias['subcategoria'].astype(str)+" / "+top_5_subcategorias['porcentaje_envio_gratis'].astype(str)+"%").tolist())
    # Crear pestañas
    tab1 = TabPanel(child=column(p1), title="Gráfico 1")
    tab2 = TabPanel(child=column(p2), title="Gráfico 2")

    # Crear el objeto Tabs
    tabs = Tabs(tabs=[tab1, tab2])
    return tabs

def pregunta_3(dbController):
    df_filtered_3 = dbController.dbPreguntar("pregunta_3")
    brands = df_filtered_3['marca'].tolist()
    low_prices = df_filtered_3['rango_bajo'].tolist()
    high_prices = df_filtered_3['rango_alto'].tolist()
    tooltips_low = ("Precio más bajo: " + df_filtered_3['rango_bajo'].astype(str)).tolist()
    tooltips_high = ("Precio más alto: " + df_filtered_3['rango_alto'].astype(str)).tolist()

    p3 = graficarBarrasAgrupadas(brands, low_prices, high_prices, tooltips_low, tooltips_high, "Pregunta 3")
    return p3

def pregunta_4(dbController):
    df_filtered_4 = dbController.dbPreguntar("pregunta_4")
    tooltips_4 = (df_filtered_4['producto_name'] + " / Stock: " + df_filtered_4['cantidad_disponible'].astype(str) +" / "+ df_filtered_4['precio'].astype(str)).tolist()
    p4 = graficarBarras(df_filtered_4['producto_name'].tolist(), df_filtered_4['precio'].tolist(), "Pregunta 4", tooltips_4)
    return p4

def pregunta_5(dbController):
    df_filtered_5 = dbController.dbPreguntar("pregunta_5")
    tooltips_5 = (df_filtered_5['producto_name'] + " / Calificación: " + df_filtered_5['calificacion'].astype(str)).tolist()
    p5 = graficarBarras(df_filtered_5['producto_name'].tolist(), df_filtered_5['cant_calificaciones'].tolist(), "Pregunta 5", tooltips_5)
    return p5

def main():
    #Objeto tipo db
    dbController = dbs.db()
    
    p1 = pregunta_1(dbController)
    p2 = pregunta_2(dbController)
    p3 = pregunta_3(dbController)
    p4 = pregunta_4(dbController)
    p5 = pregunta_5(dbController)
    
    # Crear descripciones
    descripcion1 = Div(text="<h3>Pregunta 1</h3><p>¿Cuáles son las tiendas con mayores ventas y mejores categorías de vendedor, cuáles son sus productos con más unidades disponibles en la categoría de computación?</p>")
    descripcion2 = Div(text="<h3>Pregunta 2</h3><p>¿Qué porcentaje de productos (top 5) ofrece envío gratis por categoría (tecnología)?</p>")
    descripcion3 = Div(text="<h3>Pregunta 3</h3><p>¿Cuáles son los rangos de precios más frecuentes para laptops, agrupados por marca (5 marcas más caras)?</p>")
    descripcion4 = Div(text="<h3>Pregunta 4</h3><p>¿Qué productos en la categoría deportes tienen el mayor precio y stock disponible?</p>")
    descripcion5 = Div(text="<h3>Pregunta 5</h3><p>¿Cuáles son los 3 productos reacondicionados con más calificaciones en la categoría de electrodomésticos?</p>")

    # Crear pestañas
    tab1 = TabPanel(child=column(descripcion1, p1), title="Gráfico 1")
    tab2 = TabPanel(child=column(descripcion2, p2), title="Gráfico 2")
    tab3 = TabPanel(child=column(descripcion3, p3), title="Gráfico 3")
    tab4 = TabPanel(child=column(descripcion4, p4), title="Gráfico 4")
    tab5 = TabPanel(child=column(descripcion5, p5), title="Gráfico 5")

    # Crear el objeto Tabs
    tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5])

    # Mostrar el resultado
    show(tabs)

main()