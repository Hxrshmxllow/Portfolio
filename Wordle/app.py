from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config["TEMPLATES_AUTO_RELOAD"] = True

cells=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", letters=letters, cells = cells)

@app.route("/", methods=['POST'])
def addLetter():
    key = request.get_json()
    print(key)
    i = 0
    j = 0
    for row in cells:
        j = 0
        for cell in row:
            if cell == "":
                cells[i][j] = key
                key = ""
                break
            j += 1
        i += 1
    print(cells)
    render_template("index.html", letters = letters, cells = cells)
    return jsonify(render_template("index.html", letters = letters, cells = cells))

    

if __name__ == "__main__":
    app.run('localhost', 8080)