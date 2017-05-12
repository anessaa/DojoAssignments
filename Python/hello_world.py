print("hello world!")
x = "Hello Python"
print(x)
y = 42
print(y)

def say_hello(name):
    if name:
        print("Hello, " + name + " from inside the function")
    else:
        print("No name")
say_hello("anessa")
name = "Zen"
print("My name is", name)
print("my name is " + name)
print ("my name is", 7)

first_name = "Zen"
last_name = "Coder"
print("My name is {} {}".format(first_name, last_name))

hw = "hello %s" % 'world'
print(hw)
