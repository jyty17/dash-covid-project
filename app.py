import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import (
	display,
	nationalDisplay,
	internationalDisplay
	)

# import pandas as pd

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
               	"https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
               	"https://fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                "https://raw.githubusercontent.com/plotly/dash-sample-apps/master/apps/dash-financial-report/assets/base.css",
                'https://codepen.io/chriddyp/pen/bWLwgP.css',
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://codepen.io/dmcomfort/pen/JzdzEZ.css",]
                # "https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"]

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets, url_base_pathname='/cc-travel-report/paid-search/')
app = dash.Dash(
	__name__,
	url_base_pathname='/',
	meta_tags=[{"name": "viewport", "content": "width=device-width"}],
	external_stylesheets=external_css,
	external_scripts=external_js
	)

server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Jerry Yeh - 2020</div>
    </body>
</html>
'''
app.title = 'Covid19 Reports'

app.layout = html.Div([
	dcc.Location(id='url', refresh=False),
	html.Div(id='page-content')
])


# Update page
# # # # # # # # #
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
	if pathname == '/national':
		return nationalDisplay.nationalDisplay
	elif pathname == '/international':
		return internationalDisplay.internationalDisplay
	else:
		return display.default_display


    # if pathname == '/cc-travel-report' or pathname == '/cc-travel-report/overview-birst/':
    #     return layout_birst_category
    # elif pathname == '/cc-travel-report/overview-ga/':
    #     return layout_ga_category
    # elif pathname == '/cc-travel-report/paid-search/':
    #     return layout_paid_search
    # elif pathname == '/cc-travel-report/display/':
    #     return layout_display
    # elif pathname == '/cc-travel-report/publishing/':
    #     return layout_publishing
    # elif pathname == '/cc-travel-report/metasearch-and-travel-ads/':
    #     return layout_metasearch
    # else:
    #     return noPage

# app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
	app.run_server(debug=True)

