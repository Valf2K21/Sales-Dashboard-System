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
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# import user-created dependencies
import classes.ColumnSchema as ColSchema
import classes.ComponentSchema as ComSchema
import classes.ComponentStyles as CStyles
import classes.ZoneStyles as ZStyles

# create a function to construct the advanced sales chart
def render_advanced_saleschart(app: Dash, df_sales: pd.DataFrame, cat_col: str, time_col: str, chart_title: str) -> html.Div():
    # use px.bar() function to create a Plotly bar chart and store it in a variable
    fig = px.bar(df_sales, x = time_col, y = ColSchema.SALES, color = cat_col, text = ColSchema.SALES, title = chart_title)

    # store the bar chart's x-axis and y-axis titles in their respective variables
    xaxis_title = fig.layout.xaxis.title.text
    yaxis_title = fig.layout.yaxis.title.text

    # use .update_layout() function to modify some of the bar chart's layout content
    fig.update_layout(
        # open this layout's legend dictionary
        legend = dict(
            # modify the legend's title to add new instructions on how to use it
            title = "LEGEND:<br><span style = 'color: red;'>(single-click to select/deselect a category)<br>(double-click to focus to a category)<br></span>"
        ),

        # open this layout's x-axis dictionary
        xaxis = dict(
            # open x-axis' title dictionary
            title = dict(
                # modify the x-axis' text to capitalize it
                text = xaxis_title.upper()
            )
        ),

        # open this layout's y-axis dictionary
        yaxis = dict(
            # open y-axis' title dictionary
            title = dict(
                # modify the y-axis' text to capitalize it
                text = yaxis_title.upper()
            )
        )
    )

    # return a div element containing the created bar chart
    return html.Div(
        # use a schema from ComoSchema to set this element's id
        id = ComSchema.ADVANCED_BAR_GRAPH,

        # use children parameter to define this element's sub-elements
        children = [
            # element 1: graph element via dcc.Graph() function
            dcc.Graph(figure = fig, style = CStyles.GRAPH_STYLE)
        ],

        # use a style from ZStyles to set this element's CSS style
        style = ZStyles.GRAPH_STYLE
    )