import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('test_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/')
def results():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    print(posts)
    return render_template('results.html', posts=posts)

@app.route('/inherits/one')
def inherits():
    return render_template('inheritone.html')


if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=5001, debug=True)