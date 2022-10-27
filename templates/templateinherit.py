from flask import Flask, render_template
app = Flask(__name__)

@app.route("/inherits.html")
def inherits():
    return render_template("base.html")

@app.route("/extensions1")
def extensions_1():
    return render_template("template.html")

    if __name__ == ("__main__"):
        app.run(host='0.0.0.0', debug=True)
