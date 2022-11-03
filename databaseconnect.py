import sqlite3
conn = sqlite3.connect('test_database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS products
([product_id] INTERGER PRIMARY KEY, [product_name] TEXT)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS prices
([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
''')

conn.commit()


