data=lambda a,b:f"here the addition of {a}+{b}={a+b}"
print(data(5,5))

def findlarge(a,b):
    return f"big number is a = {a}" if(a>b) else f"b is bigger b = {b}"

#print(findlarge(5000,300))
findlarge(float(input("enter first num")),float(input("enter second num")))