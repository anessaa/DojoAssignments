#l = ['magical unicorns',19,'hello',98.98,'world']
l = [2,3,1,7,4,12]
#l = ['magical','unicorns']
sum = 0
newString = " "
for item in l:
    if isinstance(item,str):
        newString += item + " "
    if isinstance(item,int) or isinstance(item,float):
        sum += item
    if isinstance(item, int) and isinstance(item, float) and isinstance(item, str):
        print "The array you entered is mixed type."
        break
    if isinstance(item, int):
        print "The array you entered is an integer type."
        break
    if isinstance(item, str):
        print "The array you entered is a string type."
        break
print "Sum:", sum
print "String:", newString