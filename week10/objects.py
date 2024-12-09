# Object module that has Product class
class Product: 
    def __init__(self, name, price, discountPercent): # 3 parameters
        self.name = name # attribute 1 
        self.price = price # attribute 2
        self.discountPercent = discountPercent # attribute 3

    def getDiscountAmount(self): # method of Product class that returns discount amount 
        return self.price * self.discountPercent / 100
    
    def getDiscountedPrice(self): # method of Product class that returns discounted price
        return self.price - self.getDiscountAmount()