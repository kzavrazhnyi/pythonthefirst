# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)

# Time Series Plot with datetime Objects

# # Using plotly.express
# import plotly.express as px
#
# import pandas as pd
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
#
# fig = px.line(df, x='Date', y='AAPL.High')
# fig.show()

# # Using graph_objects
# import plotly.graph_objects as go
#
# import pandas as pd
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
#
# fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
# fig.show()

# Time Series Plot with Custom Date Range

# import plotly.graph_objects as go
# import datetime
#
# x = [datetime.datetime(year=2013, month=10, day=4),
#      datetime.datetime(year=2013, month=11, day=5),
#      datetime.datetime(year=2013, month=12, day=6)]
#
# fig = go.Figure(data=[go.Scatter(x=x, y=[1, 3, 6])])
# # Use datetime objects to set xaxis range
# fig.update_layout(xaxis_range=[datetime.datetime(2013, 10, 17),
#                                datetime.datetime(2013, 11, 20)])
# fig.show()

# Time Series With Rangeslider

# import plotly.graph_objects as go
# import pandas as pd
#
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
#
# fig = go.Figure()
# fig.add_trace(go.Scatter(
#                 x=df.Date,
#                 y=df['AAPL.High'],
#                 name="AAPL High",
#                 line_color='deepskyblue',
#                 opacity=0.8))
#
# fig.add_trace(go.Scatter(
#                 x=df.Date,
#                 y=df['AAPL.Low'],
#                 name="AAPL Low",
#                 line_color='dimgray',
#                 opacity=0.8))
#
# # Use date string to set xaxis range
# fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
#                   title_text="Manually Set Date Range")
# fig.show()

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),
#
#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),
#
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     )
# ])
#
# app.run_server(debug=True)

# import pandas as pd
# import matplotlib.pyplot as plt
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', 80)
# pd.set_option('max_rows', 6000)
#
# # https://finance.yahoo.com/quote/AAPL
# df = pd.read_csv("AAPL.csv",sep=',', header=0, index_col='Date', parse_dates=True)
# df = df.sort_values(by='Date')
# df['returns']=(df['Close']/df['Close'].shift(1))-1
# df['returns_pers']=((df['Close']/df['Close'].shift(1))-1)*100
#
# # https://finance.yahoo.com/quote/MSFT/
# df2 = pd.read_csv("MSFT.csv",sep=',', header=0, index_col='Date', parse_dates=True)
# df2 = df2.sort_values(by='Date')
# df2['returns']=(df2['Close']/df2['Close'].shift(1))-1
# df2['returns_pers']=((df['Close']/df2['Close'].shift(1))-1)*100
#
# df['Close'].plot(label='AAPL')
# df['ma50'] = df['Open'].rolling(5).mean().plot(label='ma5')
# df2['Close'].plot(label='AAPL')
# df2['ma50'] = df2['Open'].rolling(5).mean().plot(label='ma5')
#
# print(df)
# print(df2)
#
# plt.legend()
# plt.show()

# # Використання для аналізу курсів валют біблітекі yfinance
# import yfinance
# from matplotlib import pyplot as plt
# import datetime
#
# EURUAH = yfinance.download("EURUAH=X", start="2020-02-20", end=datetime.datetime.today())
# USDUAH = yfinance.download("USDUAH=X", start="2020-02-20", end=datetime.datetime.today())
# print(EURUAH)
# print(USDUAH)
#
# df = EURUAH.sort_values(by='Date')
# df['Close'].plot(label='EUR/UAH')
# df2 = USDUAH.sort_values(by='Date')
# df2['Close'].plot(label='USD/UAH')
#
# plt.legend()
# plt.show()
