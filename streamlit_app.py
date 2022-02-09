from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!!!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
# Importar librerias
import requests

from datetime import datetime

import pandas as pd
import json as json
import numpy as np

from bs4 import BeautifulSoup # fundamental para scrapping

# Scrapear de RAVA Online

def historico(ticket=''):
    # Link a la página que contiene la tabla
    # Atención: dolar-plus.com entrega algo más de un año de historico
    url  = 'https://www.rava.com/perfil/'+ticket

    # Cargar la página
    resp = requests.get(url)

    # Interpretar la respuesta
    soup = BeautifulSoup(resp.text, "html.parser")
    
    # Armar la respuesta según la página de RAVA Online
    res = soup.find('perfil-p')[':res']
    data = json.loads(res)
    
    
    df=pd.DataFrame()
    

    df = pd.json_normalize(data['coti_hist'])
    df.set_index('fecha',inplace=True)

    X = []
    Y = []
    
    if type(data['grafico_intradiario']) == list:
        for each in data['grafico_intradiario']:
            date = datetime.strptime(each['fecha']+' '+each['hora'], '%Y-%m-%d %H:%M:%S')
            X.append(date)
            Y.append(float(each['ultimo']))

    intra = pd.DataFrame()
    intra['time']=X
    intra['price']=Y
    intra.set_index('time',inplace=True)

    
    return(df,intra)

h,i=historico('tx26')
h.cierre.plot()
i.plot()
