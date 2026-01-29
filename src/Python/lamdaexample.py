def lamdaexamples(x,y):
    data=lambda a,b:a+b
    print(data(x,y))
lamdaexamples(20,30)


big=lambda x,y,z:x if(x>y) and (x>z) else y if(y>x) and (y>z) else z
print(big(100,122,347))