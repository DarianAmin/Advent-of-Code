file=open("data.txt")
record=file.readlines()

answers=[]
for lines in record:
    rule,password=lines.split(":")
    minchar,value2=rule.split("-")
    maxchar,char=value2.split()
    strippass=password.strip("\n").strip()

    count=strippass.count(char)
    if strippass[int(minchar)-1]==char and strippass[int(maxchar)-1]==char:
        pass
    elif strippass[int(minchar)-1]==char or strippass[int(maxchar)-1]==char:
        answers.append(count)


print(len(answers))



