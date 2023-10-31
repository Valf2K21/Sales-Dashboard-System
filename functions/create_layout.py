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