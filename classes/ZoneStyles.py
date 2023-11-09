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

# set styles for zones
NAVBAR_STYLE = {'background-color': '#FCD5D1', 'height': '100%', 'maxHeight': '100%', 'minHeight': '100%', 'width': 'calc(100vw - 85vw)', 'maxWidth': '250px', 'minWidth': '250px', 'position': 'fixed', 'top': '0', 'left': '0', 'padding': '20px'}
FILTERBAR_STYLE = {'display': 'flex', 'background-color': 'red', 'top': '0', 'right': '0', 'left': '0', 'width': '100vw', 'maxWidth': '100vw', 'minWidth': '100vw', 'position': 'fixed', 'margin-top': '60px'}
GRAPH_STYLE = {'display': 'flex', 'background-color': 'transparent', 'bottom': '0', 'right': '0', 'height': 'calc(100vh - 40px)', 'maxHeight': 'calc(100vh - 40px)', 'minHeight': 'calc(100vh - 40px)', 'width': 'calc(100vw - 250px)', 'maxWidth': 'calc(100vw - 250px)', 'minWidth': 'calc(100vw - 250px)', 'position': 'fixed'}
BASIC_OFFCANVAS_STYLE = {'background-color': 'red', 'height': '', 'maxHeight': '100px', 'minHeight': '100px', 'color': 'white'}
ADVANCED_OFFCANVAS_STYLE = {'background-color': 'red', 'height': '', 'maxHeight': '300px', 'minHeight': '300px', 'color': 'white'}