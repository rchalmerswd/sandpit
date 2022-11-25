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
def search():
    if request.method == "POST":
        album = request.form['album']
        # search by artist or album
        cursor.execute("SELECT artist, album, year, genre from products WHERE artist LIKE ? OR album LIKE ? OR genre LIKE ? OR year LIKE ? ", (album,album,album,album))
        conn.commit()
        data = cursor.fetchall()
        print (data)
        return redirect ('/newin', data=data)
    return render_template('newin.html')

@app.route('/login', methods=['GET', 'POST'])
def loginextend():
    return render_template('login.html')
def login():
        # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
                # Check if account exists using MySQL
        cursor.execute('SELECT * FROM accounts WHERE username LIKE ? AND password LIKE ?', (username, password))
        conn.commit()
        # Fetch one record and return result
        account = cursor.fetchone()
        print (account)
                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    #Output Message if something goes wrong..
    msg = 'that didnt work'
    return render_template('index.html', msg='')

if __name__ == ("__main__"):    app.run(host='0.0.0.0', port=5001, debug=True)