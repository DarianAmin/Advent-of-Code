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
        for moreindex in range(1,len(data1)+1):
            calc=data1[index-1]+data1[indexes-1]+data1[moreindex-1]
            if int(calc)==2020:
                values.append(data1[index-1])
                values = list(dict.fromkeys(values))
                add=calc

print(values[0]*values[1]*values[2])
print(values)
            


    



