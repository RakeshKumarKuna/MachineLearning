list1=[2,4,5,9,6,8]
print(list1,type(list1),id(list1))
list1.append(48)
print(list1,type(list1),id(list1))

tuple1=(2,4,5,9,6,8)
print(tuple1,type(tuple1),id(tuple1))
tuple1=(45)
print(tuple1,type(tuple1),id(tuple1))
r=range(10)
for i in r:
    print(i)