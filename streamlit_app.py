ticker= ['YPFD','AGRO','AUSO','BHIP','BOLT','BPAT','BRIO','CADO','CAPX','CARC','CECO2',
         'CELU','CGPA2','CTIO','DGCU2','DYCA','FERR','FIPL','GAMI','GARO','GBAN',
         'GCLA','GRIM','HARG','HAVA','INTR','INVJ','IRCP','IRSA','LEDE','LOMA','LONG',
         'METR','MOLA','MOLI','MORI','OEST','PATA','PGR','POLL','RICH','RIGO','ROSE',
         'SAMI','SEMI','TGLT']

import streamlit as st
import pandas as pd

import pandas_datareader as data
import pandas as pd

data_source = 'yahoo'
start_date = '2016-01-01'
end_date = '2021-11-30'
Google = data.DataReader('GOOG', data_source, start_date, end_date)
Amazon = data.DataReader('AMZN', data_source, start_date, end_date)
Microsoft = data.DataReader('MSFT', data_source, start_date, end_date)
Apple = data.DataReader('AAPL', data_source, start_date, end_date)
Facebook = data.DataReader('FB', data_source, start_date, end_date)

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
%matplotlib inline

px.line(df.xs(key='Close', axis=1, level='Stock Info')[['GOOG', 'AMZN']])
