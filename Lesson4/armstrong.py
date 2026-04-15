num = int(input("enter the number "))
temp = num
sum = 0
while temp >0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("armstrong number")
else:
    print("not an armstrong number")
