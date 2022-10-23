file1 = open('query.titles.json','w')
queries= open("query.titles.tsv",'r')

a = '{'
b = '\n\t"requested": 1000,'
c = '\n\t"index": "/home/student/robust04-complete-index",'
d = '\n\t"mu": 1000,'
e = '\n\t"scorer" : "dirichlet",'
f = '\n\t"queries": ['
g = '\n\t]'
h = '\n}'

file1.write(a+b+c+d+e+f)
Lines = queries.readlines()
linecount = 0
for line in Lines:
    sentence = line.split()
    formattedSentence = ['\n\t\t{','\n\t\t"number": ']
    count = 0
    for i in sentence:
        if count == 0:
            formattedSentence.append('"' + i + '",')
        elif count == 1:
            formattedSentence.append('\n\t\t"text": "#combine(' + i)
        else:
            formattedSentence.append(' '+ i)
        count += 1
    formattedSentence.append(')"\n\t\t}')
    linecount += 1
    if linecount < len(Lines):
        formattedSentence.append(',')
    file1.write(''.join(formattedSentence))
file1.writelines(g+h)
file1.close()
queries.close()
