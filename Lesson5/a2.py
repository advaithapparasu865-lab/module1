def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return n
    else:
        return n*factorial(n-1)
num = int(input("Enter your number")) 
if num < 0:
    print("you have enetered a negative number")
else:  
    result = factorial(num)
    print("factorial of", num,)