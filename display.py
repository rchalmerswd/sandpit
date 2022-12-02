from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
import re
import sqlite3
conn = sqlite3.connect('test_database.db', check_same_thread=False)
cursor = conn.cursor()

app.secret_key = 'supersecretpassword'

#search functionality for home page(index.html)
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        searchbar = request.form['searchbar']
        # search by artist or album
        cursor.execute("SELECT artist, album, year, genre from products WHERE artist LIKE ? OR album LIKE ? OR genre LIKE ? OR year LIKE ? ", (searchbar,searchbar,searchbar,searchbar))
        conn.commit()
        data = cursor.fetchall()
        print (data)
        
        return render_template('index.html', data=data)
    return render_template('index.html')

@app.route('/newin', methods=['GET', 'POST'])
def newin():
    return render_template('newin.html')

def loginextend():
    return render_template('login.html')


# Log in/resgister function inspired by https://codeshack.io/login-system-python-flask-mysql/#authenticatinguserswithpython
@app.route('/login/', methods=['GET', 'POST'])s
def login():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM accounts WHERE username = ? AND password = ?', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


@app.route('/logout/')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor.execute('SELECT * FROM accounts WHERE username = ?', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (?, ?, ?)', (username, password, email))
            conn.commit()
            msg = 'You have successfully registered, now you can log in!'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


@app.route('/home', methods =['GET', 'POST'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html')
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/add', methods =['GET', 'POST'])
def add():
    msg = ''
    if request.method == 'POST':
        artist = request.form['artist']
        album = request.form['album']
        cursor.execute('INSERT INTO collection (artist, album) VALUES (?, ?)', (artist, album))
        conn.commit()
        print (artist, album)
        msg = 'Added To Collection'
    elif request.method == 'GET':
        return render_template('home.html')
    return render_template('home.html', msg = msg)


@app.route('/collection', methods=['GET', 'POST'])
def collection():
        cursor.execute("SELECT * FROM collection")
        conn.commit()
        data = cursor.fetchall()
        print (data)
        return render_template('home.html', data=data)
    


if __name__ == ("__main__"):    app.run(host='0.0.0.0', port=5001, debug=True)