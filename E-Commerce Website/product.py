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
    
    def getQuantity(self):
        return self.Qty
    
    def setQuantity(self, quantity):
        self.Qty = quantity