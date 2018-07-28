import pandas as pd
from bs4 import BeautifulSoup

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
    16:1
    }

def extract_data(html_file, race_key, export_csv=False):
    """Extract data from HTML export of race software and return Pandas dataframe"""
    with open(html_file, 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
    results = soup.find_all('table')[1]
    result_soup = BeautifulSoup(str(results), 'html.parser')

    header = [item.string for item in results.find_all('tr')[0] if item.string != '\n']
    rows = [[item.string for item in row if item.string != '\n'] for row in results.find_all('tr')]

    if export_csv:
        print("I'll implement this later, sorry")
    
    df = pd.DataFrame({f'position-{race_key}': [row[0] for row in rows[1:]], f'points-{race_key}': [race_points[int(row[0])] for row in rows[1:]]}, index=[row[6] for row in rows[1:]])
    
    return df


def combine_tables(list_of_tables, event_key='unnamed', display=False):
    combined_tables = pd.DataFrame()
    for table in list_of_tables:
        combined_tables = pd.concat([combined_tables, pd.DataFrame.from_csv(table)], axis=1)
    if display:
        print(combined_tables)
    df.to_csv(f'{event_key}-race-results.csv')
    return combined_tables


combine_tables([extract_data('sample-data.html', 'a'), extract_data('sample-data.html', 'b')], event_key='test weekend')