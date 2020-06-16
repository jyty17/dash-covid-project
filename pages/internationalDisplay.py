import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from .headerComponent import Header

import pandas as pd

# internationalDisplay = html.Div([
# 	Header(),
# 	html.H1("Worldwide data on Covid-19")
# 	], className="page")

# international data should also display more stats than just infected cases and deaths 

colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'theme': '#C41330',
    'infected': '',
    'deaths': ''
}


df = pd.read_csv('data/owid-covid-data.csv')
countries = df.location.unique()
countries_option = [{'label': x, 'value': x} for x in countries]

country_first = df[df.location == countries[0]]
fig = go.Figure()
fig.add_trace(
	go.Scatter(
		y=country_first.total_cases, #
		x=country_first.date,
		mode='lines',
		name='Infected',
		line={'color': 'firebrick'}
	))
fig.add_trace(
	go.Scatter(
		y=country_first.total_deaths, #
		x=country_first.date,
		mode='lines',
		name='Deaths',
		line={'color': 'darkslateblue'}
	))
fig.update_layout(
	title='Global No. of Infected and Deaths Due to CoVid-19',
	plot_bgcolor=colors['background'],
	)

def create_layout(app):
	internationalDisplay = html.Div([
		Header(),
		html.H1("Worldwide data on Covid-19 (NYTimes)"),
		dcc.Dropdown(
			id='country_dropdown',
			options=countries_option,
			value=countries[0]
			),
		dcc.Graph(
			id='world_graph',
			figure=fig
			),
		html.Div([
			html.Div([
				html.H4('Total Infected as of {}'.format('** last updated time **'),
					className="padded twelve"),
				html.H5(id='country-infected'), #
				], className='row tab'),
			html.Div([
				html.H4('Total Deaths as of {}'.format('** last updated time **'),
					className="padded twelve"),
				html.H5(id='country-deaths') #
				], className='row tab')
			])
		], className="page")

	@app.callback(
		Output('world_graph', 'figure'),
		[Input('country_dropdown', 'value')]
		)
	def update_country_data(dropdown_value):
		print(df[df.location == dropdown_value])

		country_data = df[df.location == dropdown_value]

		infected = go.Scatter(
			y=country_data['total_cases'],
			x=country_data.date,
			mode='lines',
			name='Infected',
			line={'color': 'firebrick'}
			)
		deaths = go.Scatter(
			y=country_data['total_deaths'],
			x=country_data.date,
			mode='lines',
			name='Deaths',
			line={'color': 'darkslateblue'}
			)
		# newFig = go.Figure()
		# newFig.add_trace(
		# 	go.Scatter(
		# 		y=df[df.location == dropdown_value]['cases'], #
		# 		x=df['date'],
		# 		mode='lines',
		# 		name='Infected',
		# 		line={'color': 'firebrick'}
		# 	))
		# newFig.add_trace(
		# 	go.Scatter(
		# 		y=df[df.location == dropdown_value]['deaths'], #
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
		Output('country-infected', 'children'),
		Output('country-deaths', 'children')
		],
		[Input('country_dropdown', 'value')]
		)
	def update_counts(dropdown_value):
		last = df[df.location == dropdown_value].tail(1) #
		return last['total_cases'], last['total_deaths']


	return internationalDisplay
