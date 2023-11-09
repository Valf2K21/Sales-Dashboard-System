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

# set mapping dictionaries and order lists prior to column generation
# mapping dictionary of modelnames for modelseries column generation
MODELNAME_MAPPER = {
    'SEDAN': ['FWD SEDAN', 'RWD SEDAN', 'AWD SEDAN'],
    'SUV': ['FWD SUV', 'RWD SUV', 'AWD SUV'],
    'TRUCK': ['FWD TRUCK', 'RWD TRUCK', 'AWD TRUCK']
}

# mapping dictionary of months for month column generation
MONTH_MAPPER = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

# mapping dictionary of quarter for quarter column generation
QUARTER_MAPPER = {
    1: '1Q',
    2: '2Q',
    3: '3Q',
    4: '4Q'
}

# ordered list of months
MONTH_ORDER = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# ordered list of quarters
QUARTER_ORDER = ['1Q', '2Q', '3Q', '4Q']

# ordered list of years
YEAR_ORDER = [{'label': '2021', 'value': '2021'}, {'label': '2022', 'value': '2022'}, {'label': '2023', 'value': '2023'}]