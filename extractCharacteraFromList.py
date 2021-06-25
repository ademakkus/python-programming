number = int(input("Enter a number :"))
result = 1
if number == 0:
    print(1)
else:
    while number >= 1:
        result = result * number
        number = number - 1
print(str(result))
