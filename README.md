# Sales Dashboard System
The Sales Dashboard System is a web application for analyzing vehicle sales performance according to five categories: model name, model series, salesman, month, and quarter.

## License
This project is licensed under the [GNU Affero General Public License (AGPLv3)](LICENSE)

## Tech Stack
- Python - backend programming language
- Dash - data science micro web framework to develop this Python-based web application
- Pandas - Python-based data wrangling and analysis library
- Plotly - Python-based graphing library to create interactive sales dashboards
- PostgreSQL - database creation and data storage of sample vehicle sales records
- Psycopg2 - adapter to connect and interact Python and PostgreSQL
- HTML - frontend markup language via Dash
- CSS - style sheet for HTML via Dash

## Installation
1. Clone this repository:
```cmd
git clone https://github.com/Valf2K21/Sales-Dashboard-System.git
cd Sales-Dashboard-System
```
2. Create virtual environment
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```
3. Install dependencies
```cmd
pip install -r requirements.txt
```
4. Create new database named sales_dashboard_db in PostgreSQL 16's pgAdmin4
5. Use sales_dashboard_db_sample.sql to restore required tables in newly-created database
6. Modify database.ini by changing values of host, user, and password if needed
7. Run Sales Dashboard System
```cmd
python -m main
```

## Demo
[![Sales Dashboard System Demo](https://img.youtube.com/vi/FVIeX-PwF_I/0.jpg)](https://www.youtube.com/watch?v=FVIeX-PwF_I)

## Acknowledgements
The Sales Dashboard System's development was made possible thanks to the following open-source technologies and libraries:
- Python. Huge thanks to the Python Software Foundation for continuously developing the versatile programming language that served as this system's backend language.
- Pandas. I would like to thank Wes McKinney for creating an invaluable tool used for this system's data wrangling and analysis processes.
- Plotly, Dash. Thanks to Plotly for providing maintenance and improvements to the Python-based graphing library and data science micro-web framework that enabled the efficient development of this system.
- PostgreSQL. My sincere thanks to the PostgreSQL Global Development Group for developing the free and open-source relational database management system used as this system's data storage and management system.
- Psycopg2. The Psycopg Team's efforts to provide the community with a reliable PostgreSQL connection adapter are highly appreciated, and their library enabled the system's backend to seamlessly interact with the relational database.
- HTML, CSS. Thank you to the World Wide Web Consortium for providing the web development community with specifications and standards, ensuring that all developed web applications are made with the utmost quality in mind.