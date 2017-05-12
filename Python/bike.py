class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 "mph"
    def displayInfo(self):
        return str(self.price)+ " "+ str(self.max_speed) + " " + str(self.miles)
        return self
    def ride(self):
        print "Riding " + str(self.miles + 10) +" mph"
        return self
    def reverse(self):
        print "Reversing " + str(self.miles - 5) +" mph"
        return self

user1 = Bike("$1000", "100mph", 20)
print user1.ride().ride().ride().reverse().displayInfo()