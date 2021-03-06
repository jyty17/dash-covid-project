# import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

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
# df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
countries = df.location.unique()
countries.sort()
countries_option = [{'label': x, 'value': x} for x in countries]

country_first = df[df.location == countries[0]]
# fig = go.Figure()
# fig.add_trace(
# 	go.Scatter(
# 		y=country_first.total_cases,
# 		x=country_first.date,
# 		mode='lines',
# 		name='Infected',
# 		line={'color': 'firebrick'}
# 	))
# fig.add_trace(
# 	go.Scatter(
# 		y=country_first.total_deaths,
# 		x=country_first.date,
# 		mode='lines',
# 		name='Deaths',
# 		line={'color': 'darkslateblue'}
# 	))
# fig.update_layout(
# 	title=countries[0],
# 	plot_bgcolor=colors['background'],
# 	)

def create_layout(app):
	recent_data_point = df[df.location == countries[0]].tail(1)
	# print(type(recent_data_point.total_cases))
	internationalDisplay = html.Div([
		html.H1("Worldwide data on Covid-19 (OWID)", 
			className="content-title"),
		dcc.Dropdown(
			id='country_dropdown',
			options=countries_option,
			value=countries[0]
			),
		html.Div([
			dcc.Graph(
				id='country_graph',
				figure={
					'data': [
					go.Scatter(
						y=country_first.total_cases,
						x=country_first.date,
						mode='lines',
						name='Infected',
						line={'color': 'firebrick'}
						),
					go.Scatter(
						y=country_first.total_deaths,
						x=country_first.date,
						mode='lines',
						name='Deaths',
						line={'color': 'darkslateblue'}
						)
					],
					'layout': go.Layout(
						title=countries[0],
						plot_bgcolor=colors['background']
						)
					},
				className="w-50"
				),
			dcc.Graph(
				id='country_velocity',
				figure={
					'data': [
						go.Scatter(
							y=country_first.new_cases,
							x=country_first.date,
							mode='lines',
							name='new cases',
							),
						go.Scatter(
							y=country_first.new_deaths,
							x=country_first.date,
							mode='lines',
							name='new deaths'
							)
						],
					'layout': go.Layout(title='Trends')
					},
					className="w-50"
				)
			], className="d-flex flex-row justify-content-between", style={"height": "40vh"}),
		html.Div([
			html.H1(children="Last Updated: "+recent_data_point.date, className=""),
			html.Div([
				html.H2('Total cases: '),
				html.H2(children=recent_data_point.total_cases, id='country-cases'), #
				], className='row tab'),
			html.Div([
				html.H2('Total Deaths: '),
				html.H2(children=recent_data_point.total_deaths, id='country-deaths') #
				], className='row tab')
			], className="d-flex flex-row justify-content-between w-75"),
		html.Div([
			dcc.Graph(
				id='country_percentages',
				figure={
					'data': [
						go.Pie(
							labels=['Cases', 'Deaths'],
							values=[int(recent_data_point.total_cases), int(recent_data_point.total_deaths)],
							hole=0.5)
						],
					'layout': {"title": {"text": recent_data_point.date }}
					},
				className="w-50"
				),
			dcc.Graph(
				id='country_current',
				figure={
					'data': [
						go.Bar(
							x=["Cases", "Deaths"],
							y=[int(recent_data_point.new_cases), int(recent_data_point.new_deaths)],
							marker_color=['firebrick', 'darkslateblue'],
							width=[0.5]*2
							)
						],
					'layout': {"title": {"text": recent_data_point.date }}
					},
				className="w-50"
				)
			], className='d-flex flex-row justify-content-between')
		
		], className="page")

	@app.callback(
		[
		Output('country-cases', 'children'),
		Output('country-deaths', 'children'),
		Output('country_graph', 'figure'),
		Output('country_velocity', 'figure'),
		Output('country_percentages', 'figure'),
		Output('country_current', 'figure')
		],
		[Input('country_dropdown', 'value')]
		)
	def update_country_data(dropdown_value):
		# print(df[df.location == dropdown_value])

		country_data = df[df.location == dropdown_value]
		date_axis = country_data.date

		country_data_last = country_data.tail(1)

		cases = go.Scatter(
			y=country_data.total_cases,
			x=date_axis,
			mode='lines',
			name='cases',
			line={'color': 'firebrick'}
			)
		deaths = go.Scatter(
			y=country_data.total_deaths,
			x=date_axis,
			mode='lines',
			name='Deaths',
			line={'color': 'darkslateblue'}
			)
		
		new_cases = go.Scatter(
			y=country_data.new_cases,
			x=date_axis,
			mode='lines',
			name='New Cases',
			)
		new_deaths = go.Scatter(
			y=country_data.new_deaths,
			x=date_axis,
			mode='lines',
			name='New Deaths')

		new_percentage = go.Pie(
			labels=['Cases', 'Deaths'],
			values=[int(country_data_last.total_cases), int(country_data_last.total_deaths)],
			hole=0.5)

		new_current = go.Bar(
			x=["Cases", "Deaths"],
			y=[int(country_data_last.new_cases), int(country_data_last.new_deaths)],
			marker_color=['firebrick', 'darkslateblue'],
			width=[0.5]*2
			)

		newFigs = [
			country_data_last['total_cases'], 
			country_data_last['total_deaths'],
			{
				'data': [cases, deaths],
				'layout': go.Layout(
					title=dropdown_value,
					plot_bgcolor=colors['background'],
					)
			},
			{
				'data': [new_cases, new_deaths],
				'layout': go.Layout(title='Trends')
			},
			{
				'data': [new_percentage],
				'layout': {"title": {"text": country_data_last.date }}
			},
			{
				'data': [new_current],
				'layout': {"title": {"text": country_data_last.date }}
			}
		]
		return newFigs

	# @app.callback(
	# 	[
	# 	Output('country-cases', 'children'),
	# 	Output('country-deaths', 'children')
	# 	],
	# 	[Input('country_dropdown', 'value')]
	# 	)
	# def update_counts(dropdown_value):
	# 	last = df[df.location == dropdown_value].tail(1) #
	# 	return last['total_cases'], last['total_deaths']


	return internationalDisplay
