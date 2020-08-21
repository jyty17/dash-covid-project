# import dash
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

state_first = df[df.state == states[0]]
fig = go.Figure()
fig.add_trace(
	go.Scatter(
		y=state_first.cases,
		x=state_first.date,
		mode='lines',
		name='Infected',
		line={'color': 'firebrick'}
	))
fig.add_trace(
	go.Scatter(
		y=state_first.deaths,
		x=state_first.date,
		mode='lines',
		name='Deaths',
		line={'color': 'darkslateblue'}
	))
fig.update_layout(
	title='National No. of Infected and Deaths Due to CoVid-19',
	plot_bgcolor=colors['background'],
	)


def create_layout(app):
	recent_data_point = df[df.state == states[0]].tail(1)
	recent_update = df[df.date == recent_data_point.date.values[0]]
	print(recent_update)
	nationalDisplay = html.Div([
		Header(),
		html.H1("USA data on Covid-19 (NYTimes)",
			className="content-title"),
		dcc.Dropdown(
			id='state_dropdown',
			options=states_option,
			value=states_option[0]['value']
			),
		dcc.Graph(
			id='national_graph',
			figure={
				'data': [
					go.Scatter(
						y=state_first.cases,
						x=state_first.date,
						mode='lines',
						name='Infected',
						line={'color': 'firebrick'}
					),
					go.Scatter(
						y=state_first.deaths,
						x=state_first.date,
						mode='lines',
						name='Deaths',
						line={'color': 'darkslateblue'}
					)
				],
				'layout': go.Layout(title=states[0])

			}
			),
		# dcc.Graph(
		# 	id='national_map',
		# 	figure={
		# 		'data': [
		# 			go.Choropleth(
		# 			    locations=df['code'],
		# 			    z=df['total exports'].astype(float),
		# 			    locationmode='USA-states',
		# 			    colorscale='Reds',
		# 			    autocolorscale=False,
		# 			    text=df['text'], # hover text
		# 			    marker_line_color='white', # line markers between states
		# 			    colorbar_title="Millions USD"
		# 			)
		# 		]
		# 	}
		# 	)
		html.Div([
			html.H1(children="Last Updated: "+recent_data_point.date, className=""),
			html.Div([
				html.H2('Total Infected'),
				html.H2(children=recent_data_point.cases ,id='state-infected'),
				], className='row tab'),
			html.Div([
				html.H2('Total Deaths'),
				html.H2(children=recent_data_point.deaths ,id='state-deaths')
				], className='row tab')
			], className="d-flex flex-row justify-content-between w-75")
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


	# @app.callback(
	# 	[Output()],
	# 	[Input()]
	# 	)
	# def update_movers(date):
	# 	_date = df.date.unique()
	# 	_date.sort()
	# 	day = _date[-1]
		
	# 	top_movers = df[df.location == date].sort_values(by=['new_cases'], ascending=False).head(10)


	return nationalDisplay
