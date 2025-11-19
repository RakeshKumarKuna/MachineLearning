def readingFile():
    file=open("D:/AI/Python/resources/textfile.txt",mode="r")
    print(file.readlines())

# doing operations with file using with open
def readingFilewithopen():
    with open("D:/AI/Python/resources/textfile.txt",mode="r+") as file:
        data=file.readlines()
        print(data)
        print("="*45)
        file.write("currently i am learning python")
        print(file.readlines())

#readingFile()
#readingFilewithopen()
# writingFile():
def writingFile():
    with open("D:/AI/Python/resources/textfile.txt",mode="r+") as file:
        file.write("\n this is new line added")
        data=file.readlines()
        print(data)

#writingFile()

#pic random pet name

def picRandonPerName():
    import random
    with open("D:/AI/Python/resources/pets.txt",mode="r") as file:
        data=file.read()
        print(type(data))
        data=data.split("\n")
        print(data)
        print(type(data))
        print("Random Per Name:", random.choice(data))

picRandonPerName()