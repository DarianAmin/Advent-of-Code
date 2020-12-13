file=open("data.txt")
record=file.readlines()

answers=[]
for lines in record:
    rule,password=lines.split(":")
    minchar,value2=rule.split("-")
    maxchar,char=value2.split()
    strippass=password.strip("\n").strip()

    count=strippass.count(char)
    if int(count)>=int(minchar) and int(count)<=int(maxchar):
        answers.append(count)


print(len(answers))



