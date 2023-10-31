# import dependencies
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# import user-created dependencies
import classes.ColumnSchema as ColSchema
import classes.ComponentSchema as ComSchema
import classes.ComponentStyles as CStyles
import classes.ZoneStyles as ZStyles

# create a function to construct the basic sales chart
def render_basic_saleschart(app: Dash, df_sales: pd.DataFrame, data_col: str, chart_title: str) -> html.Div:
    # if-else statement to determine the chart direction to use
    if chart_title == 'SALES BY MONTH' or chart_title == 'SALES BY QUARTER':
        # set direction parameter to use as vertical
        direction = 'v'

        # set x-axis parameter to use as data_col
        xaxis = data_col
        
        # use a schema from ColSchema to set the y-axis to use
        yaxis = ColSchema.SALES

        # use a schema from ColSchema to set the hue to use
        hue = ColSchema.SALES

    else:
        # set direction parameter to use as horizontal
        direction = 'h'

        #  use a schema from ColSchema to set the x-axis to use
        xaxis = ColSchema.SALES

        # set y-axis parameter to use as data_col
        yaxis = data_col

        # set hue parameter to use as data_col
        hue = data_col

    # set col and title as global to make it accessible outside function
    global col
    global title

    # save passed data_col and chart_title to their respective variables
    col = data_col
    title = chart_title
    
    # use px.bar() function to create a Plotly bar chart and store it in a variable
    fig = px.bar(df_sales, x = xaxis, y = yaxis, color = hue, text = ColSchema.SALES, title = chart_title, orientation = direction)

    # use .update_traces() function to modify the bar chart's textposition parameter
    fig.update_traces(textposition = 'outside')

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
        id = ComSchema.BASIC_BAR_GRAPH,

        # use children parameter to define this element's sub-elements
        children = [
            # element 1: graph element via dcc.Graph() function
            dcc.Graph(figure = fig, style = CStyles.GRAPH_STYLE)
        ],

        # use a style from ZStyles to set this element's CSS style
        style = ZStyles.GRAPH_STYLE
    )