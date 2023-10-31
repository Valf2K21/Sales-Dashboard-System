# import dependencies
import dash_bootstrap_components as dbc
from dash import Dash, html, callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# import user-created dependencies
import classes.ColumnSchema as ColSchema
import classes.ComponentSchema as ComSchema
import classes.MapperOrder as MOrder
import classes.NavigationSchema as NSchema
import classes.TitleSchema as TSchema
import classes.ZoneSchema as ZSchema
from functions.create_layout import create_layout
from functions.query_data import query_data
from functions.render_advanced_saleschart import render_advanced_saleschart
from functions.render_basic_saleschart import render_basic_saleschart
from functions.render_filterbar import render_filterbar
from functions.render_multi_filterbar import render_multi_filterbar

# create a function containing the Dash web application instance
def main() -> None:
    # create a Dash web application instance
    app = Dash(external_stylesheets = [dbc.themes.SIMPLEX], suppress_callback_exceptions = True)

    # set the web application's title
    app.title = 'Sales Dashboard System'

    # call create_layout() function to set the web application's layout
    app.layout = create_layout(app)

    # create a callback that calls years_selected() callback function below, and sets the year selector elements' values as input, and dummy div element as output
    @app.callback(Output(ZSchema.DUMMY_ZONE, 'children'), [Input(ComSchema.YEAR_SELECTOR_START, 'value'), Input(ComSchema.YEAR_SELECTOR_END, 'value')])

    # create user-defined callback function for storing user-selected years
    def years_selected(year_one, year_two):
        # set year_start and year_end as global to make it accessible outside function
        global year_start
        global year_end

        # store passed year_one and year_two in their respective variables
        year_start = year_one
        year_end = year_two

        # use Preventupdate to tell Dash not to update dummy div element
        raise PreventUpdate
    
    # create a callback that calls update_chart_content() callback function below, and sets the navbar link elements' clicks and status as input, and filterbar and graph zones as output
    @app.callback([Output(ZSchema.FILTERBAR_ZONE, 'children'), Output(ZSchema.GRAPH_ZONE, 'children')], 
                  [Input(NSchema.SALES_MODELNAME_LINK, 'n_clicks'), Input(NSchema.SALES_MODELSERIES_LINK, 'n_clicks'), Input(NSchema.SALES_SALESMAN_LINK, 'n_clicks'), Input(NSchema.SALES_MONTH_LINK, 'n_clicks'),
                   Input(NSchema.SALES_QUARTER_LINK, 'n_clicks'), Input(NSchema.MONTHLY_MODELNAME_LINK, 'n_clicks'), Input(NSchema.MONTHLY_MODELSERIES_LINK, 'n_clicks'), Input(NSchema.MONTHLY_SALESMAN_LINK, 'n_clicks'),
                   Input(NSchema.QUARTERLY_MODELNAME_LINK, 'n_clicks'), Input(NSchema.QUARTERLY_MODELSERIES_LINK, 'n_clicks'), Input(NSchema.QUARTERLY_SALESMAN_LINK, 'n_clicks')],
                  [State(NSchema.SALES_MODELNAME_LINK, 'active'), State(NSchema.SALES_MODELSERIES_LINK, 'active'), State(NSchema.SALES_SALESMAN_LINK, 'active'), State(NSchema.SALES_MONTH_LINK, 'active'),
                   State(NSchema.SALES_QUARTER_LINK, 'active'), State(NSchema.MONTHLY_MODELNAME_LINK, 'active'), State(NSchema.MONTHLY_MODELSERIES_LINK, 'active'), State(NSchema.MONTHLY_SALESMAN_LINK, 'active'),
                   State(NSchema.QUARTERLY_MODELNAME_LINK, 'active'), State(NSchema.QUARTERLY_MODELSERIES_LINK, 'active'), State(NSchema.QUARTERLY_SALESMAN_LINK, 'active')])
    
    # create user-defined callback function for updating chart content
    def update_chart_content(model_name_clicks, model_series_clicks, sales_man_clicks, month_clicks, quarter_clicks, monthly_model_name_clicks, monthly_model_series_clicks, monthly_sales_man_clicks, quarterly_model_name_clicks,
                             quarterly_model_series_clicks, quarterly_sales_man_clicks, model_name_active, model_series_active, sales_man_active, month_active, quarter_active, monthly_model_name_active, monthly_model_series_active,
                             monthly_sales_man_active, quarterly_model_name_active, quarterly_model_series_active, quarterly_sales_man_active):
        # set button_id as global to make it accessible outside function
        global button_id

        # initialize two variables as empty div elements before conducting if-elif conditional statements
        filter_element = html.Div()
        graph_element = html.Div()

        # store the callback context in a variable
        ctx = callback_context

        # if-else statement to check if something triggered the navbar callback
        if not ctx.triggered:
            # keep the two variables in its default state
            filter_element = html.Div()
            graph_element = html.Div()

        else:
            # save the button id that triggered the navbar callback in a variable
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]

            # set unfiltered as global to make it accessible outside function
            global unfiltered

            # call query_data() function to get the sales dataframes needed
            model_name_sales, model_series_sales, sales_man_sales, month_sales, quarter_sales, model_name_month_sales, model_series_month_sales, sales_man_month_sales, model_name_quarter_sales, model_series_quarter_sales, sales_man_quarter_sales = query_data(year_start, year_end)

            # if-elif-else statements to determine the filterbar and sales chart to display, and unfiltered to globalize
            if button_id == NSchema.SALES_MODELNAME_LINK:
                # call render_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_filterbar(app, model_name_sales, ColSchema.MODELNAME, 'FILTER BY MODEL NAME')

                # call render_basic_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_basic_saleschart(app, model_name_sales, ColSchema.MODELNAME, TSchema.MODELNAMETITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = model_name_sales

            elif button_id == NSchema.SALES_MODELSERIES_LINK:
                # call render_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_filterbar(app, model_series_sales, ColSchema.MODELSERIES, 'FILTER BY MODEL SERIES')

                # call render_basic_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_basic_saleschart(app, model_series_sales, ColSchema.MODELSERIES, TSchema.MODELSERIESTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = model_series_sales

            elif button_id == NSchema.SALES_SALESMAN_LINK:
                # call render_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_filterbar(app, sales_man_sales, ColSchema.SALESMAN, 'FILTER BY SALESMAN')

                # call render_basic_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_basic_saleschart(app, sales_man_sales, ColSchema.SALESMAN, TSchema.SALESMANTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = sales_man_sales

            elif button_id == NSchema.SALES_MONTH_LINK:
                # call render_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_filterbar(app, month_sales, ColSchema.MONTH, 'FILTER BY MONTH')

                # call render_basic_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_basic_saleschart(app, month_sales, ColSchema.MONTH, TSchema.MONTHTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = month_sales

            elif button_id == NSchema.SALES_QUARTER_LINK:
                # call render_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_filterbar(app, quarter_sales, ColSchema.QUARTER, 'FILTER BY QUARTER')

                # call render_basic_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_basic_saleschart(app, quarter_sales, ColSchema.QUARTER, TSchema.QUARTERTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = quarter_sales

            elif button_id == NSchema.MONTHLY_MODELNAME_LINK:
                # call render_multi_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_multi_filterbar(app, model_name_sales, ColSchema.MODELNAME, MOrder.MONTH_ORDER, 'MODEL NAME', 'MONTH')

                # call render_advanced_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_advanced_saleschart(app, model_name_month_sales, ColSchema.MODELNAME, ColSchema.MONTH, TSchema.MODELNAMEBYMONTHTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = model_name_month_sales

            elif button_id == NSchema.MONTHLY_MODELSERIES_LINK:
                # call render_multi_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_multi_filterbar(app, model_series_sales, ColSchema.MODELSERIES, MOrder.MONTH_ORDER, 'MODEL SERIES', 'MONTH')

                # call render_advanced_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_advanced_saleschart(app, model_series_month_sales, ColSchema.MODELSERIES, ColSchema.MONTH, TSchema.MODELSERIESBYMONTHTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = model_series_month_sales

            elif button_id == NSchema.MONTHLY_SALESMAN_LINK:
                # call render_multi_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_multi_filterbar(app, sales_man_sales, ColSchema.SALESMAN, MOrder.MONTH_ORDER, 'SALESMAN', 'MONTH')

                # call render_advanced_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_advanced_saleschart(app, sales_man_month_sales, ColSchema.SALESMAN, ColSchema.MONTH, TSchema.SALESMANBYMONTHTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = sales_man_month_sales

            elif button_id == NSchema.QUARTERLY_MODELNAME_LINK:
                # call render_multi_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_multi_filterbar(app, model_name_sales, ColSchema.MODELNAME, MOrder.QUARTER_ORDER, 'MODEL NAME', 'QUARTER')

                # call render_advanced_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_advanced_saleschart(app, model_name_quarter_sales, ColSchema.MODELNAME, ColSchema.QUARTER, TSchema.MODELNAMEBYQUARTERTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = model_name_quarter_sales

            elif button_id == NSchema.QUARTERLY_MODELSERIES_LINK:
                # call render_multi_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_multi_filterbar(app, model_series_sales, ColSchema.MODELSERIES, MOrder.QUARTER_ORDER, 'MODEL SERIES', 'QUARTER')

                # call render_advanced_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_advanced_saleschart(app, model_series_quarter_sales, ColSchema.MODELSERIES, ColSchema.QUARTER, TSchema.MODELSERIESBYQUARTERTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = model_series_quarter_sales

            elif button_id == NSchema.QUARTERLY_SALESMAN_LINK:
                # call render_multi_filterbar() function to set the web application's filterbar, and store it in a variable
                filter_element = render_multi_filterbar(app, sales_man_sales, ColSchema.SALESMAN, MOrder.QUARTER_ORDER, 'SALESMAN', 'QUARTER')

                # call render_advanced_saleschart() function to set the web application's graph, and store it in a variable
                graph_element = render_advanced_saleschart(app, sales_man_quarter_sales, ColSchema.SALESMAN, ColSchema.QUARTER, TSchema.SALESMANBYQUARTERTITLE)

                # store passed sales dataframe to unfiltered
                unfiltered = sales_man_quarter_sales

            else:
                # keep the two variables in its default state
                filter_element = html.Div()
                graph_element = html.Div()

        # return selected filter_element and graph_element
        return [filter_element, graph_element]
    
    # create a callback that calls toggle_offcanvas() callback function below, and sets the offcanvas button element's click and open status as input, and offcanvas zone' open status as output
    @app.callback(Output(ZSchema.OFFCANVAS_ZONE, 'is_open'), Input(ComSchema.OPEN_OFFCANVAS, 'n_clicks'), State(ZSchema.OFFCANVAS_ZONE, 'is_open'))

    # create user-defined callback function for opening and closing offcanvas zone
    def toggle_offcanvas(n1, is_open):
        # if-statement to check if offcanvas button element is clicked
        if n1:
            # return a closed offcanvas zone
            return not is_open
        
        # return an opened offcanvas zone
        return is_open
    
    # create a callback that calls select_all_categories_one() callback function below, and sets the first filterbar's select all button element's clicks as input, and the first filterbar element's values as output
    @app.callback(Output(ComSchema.DATACATEGORY_FILTER_ONE, 'value'), Input(ComSchema.SELECT_ALL_CATEGORIES_BUTTON_ONE, 'n_clicks'))

    # create user-defined callback function for filling up the first filterbar element with all unique values
    def select_all_categories_one(_: int) -> list[str]:
        # if-elif statement to determine the unique_cats global variable to use depending on button_id
        if button_id in [NSchema.SALES_MODELNAME_LINK, NSchema.SALES_MODELSERIES_LINK, NSchema.SALES_SALESMAN_LINK, NSchema.SALES_MONTH_LINK, NSchema.SALES_QUARTER_LINK]:
            # fetch most recent values of render_filterbar() function's unique_cats global variable and return it
            return render_filterbar.unique_cats
        
        elif button_id in [NSchema.MONTHLY_MODELNAME_LINK, NSchema.MONTHLY_MODELSERIES_LINK, NSchema.MONTHLY_SALESMAN_LINK, NSchema.QUARTERLY_MODELNAME_LINK, NSchema.QUARTERLY_MODELSERIES_LINK, NSchema.QUARTERLY_SALESMAN_LINK]:
            # fetch most recent values of render_multi_filterbar() function's unique_cats global variable and return it
            return render_multi_filterbar.unique_cats
        
    # create a callback that calls select_all_categories_two() callback function below, and sets the second filterbar's select all button element's clicks as input, and the second filterbar element's values as output
    @app.callback(Output(ComSchema.DATACATEGORY_FILTER_TWO, 'value'), Input(ComSchema.SELECT_ALL_CATEGORIES_BUTTON_TWO, 'n_clicks'))

    # create user-defined callback function for filling up the second filterbar element with all unique values
    def select_all_categories_two(_: int) -> list[str]:
        # fetch most recent values of render_multi_filterbar() function's time global variable and return it
        return render_multi_filterbar.time
    
    # create a callback that calls update_bar_chart_basic() callback function below, and sets the first filterbar element's values as input, and the basic bar chart as output
    @app.callback(Output(ComSchema.BASIC_BAR_GRAPH, 'children'), Input(ComSchema.DATACATEGORY_FILTER_ONE, 'value'))

    # create user-defined callback function for updating basic bar chart
    def update_bar_chart_basic(filtered_cats: list[str]) -> html.Div:
        # fetch dataframe of unfiltered global variable, and filter it with filtered_cats using .query() function
        filtered_sales_df = unfiltered.query(f'{render_basic_saleschart.col} in @filtered_cats')

        # if-statement to check if filtered_sales_df has no content
        if filtered_sales_df.shape[0] == 0:
            # return a div element with a notice
            return html.Div('NO DATA SELECTED')
        
        # call render_basic_saleschart() function to update the basic bar chart and return it
        return render_basic_saleschart(app, filtered_sales_df, render_basic_saleschart.col, render_basic_saleschart.title)
    
    # create a callback that calls update_bar_chart_advanced() callback function below, and sets the first and second filterbar elements' values as input, and the advanced bar chart as output
    @app.callback(Output(ComSchema.ADVANCED_BAR_GRAPH, 'children'), [Input(ComSchema.DATACATEGORY_FILTER_ONE, 'value'), Input(ComSchema.DATACATEGORY_FILTER_TWO, 'value')])

    # create user-defined callback function for updating advanced bar chart
    def update_bar_chart_advanced(filtered_cats: list[str], filtered_time: list[str]) -> html.Div:
        # fetch dataframe of unfiltered global variable, and filter it with filtered_cats and filtered_time using .query() function
        filtered_sales_df = unfiltered.query(f'{render_advanced_saleschart.col} in @filtered_cats and {render_advanced_saleschart.col2} in @filtered_time')

        # if-statement to check if filtered_sales_df has no content
        if filtered_sales_df.shape[0] == 0:
            # return a div element with a notice
            return html.Div('NO DATA SELECTED')
        
        # call render_advanced_saleschart() function to update the advanced bar chart and return it
        return render_advanced_saleschart(app, filtered_sales_df, render_advanced_saleschart.col, render_advanced_saleschart.col2, render_advanced_saleschart.title)
    
    # run Dash web application instance
    app.run()

# if-statement to run main() function
if __name__ == '__main__':
    main()