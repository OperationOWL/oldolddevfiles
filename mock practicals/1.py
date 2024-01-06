file = "text.txt"
f = open(file, 'r')
rec = []

for i in f:
    if i[-1]=='\n':
        for j in i[0:-1].split():
            rec.append(j)
    else:
        for j in i.split():
            rec.append(j)

print(rec)