def swap(a, b):
    temp = a
    a = b
    b = temp
    print("After Swapping two Number: x = {0} and y = {1}".format(a, b))

x = float(input(" Please Enter the First Value : "))
y = float(input(" Please Enter the Second Value : "))
swap(x, y)

'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Enter a number for factorial : "))
print(factorial(n))'''
