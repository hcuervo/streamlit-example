import pandas as pd  # pip install pandas openpyxl
import numpy as np
import statsmodels.api as sm
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

import yfinance as yf

periods = [90,30,10,3]
tickets = ['AAPL','YPF','GGAL.BA','SBUX']

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- GET DATA ----
#@st.cache
def get_data():
    hist = yf.download(tickets,period='1y')
    return(hist.Close)

def tendencia(df2,periods=periods):
    df2 = df2.tail(max(periods)).fillna(method='bfill')

    for period in periods:
        # Calcular tendencias
        Y = df2.tail(period).iloc[:,0]
        X = pd.to_numeric(df2.tail(period).index)
        X = sm.add_constant(range(len(df2.tail(period).index)),prepend=True)
        model = sm.OLS(Y,X)
        results = model.fit()
        trend = results.fittedvalues
        #lista.append(trend)
        df2 = pd.concat([df2,pd.DataFrame(trend,columns=[period])],axis=1)

    return(df2)    


df = get_data()


# ---- MAINPAGE ----
st.title(":bar_chart: Ticker Trends")
st.markdown("##")

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
ticker = st.sidebar.multiselect(
    "Select the Ticker:",
    options=df.columns.unique(),
    #default=df.columns.unique()
)


st.title(ticker)

for each in ticker:
    lista = tendencia(pd.DataFrame(df[each]))

    base = alt.Chart(lista).mark_point(color="white").encode(
                    x='index:T',
                    y=each
                    )
    alt.layer(base.mark_line(color='blue').encode(y=90),
              base.mark_line(color='red').encode(y=30)
              )
    
    st.altair(base)
    






# # TOP KPI's
# total_sales = 1000
# average_rating = 2000
# star_rating = ":star:" * 3
# average_sale_by_transaction = 800

# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader("Total Sales:")
#     st.subheader(f"US $ {total_sales:,}")
# with middle_column:
#     st.subheader("Average Rating:")
#     st.subheader(f"{average_rating} {star_rating}")
# with right_column:
#     st.subheader("Average Sales Per Transaction:")
#     st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")



left_column, right_column = st.columns(2)
#left_column.plotly_chart(fig_hourly_sales, use_container_width=True)



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

