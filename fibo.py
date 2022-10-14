def fibo(n):
    if(n <= 1):
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

number = 10

if(number <= 0):
    print("enter positive number")
else:
    for i in range(number):
        print(fibo(i))
