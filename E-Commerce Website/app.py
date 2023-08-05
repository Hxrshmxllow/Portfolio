from flask import Flask, render_template, request
from Inventory import getItems

app = Flask(__name__, template_folder='templates', static_folder='static')

class Product():          # leave this empty
    def __init__(self, id, brand, name, price, imageFile, desc, sizes, qty, colors):   # constructor function using self
        self.Id = id  # variable using self.
        self.Brand = brand  # variable using self
        self.Name = name  # variable using self
        self.Price = price  # variable using self
        self.ImageFile = imageFile  # variable using self
        self.Description = desc  # variable using self
        self.Sizes = sizes  # variable using self
        self.StockQty = qty  # variable using self
        self.Colors = colors

cart=[]


@app.route("/")
def index():
    prodArray = []
    items = getItems('E-Commerce Website/Inventory.xlsx', 'Men')
    for item in items:
        colors = item[5].split(',')
        color = colors[0]
        prodOj = Product(item[0], item[1], item[2], item[3], str(item[0]) + "/" + color + "/1.png", item[4], 4, 10, colors)
        prodArray.append(prodOj)

    return render_template('index.html', products=prodArray)

@app.route("/search", methods = ['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route("/product/<Id>/<Color>", methods = ['GET', 'POST'])
def product(Id, Color):
    product = Product(0, "", "", 0, "", "", 0, 0, ["", ""])
    items = getItems('E-Commerce Website/Inventory.xlsx', 'Men')
    for item in items:
        if Id in str(item[0]):
            colors = item[5].split(',')
            color = colors[0]
            product = Product(item[0], item[1], item[2], item[3], str(item[0]) + "/" + color + "", item[4], 4, 10, colors)
    return render_template('product.html', product=product)

@app.route("/cart", methods = ['GET', 'POST'])
def checkout():
    return render_template('cart.html')

if __name__ == "__main__":
    app.run('localhost', 8080) 
