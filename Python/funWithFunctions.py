def odd_even():
    for item in range(1,2001):
        if item % 2 != 0:
            print "Number is ", item, ". This is an odd number."
        else:
            print "Number is ", item, ". This is an even number."
print odd_even()

def multiply(arr, num):
    for item in range(len(arr)):
        arr[item] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

def layered_multiples(arr):
    print arr
    newArr = []
    for item in arr:
        val_arr = []
        for x in range(0,item):
            val_arr.append(1)
        newArr.append(val_arr)
    return newArr

y = layered_multiples(multiply([2,4,5],3))
print y

