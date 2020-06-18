import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

import pathlib
import os
import pandas as pd

from .headerComponent import Header

from .data_check import df_global_cases as gc

# import datetime as dt

# get relative data folder
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../data").resolve()

colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'theme': '#C41330',
    'infected': '',
    'deaths': ''
}

# create traces
fig = go.Figure()
fig.add_trace(
	go.Scatter(
		y=gc['total_cases'],
		x=gc['date'],
		mode='lines',
		name='Infected',
		line={'color': 'firebrick'}
	))
fig.add_trace(
	go.Scatter(
		y=gc['total_deaths'],
		x=gc['date'],
		mode='lines',
		name='Deaths',
		line={'color': 'darkslateblue'}
	))
fig.update_layout(
	title='Global No. of Infected and Deaths Due to CoVid-19',
	plot_bgcolor=colors['background'],
	)

# fig2 = go.Figure()
# fig2.add_trace(
# 	go.Bar(),
# 	row=1,
# 	col=1)
# fig.add_trace(
# 	go.Bar(),
# 	row=1,
# 	col=2)

last = gc.tail(1)
print(last, '\n', last['date'])

def create_layout(app):
	default_display = html.Div([
		html.Div([
			Header(),
		    dcc.Graph(
		    	id="general_graph",
		    	figure=fig
	    	),
			html.Div([
				html.H4(children="Last Updated: "+last.date, className=""),
				html.Div([
					html.H4('Total Infected: ',
						className="padded twelve"),
					html.H5(last.total_cases),
					], className='row tab'),
				html.Div([
					html.H4('Total Deaths: ',
						className="padded"),
					html.H5(last.total_deaths)
					], className='row tab')
				])
			])
		], className="page")

	return default_display


