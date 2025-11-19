a,b=15,20
def inputs():
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    return a,b

def addition():
    x,y=inputs()
    return x+y
def sub():
    x,y=inputs()
    return x-y
def locavar():
    a,b=500,600
    glaa=globals()['a']
    glab=globals()['b']
    print(a,b)
    print(glaa,glab)
#def mofifyglobal():



print(addition())
print(sub())
locavar()
print(f"gloal variables before modification {a},{b}")
def incrementglobal():
    global a,b
    a=a+10
    b=b+10
incrementglobal()
print(f"gloal variables after modification {a},{b}")
