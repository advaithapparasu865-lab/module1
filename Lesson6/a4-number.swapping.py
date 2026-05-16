print("Number Swapping Program")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# Swap numbers into ascending order
if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

print()
print("Numbers in ascending order:")
print("x =", x)
print("y =", y)
print("z =", z)