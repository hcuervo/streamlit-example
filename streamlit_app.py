stock_tickers = ['AAPL', 'GOOGL','PG','TCS.BO','MSFT','TWTR','NFLX','INFY.BO','WIPRO.BO','SBIN.NS',
                'HDFC.NS','ICICIBANK.NS','RELIANCE.NS','TECHM.NS','HINDUNILVR.NS','BHARTIARTL.NS',
                'HCLTECH.NS','ASIANPAINT.NS','LT.NS','AXISBANK.NS','MARUTI.NS','TATAMOTORS.NS','TATASTEEL.NS',
                'NESTLEIND.NS','AMZN','ACN','ADBE','ORCL','FB','CIPLA6.BO','KPITTECH.NS','BSOFT.NS','LTI.NS','MINDTREE.BO','MPHASIS.NS','NAZARA.NS','NAUKRI.NS',
                'TATAELXSI.NS','HAPPSTMNDS.NS','LUPIN.NS','GLAND.NS','ADANITRANS.NS','ADANIGREEN.NS']

from ast import Pass
from email.mime import image
from urllib.parse import scheme_chars
from nbformat import write
import streamlit as st
from optparse import Option
from tracemalloc import start
import yfinance as yf 
import pandas as pd
from tickers import stock_tickers
import datetime
from streamlit_option_menu import option_menu 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cufflinks as cf



image1 = Image.open('icon.png')
st.set_page_config(page_title="Stock Market Analysis", page_icon= image1)
image = Image.open('main.png')
st.image(image)

hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden; footer {visibility: hidden;}}
                </style>
                """
st.markdown(hide_menu_style, unsafe_allow_html=True)
