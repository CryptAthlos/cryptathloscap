import psycopg2
from coinmarketcap import Market
from rest_framework.utils import json

import csv

fieldnames = []
crypto = json.dumps(Market().ticker(start=0, limit=1000))
crypto = json.loads(crypto)
header = crypto[0].keys()

for headers in header:
    if headers == 'id':
        headers = 'name_id'
        fieldnames.append(headers)
    elif headers == 'price_usd':
        headers = 'prices_usd'
        fieldnames.append(headers)
    elif headers == 'price_btc':
        headers = 'prices_btc'
        fieldnames.append(headers)
    elif headers == '24h_volume_usd':
        headers = 'volume_usd_24h'
        fieldnames.append(headers)
    elif headers == 'market_cap_usd':
        headers = 'market_usd_cap'
        fieldnames.append(headers)
    else:
        fieldnames.append(headers)

with open('mainIN.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for row in crypto:
        writer.writerow(row)

with open('mainIN.csv', 'r') as inFile, open('mainOUT.csv', 'w') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)

    next(r, None)  # skip the first row from the reader, the old header

    # copy the rest
    for row in r:
        w.writerow(row)

crypto = open('mainOUT.csv')

conn = psycopg2.connect(host='127.0.0.1', dbname='cryptos', user='crypto', password='0lympu$24$jmfISU')
cur = conn.cursor()

cur.execute(
            """
            CREATE TABLE IF NOT EXISTS main (
                id SERIAL PRIMARY KEY, 
                name_id varchar, 
                name varchar, 
                symbol varchar, 
                rank integer,
                prices_usd decimal,
                prices_btc decimal, 
                volume_usd_24h decimal, 
                market_usd_cap decimal,
                available_supply varchar, 
                total_supply varchar, 
                max_supply varchar,
                percent_change_1h varchar, 
                percent_change_24h varchar, 
                percent_change_7d varchar,
                last_updated varchar, 
                cached varchar,
                created_at time, 
                updated_at time
                )
            """
        )
conn.commit()

cur.copy_from(crypto, 'main', columns=fieldnames, sep=",")

conn.commit()
conn.close()

print("*** COMMIT CSV ***")
