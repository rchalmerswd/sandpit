import sqlite3
conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products
([product_id] INTERGER PRIMARY KEY, [product_name] TEXT)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS prices
([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
''')

conn.commit()


