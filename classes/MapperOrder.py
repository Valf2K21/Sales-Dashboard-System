# set mapping dictionaries and order lists prior to column generation
# mapping dictionary of modelnames for modelseries column generation
MODELNAME_MAPPER = {
    'CYH': ['CYH52SRA', 'CYH52W W/OUT PTO'],
    'CYZ': ['CYZ52QVC45 W/ TRANSMISSION SIDE PTO', 'CYZ52T TSPTO'],
    'D-MAX': ['D-MAX 3.0 4X2 LS-A AT (RG01)', 'D-MAX 3.0 4X2 LS-A AT (RG10)', 'D-MAX 3.0 4X2 LS-A MT (RG10)', 'D-MAX 3.0 4X4 LS MT (RG01)', 'D-MAX 3.0 4X4 LS-A MT (RG10)', 'D-MAX 3.0 4X4 LS-A MT (RT66)', 'D-MAX 3.0 4X4 LS-E AT (RG01)', 'D-MAX 3.0 4X4 LS-E AT (RG10)', 'D-MAX 3.0 4X4 LT MT (RG01)', 'D-MAX 3.0 4X4 LT MT (RG10)', 'D-MAX 3.0 4X4 SINGLE-CAB MT (RG10)', 'D-MAX RZ4E 4X2 LS AT (RG01)', 'D-MAX RZ4E 4X2 LS MT (RG01)', 'D-MAX RZ4E 4X2 LS MT (RG10)', 'D-MAX RZ4E 4X2 LT MT (RG10)', 'D-MAX RZ4E 4X2 SINGLE-CAB MT (RG10)'],
    'EXR': ['EXR52FVC45 W/ PTO', ],
    'EXZ': ['EXZ52K TSPTO (KING PIN 3.5 INCHES)', 'EXZ52KVC45 W/ PTO'],
    'FRR': ['FRR90M'],
    'FTR': ['FTR90M', ],
    'FTS': ['FTS34J C/C W/ PTO & AIRCON'],
    'FVM': ['FVM34T', 'FVM34W'],
    'FVR': ['FVR34'],
    'FVZ': ['FVZ34T W/ PTO & AIRCON'],
    'MU-X': ['MU-X 3.0 4X2 LS-A AT (RJ01)', 'MU-X 3.0 4X2 LS-A AT (RJ05)', 'MU-X 3.0 4X2 LS-E AT (RJ01)', 'MU-X 3.0 4X2 LS-E AT (RJ05)', 'MU-X 3.0 4X4 LS-E AT (RJ01)', 'MU-X 3.0 4X4 LS-E AT (RJ05)', 'MU-X RZ4E 4X2 LS AT (RJ01)', 'MU-X RZ4E 4X2 LS AT (RJ05)', 'MU-X RZ4E 4X2 LS-A MT (RJ01)'],
    'NLR': ['NLR77 H LWB TILT', 'NLR77 H TILT', 'NLR85 E', 'NLR85ES'],
    'NMR': ['NMR85 H', 'NMR85 H TILT'],
    'NPR': ['NPR85', 'NPR85 K', 'NPR85H CREW-CAB W/ABS', 'NPR85H CREW-CAB W/ABS & PTO'],
    'NPS': ['NPS75', 'NPS75H CREW-CAB'],
    'NQR': ['NQR75', 'NQR75 L'],
    'QKR': ['QKR77 NON-TILT 80A', 'QKR77 NON-TILT JB', 'QKR77 TILT 60A'],
    'QLR': ['QLR77 E TILT'],
    'TRAVIZ': ['TRAVIZ L', 'TRAVIZ S']
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