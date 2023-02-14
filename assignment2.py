def calculator(a,b):
    if type(a) == int and type(b) == int:
        sum = a+b
        difference = a-b
        product = a*b
    if b == 0:
        return "division by zero is not allowed"
    else:
        division = a/b
    if a == b:
        return "a and b are equal\nsum: {}\ndifference: {}\ndivision: {}".format(sum, difference, product, division)
    else:
        return "invalid input"

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print(calculator(a,b))