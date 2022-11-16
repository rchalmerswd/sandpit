from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import sqlite3
conn = sqlite3.connect('test_database.db', check_same_thread=False)
cursor = conn.cursor()

#endpoint for search
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        products = request.form['products']
        # search by author or book
        cursor.execute("SELECT * from products WHERE artist LIKE %s OR album LIKE %s", (products, products))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and products == 'all': 
         return render_template('index.html', data=data)
    return render_template('index.html')



@app.route('/inherits/one')
def inherits():
    return render_template('inheritone.html')



if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=5001, debug=True)