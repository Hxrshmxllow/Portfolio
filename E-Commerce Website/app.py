from flask import Flask, render_template, request
from Inventory import getItems
from jinja2 import Template
from product import Product

app = Flask(__name__, template_folder='templates', static_folder='static')

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
        item = [len(cart) + 1, product, price]
        cart.append(item)
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
        index = int(item)-1
        quantity = request.form['quantity']
        if quantity == 0:
            cart.pop(index)
        currentproduct = cart[index][1]
        currentproduct.setQuantity(quantity)
        cart[index][1] = currentproduct
        cart[index][2] = (float(currentproduct.getPrice()) * float(currentproduct.getQuantity()))
    subtotal = 0.00
    for item in cart:
        product = item[1]
        subtotal += float(item[2])
    shipping = round(subtotal * 0.1, 2)
    total = round((subtotal * 1.06825) + shipping, 2)
    return render_template('cart.html', cart=cart, shipping = shipping, subtotal = subtotal, total = total)

@app.route("/category/<category>", methods = ['GET', 'POST'])
def display(category):
    prodArray = []
    items = getItems('E-Commerce Website/Inventory.xlsx', 'Men')
    for item in items:
        colors = item[5].split(',')
        color = colors[0]
        prodOj = Product(item[0], item[1], item[2], item[3], str(item[0]) + "/" + color + "/1.png", item[4], "", 10, color, colors)
        prodArray.append(prodOj)
    return render_template('category.html', products = prodArray)


if __name__ == "__main__":
    app.run('localhost', 8080) 
