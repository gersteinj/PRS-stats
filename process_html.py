from bs4 import BeautifulSoup
import pandas as pd

input_file_string = """Please enter the name of the html file you want to process, WITHOUT the extension.
"""

output_file_string = """Please enter a name for the CSV file output, WITHOUT the extension.
The name of the file will also be used in the column names - please make it unique within a given race weekend.
"""

input_file = input(input_file_string)
output_file = input(output_file_string)
race_points = {
    1:75,
    2:64,
    3:54,
    4:45,
    5:37,
    6:30,
    7:24,
    8:19,
    9:15,
    10:12,
    11:10,
    12:18,
    13:6,
    14:4,
    15:2,
    16:1,
    17:0,
    18:0,
    19:0,
    20:0,
    21:0,
    22:0,
    23:0,
    24:0,
    25:0,
    26:0,
    27:0,
    28:0,
    29:0,
    30:0,
    31:0,
    32:0,
    33:0,
    34:0,
    35:0,
    36:0,
    37:0,
    38:0,
    39:0,
    40:0,
    41:0,
    42:0,
    43:0,
    44:0,
    45:0,
    46:0,
    47:0,
    48:0,
    49:0,
    50:0,
    }

with open(f'{input_file}.html', 'r') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')

# grab each table
results = soup.find_all('table')[1]

# only working with results for now
# lap_times = soup.find_all('table')[2]

# Make new soup for just the race results
result_soup = BeautifulSoup(str(results), 'html.parser')

header = [item.string for item in results.find_all('tr')[0] if item.string != '\n']
rows = [[item.string for item in row if item.string != '\n'] for row in results.find_all('tr')]

df = pd.DataFrame({f'position-{output_file}': [row[0] for row in rows[1:]], f'points-{output_file}': [race_points[int(row[0])] for row in rows[1:]]}, index=[row[6] for row in rows[1:]])

filename = f"{output_file}.csv"
df.to_csv(filename) 