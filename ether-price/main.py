# https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130428&end=20180716
from datetime import datetime
import time

data = []
with open('price.txt') as f:
    data = f.readlines()


print(data[:5])
header = data[0].split('\t')
header = [i.strip() for i in header]
print('header', header, len(header))


rows = data[1:]

parsed_rows = []
for row in rows:
    row = row.split('\t')
    row = [col.strip() for col in row]
    dt = datetime.strptime(row[0], '%b %d, %Y')

    row[0] = time.mktime(dt.timetuple())
    row[1] = float(row[1].replace(',',''))
    row[2] = float(row[2].replace(',',''))
    row[3] = float(row[3].replace(',',''))
    row[4] = float(row[4].replace(',',''))
    row[5] = int(row[5].replace(',',''))
    try:
        row[6] = int(row[6].replace(',',''))
    except Exception as e:
        row[6] = 0
    parsed_rows.append(row)


for row in parsed_rows[:5]:
    print(row)

with open('etherprice.csv','wb') as file:
    for row in parsed_rows:
        file.write(','.join(map(lambda x: str(x), row)))
        file.write('\n')
