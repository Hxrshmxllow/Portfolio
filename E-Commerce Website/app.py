from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

class Product():          # leave this empty
    def __init__(self, id, name, price, imageFile, desc, sizes, qty):   # constructor function using self
        self.Id = id  # variable using self.
        self.Name = name  # variable using self
        self.Price = price  # variable using self
        self.ImageFile = imageFile  # variable using self
        self.Description = desc  # variable using self
        self.Sizes = sizes  # variable using self
        self.StockQty = qty  # variable using self

@app.route("/")
def index():
    prodArray = []

    for x in range(8):
        prodOj = Product(x+1, "Product "+str(x+1), x + 10, "card" +str(x+1) +".png", "Product Desc", 10, 15)
        prodArray.append(prodOj)

    return render_template('index.html', products=prodArray)

@app.route("/search", methods = ['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route("/product", methods = ['GET', 'POST'])
def product():
    return render_template('product.html')

if __name__ == "__main__":
    app.run('localhost', 8080) 
