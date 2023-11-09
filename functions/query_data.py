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
import psycopg2

# import user-created dependencies
import classes.MapperOrder as MOrder
from .config import config

# create a function to gather and process data
def query_data(start: str, end: str):
    # call config() function and store server parameters in a variable
    params = config()

    # use psycopg2.connect() function to connect to PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in params variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to query and fetch sales data
    c.execute(f"SELECT p.model_name, p.sales_man, si.invoice_date FROM tb_purchase p INNER JOIN tb_sales_invoice si ON p.purchase_no = si.purchase_no WHERE si.invoice_stat = 1 AND si.invoice_date >= '{start}-01-01' AND si.invoice_date <= '{end}-12-31' ORDER BY si.invoice_date ASC;")
    sales_data = c.fetchall()

    # use pd.dataframe() function to store fetched sales data into a dataframe
    sales_df = pd.DataFrame(sales_data, columns = ['model_name', 'sales_man', 'invoice_date'])

    # close cursor and connect objects after the process
    c.close()
    conn.close()

    # use df['colname'].replace() function to conduct data cleaning by standardizing duplicate values
    sales_df['sales_man'] = sales_df['sales_man'].replace(['VALLFRID GALINATO', 'VALFRED GALINATO'], ['VALFRID GALINATO', 'VALFRID GALINATO'])

    # use pd.to_datetime(df['colname']).dt.month and .dt.quarter to conduct data wrangling and extract month and quarter into their new columns, respectively
    sales_df['month'] = pd.to_datetime(sales_df['invoice_date']).dt.month
    sales_df['quarter'] = pd.to_datetime(sales_df['invoice_date']).dt.quarter

    # use a mapper from MOrder to conduct data wrangling by grouping model names and creating a new column
    sales_df['model_series'] = sales_df['model_name'].apply(lambda x: next((k for k, v in MOrder.MODELNAME_MAPPER.items() if x in v), None))

    # use a mapper from MOrder to change the numerical months and quarters into string values
    sales_df['month'] = sales_df['month'].map(MOrder.MONTH_MAPPER)
    sales_df['quarter'] = sales_df['quarter'].map(MOrder.QUARTER_MAPPER)

    # use pd.Categorical() function to set the values of month and quarter columns into categories
    sales_df['month'] = pd.Categorical(sales_df['month'], categories = MOrder.MONTH_ORDER, ordered = True)
    sales_df['quarter'] = pd.Categorical(sales_df['quarter'], categories = MOrder.QUARTER_ORDER, ordered = True)

    # use df.sort_values() function to sort the values of month and quarter columns
    sales_df = sales_df.sort_values(['month', 'quarter'])

    # use .value_counts().reset_index() functions to count instances of unique values in various areas, then create five new basic sales dataframes
    model_name_sales = sales_df['model_name'].value_counts().reset_index()
    model_series_sales = sales_df['model_series'].value_counts().reset_index()
    sales_man_sales = sales_df['sales_man'].value_counts().reset_index()
    month_sales = sales_df.groupby('month', observed = False)['model_name'].count().reset_index()
    quarter_sales = sales_df.groupby('quarter', observed = False)['model_name'].count().reset_index()

    # use pd.MultiIndex.from_product() function to count instances of unique columnA-columnB combinations
    model_name_month = pd.MultiIndex.from_product([sales_df['model_name'].unique(), sales_df['month'].unique()], names = ['model_name', 'month'])
    model_series_month = pd.MultiIndex.from_product([sales_df['model_series'].unique(), sales_df['month'].unique()], names = ['model_series', 'month'])
    sales_man_month = pd.MultiIndex.from_product([sales_df['sales_man'].unique(), sales_df['month'].unique()], names = ['sales_man', 'month'])
    model_name_quarter = pd.MultiIndex.from_product([sales_df['model_name'].unique(), sales_df['quarter'].unique()], names = ['model_name', 'quarter'])
    model_series_quarter = pd.MultiIndex.from_product([sales_df['model_series'].unique(), sales_df['quarter'].unique()], names = ['model_series', 'quarter'])
    sales_man_quarter = pd.MultiIndex.from_product([sales_df['sales_man'].unique(), sales_df['quarter'].unique()], names = ['sales_man', 'quarter'])

    # use pd.DataFrame() function to create six new advanced sales dataframes using the variables above
    model_name_month_sales = pd.DataFrame(index = model_name_month).reset_index()
    model_series_month_sales = pd.DataFrame(index = model_series_month).reset_index()
    sales_man_month_sales = pd.DataFrame(index = sales_man_month).reset_index()
    model_name_quarter_sales = pd.DataFrame(index = model_name_quarter).reset_index()
    model_series_quarter_sales = pd.DataFrame(index = model_series_quarter).reset_index()
    sales_man_quarter_sales = pd.DataFrame(index = sales_man_quarter).reset_index()

    # use pd.merge() function to merge sales_df and each of the six advanced dataframes to fill it up with values
    model_name_month_sales = pd.merge(model_name_month_sales, sales_df.groupby(['model_name', 'month'], observed = False).size().reset_index(name = 'count'), how = 'left')
    model_series_month_sales = pd.merge(model_series_month_sales, sales_df.groupby(['model_series', 'month'], observed = False).size().reset_index(name = 'count'), how = 'left')
    sales_man_month_sales = pd.merge(sales_man_month_sales, sales_df.groupby(['sales_man', 'month'], observed = False).size().reset_index(name = 'count'), how = 'left')
    model_name_quarter_sales = pd.merge(model_name_quarter_sales, sales_df.groupby(['model_name', 'quarter'], observed = False).size().reset_index(name = 'count'), how = 'left')
    model_series_quarter_sales = pd.merge(model_series_quarter_sales, sales_df.groupby(['model_series', 'quarter'], observed = False).size().reset_index(name = 'count'), how = 'left')
    sales_man_quarter_sales = pd.merge(sales_man_quarter_sales, sales_df.groupby(['sales_man', 'quarter'], observed = False).size().reset_index(name = 'count'), how = 'left')

    # use .columns function to give the five basic and six advanced dataframes standard column names
    model_name_sales.columns = ['model_name', 'sales']
    model_series_sales.columns = ['model_series', 'sales']
    sales_man_sales.columns = ['sales_man', 'sales']
    month_sales.columns = ['month', 'sales']
    quarter_sales.columns = ['quarter', 'sales']
    model_name_month_sales.columns = ['model_name', 'month', 'sales']
    model_series_month_sales.columns = ['model_series', 'month', 'sales']
    sales_man_month_sales.columns = ['sales_man', 'month', 'sales']
    model_name_quarter_sales.columns = ['model_name', 'quarter', 'sales']
    model_series_quarter_sales.columns = ['model_series', 'quarter', 'sales']
    sales_man_quarter_sales.columns = ['sales_man', 'quarter', 'sales']

    # use df['colname'].fillna() function to fill missing values with 0
    model_name_month_sales['sales'].fillna(0, inplace = True)
    model_series_month_sales['sales'].fillna(0, inplace = True)
    sales_man_month_sales['sales'].fillna(0, inplace = True)
    model_name_quarter_sales['sales'].fillna(0, inplace = True)
    model_series_quarter_sales['sales'].fillna(0, inplace = True)
    sales_man_quarter_sales['sales'].fillna(0, inplace = True)

    # return five basic and six advanced dataframes
    return model_name_sales, model_series_sales, sales_man_sales, month_sales, quarter_sales, model_name_month_sales, model_series_month_sales, sales_man_month_sales, model_name_quarter_sales, model_series_quarter_sales, sales_man_quarter_sales