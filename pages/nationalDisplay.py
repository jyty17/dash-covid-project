import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .headerComponent import Header

nationalDisplay = html.Div([
	Header(),
	html.H1("USA data on Covid-19")
	], className="page")