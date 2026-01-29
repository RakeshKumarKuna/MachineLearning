def divideNumbers(a,b):
    return a/b
try:
    print(divideNumbers(45,0))
except ZeroDivisionError as e:
    print("something went wrong",e)

print("program end")