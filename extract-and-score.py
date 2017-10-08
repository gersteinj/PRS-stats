import pandas as pd
from bs4 import BeautifulSoup

race_points = {1:50, 2:40, 3:36, 4:32, 5:30, 6:28, 7:26, 8:24, 9:22, 10:20, 11:18, 12:16, 13:14, 14:12, 15:10, 16:8, 17:6, 18:4, 19:2, 20:1}

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


def combine_tables(*args, event_key='unnamed', display=False):
    df = pd.concat(args, axis=1)
    if display:
        print(df)
    df.to_csv(f'{event_key}-race-results.csv')


combine_tables(extract_data('sample-data.html', 'a'), extract_data('sample-data.html', 'b'), event_key='isitworkingyet')