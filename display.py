from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

import sqlite3
conn = sqlite3.connect('test_database.db', check_same_thread=False)
cursor = conn.cursor()

app.secret_key = 'supersecretpassword'

#search functionality for home page(index.html)
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        album = request.form['album']
        # search by artist or album
        cursor.execute("SELECT artist, album, year, genre from products WHERE artist LIKE ? OR album LIKE ? OR genre LIKE ? OR year LIKE ? ", (album,album,album,album))
        conn.commit()
        data = cursor.fetchall()
        print (data)
        
        return render_template('index.html', data=data)
    return render_template('index.html')

@app.route('/newin', methods=['GET', 'POST'])
def newin():
    return render_template('newin.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM accounts WHERE username LIKE ? AND password LIKE ?', (username, password,))
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            msg = 'Logged in successfully !'
            return render_template('login.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

def loginextend():
    return render_template('login.html')


if __name__ == ("__main__"):    app.run(host='0.0.0.0', port=5001, debug=True)