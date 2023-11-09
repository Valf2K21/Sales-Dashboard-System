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
from dash import Dash, html

# import user-created dependencies
import classes.ZoneSchema as ZSchema
import classes.ZoneStyles as ZStyles
from functions.render_navbar import render_navbar

# create a function to construct the zone layouts
def create_layout(app: Dash) -> html.Div:
    # create a layout div element using html.Div() function, then return it
    return html.Div(
        # use className parameter to state this element's CSS class
        className = 'app-div',

        # use children parameter to define this element's sub-elements
        children = [
            # element 1: navbar zone div element
            html.Div(
                # use a schema from ZSchema to set this element's id
                id = ZSchema.NAVBAR_ZONE,

                # use children parameter to define this element's sub-elements
                children = render_navbar(app) if render_navbar(app) else [],

                # use a style from ZStyles to set this element's CSS style
                style = ZStyles.NAVBAR_STYLE
            ),

            # element 2: graph zone div element
            html.Div(
                # use a schema from ZSchema to set this element's id
                id = ZSchema.GRAPH_ZONE,

                # use a style from ZStyles to set this element's CSS style
                style = ZStyles.GRAPH_STYLE
            ),

            # element 3: filterbar zone div element
            html.Div(
                # use a schema from ZSchema to set this element's id
                id = ZSchema.FILTERBAR_ZONE,

                # use a style from ZStyles to set this element's CSS style
                style = ZStyles.FILTERBAR_STYLE
            ),

            # element 4: dummy zone div element (for year selector dropdown component's callback() function)
            html.Div(
                # use a schema from ZSchema to set this element's id
                id = ZSchema.DUMMY_ZONE
            )
        ]
    )