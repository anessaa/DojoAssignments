class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        print self.status
        return self

    def tax(self, salestax):
        print salestax * self.price + self.price
        return self

    def returnProduct(self, reason):
        if (reason == "defective"):
            self.status = "defective"
            self.price = 0
            print self.status
            print self.price
        elif (reason == "returned in box"):
            self.status = "for sale"
            print self.status
        elif(reason == "box open"):
            self.status = "used"
            self.discount = "20% discount"
            print self.status
            print self.discount
        return self
    def displayInfo(self):
        return str(self.price) + " " + self.item_name + " " + str(self.weight) + " " + self.brand + " " + str(self.cost) + " " + self.status
        return self

one = Product(20000, "tiguan", 10000, "VW", 2000, "new")

print one.returnProduct("returned in box").displayInfo()
