from flask import Flask, render_template
app = Flask(__name__)

@app.route("/template.html")
def inherits():
    return render_template("template.html")

@app.route("/extensions1.html")
def extensions_1():
    return render_template("template.html")

    if __name__ == ("__main__"):
        app.run(host='0.0.0.0', debug=True)
