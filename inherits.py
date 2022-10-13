from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/inherits')
def inherits():
    return render_template('inheritone.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=5001, debug=True)
