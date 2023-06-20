from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return render_template("layout.html")

@app.route("/addLetter", methods=['POST'])
def addLetter():
    key = request.form['data']
    return render_template("layout.html", R1C1="key")
    

if __name__ == "__main__":
    app.run('localhost', 8080)