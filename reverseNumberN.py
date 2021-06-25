x = int(input("Enter first number:"))
y = int(input("Enter first number:"))
while y != 0:
    R = x % y
    x = y;
    y = R
print(x)
