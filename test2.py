exec(open('util.py').read())
#exec(open('test.py').read())

import pandas as pd

# Define the data

data = load_data(["earn_500_final.xls"])

"""
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]
"""
html_table_from_array(["0sorted.html",data])
