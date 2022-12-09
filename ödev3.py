f = open("data.txt" , "r+" , encoding='utf-8')
f.write('''Name: Nisan
Surname: Tekşen
Gender: female
Username: nisanthebestx
Job: makine''')
d = {}
f = open("data.txt" , "r" , encoding='utf-8')
for line in f:
    (key, val) = line.split()
    d[str(key)] = val
print(d)         
f.close()