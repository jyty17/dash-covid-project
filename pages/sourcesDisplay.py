import dash_core_components as dcc
import dash_html_components as html

from .headerComponent import Header

def create_layout(app):
	sourcesDisplay = html.Div([
		Header(),
		html.Div([
			html.H1("Sources", className="content-title"),
			html.P("I use data from these two sources for accurate data and daily updates. "),
			html.Div([
				html.H2("New York Times"),
				html.A('NYTimes   ', href='https://github.com/nytimes/covid-19-data', target="_blank", className="", style={"fontSize": "3rem"}),
				], className='py-4'),
			html.Div([
				html.H2("Our World in Data (OWID)"),
				html.A('OWID   ', href='https://github.com/owid/covid-19-data/tree/master/public/data/', target="_blank", className="py-4", style={"fontSize": "3rem"}),
				], className="py-4")
			])
		])

	return sourcesDisplay