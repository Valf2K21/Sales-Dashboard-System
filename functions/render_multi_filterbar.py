'''
    The Sales Dashboard System is a web application for analyzing vehicle sales performance according to five categories: model name, model series, salesman, month, and quarter.
    Copyright (C) 2023 Valfrid Galinato
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# import dependencies
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc

# import user-created dependencies
import classes.ComponentSchema as CSchema
import classes.ComponentStyles as CStyles
import classes.ZoneSchema as ZSchema
import classes.ZoneStyles as ZStyles

# create a function to construct the multi filterbar
def render_multi_filterbar(app: Dash, df_sales: pd.DataFrame, data_col: str, time_col: str, col_title: str, time_title: str) -> html.Div:
    # use df[colname].tolist() function to retrieve that column's values and store it in a variable
    data_cats: list[str] = df_sales[data_col].tolist()

    # use set() function to convert data_cats into a set for deduplication, then sorted() function to sort it
    unique_cats = sorted(set(data_cats), key = str)

    # create an offcanvas div element for the multi filterbar, and store it in a variable
    offcanvas = html.Div(
        [
            # element 1: offcanvas opener button element via dbc.Button() function
            dbc.Button('FILTER DATA', id = CSchema.OPEN_OFFCANVAS, n_clicks = 0, style = CStyles.OFFCANVAS_BUTTON_STYLE),

            # element 2: hidden offcanvas element via dbc.Offcanvas() function
            dbc.Offcanvas(
                # element 1: multi filterbar and select all buttons div element
                html.Div(
                    [
                        # element 1: first filterbar title
                        html.H5('FILTER BY ' + col_title + '', style = CStyles.MULTI_FILTERTITLE_STYLE),

                        # element 2: row element via dbc.Row() function
                        dbc.Row(
                            [
                                # element 1: column element via dbc.Col() function
                                dbc.Col(
                                    # element 1: filterbar dropdown element via dcc.Dropdown() function
                                    dcc.Dropdown(
                                        # use a schema from CSchema to set this element's id
                                        id = CSchema.DATACATEGORY_FILTER_ONE,

                                        # use a for-loop to loop through contents of unique_cats and set this element's options
                                        options = [{'label': cat, 'value': cat} for cat in unique_cats],

                                        # set this element's initial value
                                        value = unique_cats,

                                        # set this element's multi parameter to True
                                        multi = True,

                                        # use a style from CStyles to set this element's CSS style
                                        style = CStyles.MULTI_DROPDOWN_STYLE
                                    ),

                                    # set this element's width parameter to auto
                                    width = 'auto'
                                ),

                                # element 2: column element via dbc.Col() function
                                dbc.Col(
                                    # element 1: select all button element
                                    html.Button(
                                        # use a schema from CSchema to set this element's id
                                        id = CSchema.SELECT_ALL_CATEGORIES_BUTTON_ONE,

                                        # use className parameter to state this element's CSS class
                                        className = 'dropdown-button',

                                        # use children parameter to define this element's sub-elements
                                        children = ['SELECT ALL'],

                                        # use a style from CStyles to set this element's CSS style
                                        style = CStyles.MULTI_BUTTON_STYLE
                                    ),

                                    # set this element's width parameter to auto
                                    width = 'auto'
                                )
                            ]
                        ),

                        # element 3: line break element
                        html.Br(),

                        # element 4: second filterbar title
                        html.H5('FILTER BY ' + time_title + '', style = CStyles.MULTI_FILTERTITLE_STYLE),

                        # element 5: row element via dbc.Row() function
                        dbc.Row(
                            [
                                # element 1: column element via dbc.Col() function
                                dbc.Col(
                                    # element 1: filterbar dropdown element via dcc.Dropdown() function
                                    dcc.Dropdown(
                                        # use a schema from CSchema to set this element's id
                                        id = CSchema.DATACATEGORY_FILTER_TWO,

                                        # use a for-loop to loop through contents of time_col and set this element's options
                                        options = [{'label': cat, 'value': cat} for cat in time_col],

                                        # set this element's initial value
                                        value = time_col,

                                        # set this element's multi parameter to True
                                        multi = True,

                                        # use a style from CStyles to set this element's CSS style
                                        style = CStyles.MULTI_DROPDOWN_STYLE
                                    ),

                                    # set this element's width parameter to auto
                                    width = 'auto'
                                ),

                                # element 2: column element via dbc.Col() function
                                dbc.Col(
                                    # element 1: select all button element
                                    html.Button(
                                        # use a schema from CSchema to set this element's id
                                        id = CSchema.SELECT_ALL_CATEGORIES_BUTTON_TWO,

                                        # use className parameter to state this element's CSS class
                                        className = 'dropdown-button',

                                        # use children parameter to define this element's sub-elements
                                        children = ['SELECT ALL'],

                                        # use a style from CStyles to set this element's CSS style
                                        style = CStyles.MULTI_BUTTON_STYLE
                                    ),

                                    # set this element's width parameter to auto
                                    width = 'auto'
                                )
                            ]
                        )
                    ]
                ),

                # set this element's title
                title = 'FILTERS',

                # use a schema from ZSchema to set this element's id
                id = ZSchema.OFFCANVAS_ZONE,

                # set this element's is_open parameter to False
                is_open = False,

                # set this element's placement parameter to top
                placement = 'top',

                # use a style from ZStyles to set this element's CSS style
                style = ZStyles.ADVANCED_OFFCANVAS_STYLE
            )
        ]
    )

    # return offcanvas
    return offcanvas, unique_cats