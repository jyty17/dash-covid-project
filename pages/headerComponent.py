import dash_core_components as dcc
import dash_html_components as html

import pathlib
import os

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "275px",
    "padding": "0 1rem",
    "paddingTop": "20px",
    "paddingLeft": "20px",
    # "background-color": "#f8f9fa",
    "background-color": "#9B85FF",
    'display': 'flex',
    'flex-direction': 'column'
}

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ], style=SIDEBAR_STYLE)

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='/assets/SARS-CoV-2.png', alt="", height='120', className="rotate")
        ], className="py-5"),

        # html.Div([
        #     dcc.Link('Full View   ', href='/cc-travel-report/full-view')
        # ], className="two columns page-view no-print")

    ], className="")
    return logo


def get_header():
    header = html.Div([
        html.Div([
            html.A(
                html.H1('Covid-19 Case Report', style={"font-size": "5rem"}),
                href='/',
                className='text-decoration-none header-title'
                )
        ], style={
            "color": "#1D3461"
            })

    ], className="header")
    return header

MENU_STYLE = {
    "color": "white"
}
TITLE_STYLE = {}
ANCHOR_STYLE = {
    "fontSize": "3rem"
    }

def get_menu():
    menu = html.Div([
        html.H2("Navigation", style={'fontSize': '4rem'}),

        dcc.Link('Overview   ', href='/', className="text-white py-2", style=ANCHOR_STYLE),

        dcc.Link('World   ', href='/international', className="text-white py-2", style=ANCHOR_STYLE),

        dcc.Link('USA   ', href='/national', className="text-white py-2", style=ANCHOR_STYLE),

        dcc.Link('Sources   ', href='/sources', className="text-white py-2", style=ANCHOR_STYLE),

        # html.A('OWID   ', href='https://github.com/owid/covid-19-data/tree/master/public/data/', target="_blank", className="text-white py-2", style=ANCHOR_STYLE),

        # html.A('NYTimes   ', href='https://github.com/nytimes/covid-19-data', target="_blank", className="text-white py-2", style=ANCHOR_STYLE),

        html.A('Github   ', href='https://github.com/jyty17/dash-covid-project', target="_blank", className="text-white py-2", style=ANCHOR_STYLE),

    ], className="btn-group-vertical", style=MENU_STYLE)
    return menu