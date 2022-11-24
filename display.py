from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import sqlite3
conn = sqlite3.connect('test_database.db', check_same_thread=False)
cursor = conn.cursor()

#endpoint for search
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

@app.route('/newin/')
def newin():
    return render_template('newin.html')


if __name__ == ("__main__"):    app.run(host='0.0.0.0', port=5001, debug=True)