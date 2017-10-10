import pandas as pd

quantity_string = """How many races are you processing?
"""
file_string = """Please enter the name of your next .csv file, WITHOUT the extension.
"""

def combine_tables(list_of_tables):
    combined_tables = pd.DataFrame()
    for table in list_of_tables:
        combined_tables = pd.concat([combined_tables, pd.DataFrame.from_csv(table)], axis=1)
    return combined_tables

race_count = int(input(quantity_string))

races = [f"{input(file_string)}.csv" for n in range(race_count)]

race_results = combine_tables(races)

race_results['total'] = race_results.filter(regex='^points').sum(axis=1)

print(race_results)

race_results.to_csv('combinedoutput.csv')