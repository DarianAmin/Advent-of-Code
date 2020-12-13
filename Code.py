answers=[]

values=[]
data1=[]
file=open("data.txt","r")
record=file.readlines()

for lines in record:
    remover=lines.strip("\n")
    data1.append(int(remover))


for index in range(1,len(data1)+1):
    for indexes in range(1,len(data1)+1):
        calc=data1[index-1]+data1[indexes-1]
        if int(calc)==2020:
            values.append(data1[index-1])
            add=calc

print(values[0]*values[1])
print(values)
            


    



