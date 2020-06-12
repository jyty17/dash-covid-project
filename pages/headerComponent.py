import dash_core_components as dcc
import dash_html_components as html

import pathlib
import os

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='/assets/SARS-CoV-2.png', alt="", height='150')
        ], className="ten columns padded"),

        # html.Div([
        #     dcc.Link('Full View   ', href='/cc-travel-report/full-view')
        # ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([
        html.Div([
            html.H5('Covid-19 Cases Report')
                # 'House Stark Performance Marketing Report')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/', className="tab first"),

        dcc.Link('USA   ', href='/national', className="tab"),

        dcc.Link('World   ', href='/international', className="tab"),

        html.A('OWID   ', href='https://github.com/owid/covid-19-data/tree/master/public/data/', target="_blank", className="tab"),

        html.A('NYTimes   ', href='https://github.com/nytimes/covid-19-data', target="_blank", className="tab"),

        html.A('Github   ', href='/cc-travel-report/metasearch-and-travel-ads/', target="_blank", className="tab"),

    ], className="row all-tabs")
    return menu