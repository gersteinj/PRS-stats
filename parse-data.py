from bs4 import BeautifulSoup
html_doc = open('sample-data.html', 'r')

# create HTML soup
soup = BeautifulSoup(html_doc, 'html.parser')

# grab each table
results = soup.find_all('table')[1]
lap_times = soup.find_all('table')[2]


