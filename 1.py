 # Create a module named calculator.py with a function add(a, b) that returns the addition of two numbers. Import this module into another Python file and use the add() function.


import calculator
a = int(input("enter no a is "))
b = int(input("enter no b is "))

result = calculator.add(a,b)
print ("result",result)