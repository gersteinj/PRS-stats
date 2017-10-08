import pandas as pd

def combine_tables(*args):
    global combined_tables
    combined_tables = pd.DataFrame()
    for table in args:
        combined_tables = pd.concat([combined_tables, pd.DataFrame.from_csv(table)], axis=1)

combine_tables('race1.csv', 'race2.csv', 'race3.csv')

combined_tables['total'] = combined_tables.filter(regex='^points').sum(axis=1)

print(combined_tables)

combined_tables.to_csv('combinedoutput.csv')