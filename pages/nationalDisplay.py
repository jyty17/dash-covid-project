import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from .headerComponent import Header

import pandas as pd

colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'theme': '#C41330',
    'infected': '',
    'deaths': ''
}

df = pd.read_csv('data/us-states.csv')
states = df.state.unique()
states.sort()
states_option = [{'label': x, 'value': x} for x in states]

first = df[df.state == 'Alabama']
fig = go.Figure()
fig.add_trace(
	go.Scatter(
		y=first.cases,
		x=first.date,
		mode='lines',
		name='Infected',
		line={'color': 'firebrick'}
	))
fig.add_trace(
	go.Scatter(
		y=first.deaths,
		x=first.date,
		mode='lines',
		name='Deaths',
		line={'color': 'darkslateblue'}
	))
fig.update_layout(
	title='Global No. of Infected and Deaths Due to CoVid-19',
	plot_bgcolor=colors['background'],
	)


def create_layout(app):
	nationalDisplay = html.Div([
		Header(),
		html.H1("USA data on Covid-19 (NYTimes)"),
		dcc.Dropdown(
			id='state_dropdown',
			options=states_option,
			value=states_option[0]['value']
			),
		dcc.Graph(
			id='national_graph',
			figure=fig
			),
		html.Div([
			html.Div([
				html.H4('Total Infected as of {}'.format('** last updated time **'),
					className="padded twelve"),
				html.H5(id='state-infected'),
				], className='row tab'),
			html.Div([
				html.H4('Total Deaths as of {}'.format('** last updated time **'),
					className="padded twelve"),
				html.H5(id='state-deaths')
				], className='row tab')
			])
		], className="page")

	@app.callback(
		Output('national_graph', 'figure'),
		[Input('state_dropdown', 'value')]
		)
	def update_state_data(dropdown_value):
		print(df[df.state == dropdown_value],)
		# newFig = go
		state_data = df[df.state == dropdown_value]
		infected = go.Scatter(
			y=state_data['cases'],
			x=state_data.date,
			mode='lines',
			name='Infected',
			line={'color': 'firebrick'}
			)
		deaths = go.Scatter(
			y=state_data['deaths'],
			x=state_data.date,
			mode='lines',
			name='Deaths',
			line={'color': 'darkslateblue'}
			)

		# newFig.add_trace(
		# 	go.Scatter(
		# 		y=df[df.state == dropdown_value]['cases'],
		# 		x=df['date'],
		# 		mode='lines',
		# 		name='Infected',
		# 		line={'color': 'firebrick'}
		# 	))
		# newFig.add_trace(
		# 	go.Scatter(
		# 		y=df[df.state == dropdown_value]['deaths'],
		# 		x=df['date'],
		# 		mode='lines',
		# 		name='Deaths',
		# 		line={'color': 'darkslateblue'}
		# 	))
		# newFig.update_layout(
		# 	title=dropdown_value,
		# 	plot_bgcolor=colors['background'],
		# 	)

		return {
			'data': [infected, deaths],
			'layout': go.Layout(
				title=dropdown_value,
				plot_bgcolor=colors['background'],
				)
			}

	@app.callback(
		[
		Output('state-infected', 'children'),
		Output('state-deaths', 'children')
		],
		[Input('state_dropdown', 'value')]
		)
	def update_counts(dropdown_value):
		last = df[df.state == dropdown_value].tail(1)
		return last['cases'], last['deaths']


	return nationalDisplay
