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

# set styles for system components
DROPDOWN_STYLE = {'color': 'black', 'width': 'calc(100vw - 160px)', 'maxWidth': 'calc(100vw - 160px)', 'minWidth': 'calc(100vw - 160px)', 'position': 'right', 'margin': '10px', 'margin-right': '30px', 'margin-top': '0px'}
BUTTON_STYLE = {'align-self': 'center', 'height': '40px', 'maxHeight': '40px', 'minHeight': '40px', 'width': '100px', 'maxWidth': '100px', 'minWidth': '100px', 'margin': '10px', 'margin-left': '0px', 'margin-right': '30px', 'margin-top': '0px'}
MULTI_DROPDOWN_STYLE = {'color': 'black', 'width': '97vw', 'maxWidth': '97vw', 'minWidth': '97vw', 'position': 'right', 'margin': '10px', 'margin-left': '0px', 'margin-top': '0px'}
MULTI_BUTTON_STYLE = {'align-self': 'center', 'height': '40px', 'maxHeight': '40px', 'minHeight': '40px', 'width': '97vw', 'maxWidth': '97vw', 'minWidth': '97vw', 'margin': '10px', 'margin-left': '0px', 'margin-right': '30px', 'margin-top': '0px'}
GRAPH_STYLE = {'width': '100%', 'height': '100%'}
FILTERTITLE_STYLE = {'align-self': 'center', 'margin': '20px', 'margin-right': '30px'}
MULTI_FILTERTITLE_STYLE = {'margin-top': '0px', 'margin-right': '30px'}
BRAND_STYLE = {'fontFamily': 'Usuzi, sans-serif', 'fontSize': '45px', 'color': 'red', 'align-self': 'center', 'fontWeight': 'bold'}
LINE_STYLE = {'margin': '8px'}
NAVLINKTITLE_STYLE = {'fontFamily': 'Helvetica, sans-serif', 'fontSize': '20px', 'fontWeight': 'bold'}
NAVLINK_STYLE = {'fontFamily': 'Helvetica, sans-serif'}
OFFCANVAS_BUTTON_STYLE = {'display': 'flex', 'justify-content': 'center', 'background-color': 'red', 'top': '0', 'right': '0', 'height': '40px', 'minHeight': '40px', 'maxHeight': '40px', 'width': 'calc(100vw - 250px)', 'maxWidth': 'calc(100vw - 250px)', 'minWidth': 'calc(100vw - 250px)', 'position': 'fixed'}