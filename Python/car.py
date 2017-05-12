class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (price > 10000):
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self):
        print "Price: " + (self.price), "Speed:", self.speed, "mph" + " Fuel: " + self.fuel + " Mileage:", self.mileage, "mph" + " Tax:", self.tax
        return self


one = Car("$2,000", 35, "Full", 15)
two = Car("$2,000", 5, "Not Full", 105)
three = Car("$2,000", 15, "Kind of Full", 95)
four = Car("$2,000", 25, "Full", 25)
five = Car("$2,000", 45, "Empty", 25)
six = Car("$20,000,000", 35, "Empty", 15)

one.display_all()
two.display_all()
three.display_all()
four.display_all()
five.display_all()
six.display_all()