#Find and Replace
# In this string: str = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". 
# Then create a new string where the word "day" is replaced with the word "month".

str = "It's thanksgiving day. It's my birthday,too!"
for count in str:
    print str.find("day")
    print str.replace("day", " month")
    break

#Min and Max
#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
# Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[len(x)-1]
y = [x[0],x[len(x)-1]]
print y 

#New List
#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
#Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. 
#The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
print x
x1 = x[0:len(x)/2]
x2 = x[len(x)/2:len(x)]
print x1
print x2
x2.insert(0,x1)
print x2