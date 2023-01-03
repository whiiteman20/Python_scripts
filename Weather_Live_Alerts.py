import requests
import bs4
import pandas as pd
import sqlite3
import time

conn = sqlite3.connect("Weather_Warning_Table")

c = conn.cursor()

c.execute("""
            CREATE TABLE IF NOT EXISTS Weather_Warning_Table (
                [ID] integer PRIMARY KEY,
                [Warning_Start] TEXT,
                [Warning_End] TEXT,
                [States] TEXT,
                [Phenomena] TEXT,
                [Warning_Counties]
            )
              """)

conn.commit()

while True:
    conn = sqlite3.connect("Weather_Warning_Table")

    c = conn.cursor()

    c.execute("""
                DROP TABLE Weather_Warning_Table
              """)

    conn.commit()

    url = 'https://www.tornadohq.com/live/'

    r = requests.get(url)

    print(r)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())

    warning_table = soup.select('table.table.table-striped')[0]

    #print(warning_table)

    warning_table_df = pd.read_html(str(warning_table))[0]

    #print(warning_table_df)

    data = warning_table_df[['Warning Start', "Warning End", "States", "Phenomena", "Warning Counties"]]

    #print(data)

    data.to_sql("Weather_Warning_Table", conn, if_exists='append', index_label="ID")

    time.sleep(120)

