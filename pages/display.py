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
# print(last, '\n', last['date'])

def create_layout(app):
	default_display = html.Div([
		html.Div([
			html.H1("Overview", className="content-title"),
		    dcc.Graph(
		    	id="general_graph",
		    	figure={
		    		'data': [
			    		go.Scatter(
							y=gc['total_cases'],
							x=gc['date'],
							mode='lines',
							name='Infected',
							line={'color': 'firebrick'}
						),
						go.Scatter(
							y=gc['total_deaths'],
							x=gc['date'],
							mode='lines',
							name='Deaths',
							line={'color': 'darkslateblue'}
						)
		    		],
		    		'layout': go.Layout(title="Global No. of Infected and Deaths Due to CoVid-19")
		    	}
	    	),
			html.Div([
				html.H1(children="Last Updated: "+last.date, className=""),
				html.Div([
					html.H1('Total Infected: \t'),
					html.H1(last.total_cases),
					], className='row tab'),
				html.Div([
					html.H1('Total Deaths: \t'),
					html.H1(last.total_deaths)
					], className='row tab')
				], className="d-flex flex-row justify-content-between w-75"),
			html.Div([
			dcc.Graph(
				id='global_percentages',
				figure={
					'data': [
						go.Pie(
							labels=['Cases', 'Deaths'],
							values=[int(last.total_cases), int(last.total_deaths)],
							hole=0.5)
						],
					'layout': {"title": {"text": last.date }}
					},
					className="w-50"
				),
			dcc.Graph(
				id='global_current',
				figure={
					'data': [
						go.Bar(
							x=["Cases", "Deaths"],
							y=[int(last.new_cases), int(last.new_deaths)],
							marker_color=['firebrick', 'darkslateblue'],
							width=[0.5]*2
							)
						],
					'layout': {"title": {"text": last.date }}
					},
					className="w-50"
				)
			], className='d-flex flex-row justify-content-between')
			])
		], className="page")

	return default_display


