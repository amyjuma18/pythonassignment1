def compare_numbers(x , y):
    if type(x) == int and type(y) == int:
       if x == y:
          return "x and y are equal"
       elif x>y:
          return "x is greater than y"
       else:
          return "x is greater than y"
    else:
     return "invalid input"

x = int(input(" Enter number x: "))
y = int(input(" Enter number y: "))
print(compare_numbers(a,b))


