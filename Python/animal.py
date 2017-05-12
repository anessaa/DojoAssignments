class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.name + str(self.health)
        return self


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print self.name + str(self.health)
        print "this is a dragon"
        
class Mermaid(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)
    def swim(self):
        self.health -= 5
        return self

one = Animal("ness" + " ")
print one.walk().walk().walk().run().run()

pup = Dog("Ruff" + " ")
print pup.walk().walk().walk().run().run().pet().displayHealth()

beast = Dragon("Prince" + " ")
print beast.walk().walk().walk().run().run().fly().fly().displayHealth()

fish = Mermaid("Aerial" + " ")
print fish.swim().swim().displayHealth()


