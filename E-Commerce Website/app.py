from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods = ['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route("/product", methods = ['GET', 'POST'])
def product():
    return render_template('product.html')

if __name__ == "__main__":
    app.run('localhost', 8080) 