from bs4 import BeautifulSoup
import pandas as pd

race_points = {1:50, 2:40, 3:36, 4:32, 5:30, 6:28, 7:26, 8:24, 9:22, 10:20, 11:18, 12:16, 13:14, 14:12, 15:10, 16:8, 17:6, 18:4, 19:2, 20:1}

html_doc = open('sample-data.html', 'r')

# create HTML soup
soup = BeautifulSoup(html_doc, 'html.parser')

# close html doc
html_doc.close()

# grab each table
results = soup.find_all('table')[1]

# only working with results for now
# lap_times = soup.find_all('table')[2]

# Make new soup for just the race results
result_soup = BeautifulSoup(str(results), 'html.parser')

header = [item.string for item in results.find_all('tr')[0] if item.string != '\n']
rows = [[item.string for item in row if item.string != '\n'] for row in results.find_all('tr')]

df = pd.DataFrame(rows[1:], columns=rows[0])

point_values = []
for r in range(len(df)):
    place = int(df.iloc[r]['Position'])
    point_values.append(race_points[place])

df['Points'] = point_values

filename = f"{soup.title.text}.csv"
df.to_csv(filename)