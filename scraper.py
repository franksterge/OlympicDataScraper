import requests as r
import csv
from bs4 import BeautifulSoup as bs

domain = "http://www.espn.com/olympics/summer08/medals"
quotes = r.get(domain)

page_scrape = bs(quotes.content, "html.parser")
data = page_scrape.find_all('tr')
table_head = data[1]
csv_head = []
for table_head_attribute in table_head.children:
  attribute_name = table_head_attribute.string
  if attribute_name != '\n':
    csv_head.append(attribute_name)

# print(data[2])
csv_data_whole = []
for table_attribute_index in range(2, len(data)):
  csv_data = {}
  table_attributes = data[table_attribute_index]
  i = 0
  for table_attribute in table_attributes.children:
    table_data = table_attribute.string
    if table_data is not None and table_data != '\n':
      csv_data[csv_head[i]] = table_data
      i += 1
  csv_data_whole.append(csv_data)

with open('olympic_data_2008.csv', mode='w') as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=csv_head)

  writer.writeheader()
  for item in csv_data_whole:
    writer.writerow(item)
