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
from dash import Dash, html, dcc

# import user-created dependencies
import classes.ComponentSchema as CSchema
import classes.ComponentStyles as CStyles
import classes.MapperOrder as MOrder
import classes.NavigationSchema as NSchema
import classes.ZoneStyles as ZStyles

# create a function to construct the navbar
def render_navbar(app: Dash) -> html.Div:
    # create a navbar div element using html.Div() function, then return it
    return html.Div(
        # use children parameter to define this element's sub-elements
        children = [
            # element 1: navbar element via dbc.Nav() function
            dbc.Nav(
                # use children parameter to define this element's sub-elements
                children = [
                    # element 1: company name
                    html.H2('ISUZU', style = CStyles.BRAND_STYLE),

                    # element 2: horizontal line element
                    html.Hr(style = CStyles.LINE_STYLE),

                    # element 3: year selector title
                    html.H6('Year Selector', style = CStyles.NAVLINKTITLE_STYLE),

                    # element 4: year start dropdown element via dcc.Dropdown() function
                    dcc.Dropdown(
                        # use a schema from CSchema to set this element's id
                        id = CSchema.YEAR_SELECTOR_START,

                        # use an order from MOrder to set this element's options
                        options = MOrder.YEAR_ORDER,

                        # set this element's initial value
                        value = '2021'
                    ),

                    # element 5: 'to' title
                    html.H6('to', style = CStyles.NAVLINKTITLE_STYLE),

                    # element 6: year end dropdown element via dcc.Dropdown() function
                    dcc.Dropdown(
                        # use a schema from CSchema to set this element's id
                        id = CSchema.YEAR_SELECTOR_END,

                        # use an order from MOrder to set this element's options
                        options = MOrder.YEAR_ORDER,

                        # set this element's initial value
                        value = '2021'
                    ),

                    # element 7: horizontal line element
                    html.Hr(style = CStyles.LINE_STYLE),

                    # element 8: basic dashboards title
                    html.H6('Basic Sales Dashboards', style = CStyles.NAVLINKTITLE_STYLE),

                    # elements 9-13: basic sales graphs navlink elements via dbc.NavLink() function
                    dbc.NavLink('Sales by Model Name', id = NSchema.SALES_MODELNAME_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Sales by Model Series', id = NSchema.SALES_MODELSERIES_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Sales by Salesman', id = NSchema.SALES_SALESMAN_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Sales by Month', id = NSchema.SALES_MONTH_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Sales by Quarter', id = NSchema.SALES_QUARTER_LINK, href = '#', active = 'exact'),

                    # element 14: horizontal line element
                    html.Hr(style = CStyles.LINE_STYLE),

                    # element 15: advanced dashboards title
                    html.H6('Advanced Sales Dashboards', style = CStyles.NAVLINKTITLE_STYLE),

                    # elements 16-21: advanced sales graphs navlink elements via dbc.NavLink() function
                    dbc.NavLink('Monthly Sales by Model Name', id = NSchema.MONTHLY_MODELNAME_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Monthly Sales by Model Series', id = NSchema.MONTHLY_MODELSERIES_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Monthly Sales by Salesman', id = NSchema.MONTHLY_SALESMAN_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Quarterly Sales by Model Name', id = NSchema.QUARTERLY_MODELNAME_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Quarterly Sales by Model Series', id = NSchema.QUARTERLY_MODELSERIES_LINK, href = '#', active = 'exact'),
                    dbc.NavLink('Quarterly Sales by Salesman', id = NSchema.QUARTERLY_SALESMAN_LINK, href = '#', active = 'exact'),
                ],

                # set this element's vertical parameter to True
                vertical = True,

                # set this element's pill parameter to True
                pills = True
            )
        ],

        # use className parameter to state this element's CSS class
        className = 'sidebar',

        # use a style from ZStyles to set this element's CSS style
        style = ZStyles.NAVBAR_STYLE
    )