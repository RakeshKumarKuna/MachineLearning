'''
In python we have special function filter,map,reduce
'''
# 1.filter function examples
def getpositiveNumbers(num):
    if(num>=0):
        return True
    else:
        return False
        
lst=[45,87,-98,78,15,-78,-59,-102,156,856,-1254]
positivedata=filter(getpositiveNumbers,lst)
print(list(positivedata))



#now we get only negative numbers with lambda functions
print("======================================")
lambdaresult=lambda a:True if(a<0) else False
negativedata=filter(lambdaresult,lst)
print(list(negativedata))
str(45)
bool


#filting the data based the values are even or not
print("=================================")
even=filter(lambda a:True if(a%2==0) and (a>0) else False,lst)
print("even numbers from list: ",list(even))

# print even number from selected range
print("="*50)
def getevennumber(n):
    return filter(lambda a:a%2==0,range(0,n))
print(list(getevennumber(20)))



class Test:
    def __init__(self):
        self.data=[45,78,96,12,47,89,24,68,15,47,26,38,49,59]
    
    def geteven(self):
        evennumbers=filter(lambda a:a%2==0,self.data)
        return list(evennumbers)