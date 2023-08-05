from flask import Flask, render_template, request
from Inventory import getItems
from jinja2 import Template

app = Flask(__name__, template_folder='templates', static_folder='static')

class Product():          # leave this empty
    def __init__(self, id, brand, name, price, imageFile, desc, size, qty, color, colors):   # constructor function using self
        self.Id = id  # variable using self.
        self.Brand = brand  # variable using self
        self.Name = name  # variable using self
        self.Price = price  # variable using self
        self.ImageFile = imageFile  # variable using self
        self.Description = desc  # variable using self
        self.Size = size  # variable using self
        self.Qty = qty 
        self.Color = color # variable using self
        self.Colors = colors
    
    def getPrice(self):
        return self.Price

cart=[]


@app.route("/")
def index():
    prodArray = []
    items = getItems('E-Commerce Website/Inventory.xlsx', 'Men')
    for item in items:
        colors = item[5].split(',')
        color = colors[0]
        prodOj = Product(item[0], item[1], item[2], item[3], str(item[0]) + "/" + color + "/1.png", item[4], "", 10, color, colors)
        prodArray.append(prodOj)

    return render_template('index.html', products=prodArray)

@app.route("/search", methods = ['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route("/product/<Id>", methods = ['GET', 'POST'])
def product(Id):
    if request.method ==  "POST":
        color = request.form['color']
        size = request.form['size']
        id = request.form['id']
        name = request.form['name']
        brand = request.form['brand']
        des = request.form['des']
        price = request.form['price']
        price = price.replace("$", "")
        product = Product(id, brand, name, price, id + "/" + color, des, size, 1, color, ["", ""])
        cart.append(product)
    Color = ""
    product = Product(0, "", "", 0, "", "", "S", 0, "", ["", ""])
    items = getItems('E-Commerce Website/Inventory.xlsx', 'Men')
    for item in items:
        if Id in str(item[0]):
            colors = item[5].split(',')
            if Color == "":
                Color = colors[0]
            product = Product(item[0], item[1], item[2], item[3], str(item[0]) + "/" + Color + "", item[4], 4, 10, Color, colors)
    return render_template('product.html', product=product)

@app.route("/cart", methods = ['GET', 'POST'])
def checkout():
    if request.method == "POST":
        item = request.form['item']
        cart.remove(int(item))
    subtotal = 0.00
    for product in cart:
        subtotal += float(product.getPrice())
    shipping = round(subtotal * 0.1, 2)
    total = round((subtotal * 1.06825) + shipping, 2)
    return render_template('cart.html', cart=cart, shipping = shipping, subtotal = subtotal, total = total)

if __name__ == "__main__":
    app.run('localhost', 8080) 
