myfile=open("input.txt","r")
content=myfile.read()

uniquewords=content.split()
print(len(uniquewords))
print(uniquewords)

for word in uniquewords:
    print(word,":",uniquewords.count(word),",")