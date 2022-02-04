from collections import Counter

report = [x.strip() for x in open('day3.txt').readlines()]
reports2 = [x.strip() for x in open('day3.txt').readlines()]
reports3 = [x.strip() for x in open('day3.txt').readlines()]
gamma = ""
eps = ""


for x in range(len(report[0])):
    counts = Counter(a[x] for a in report) 
    if counts['0'] > counts['1']:
        gamma += '0'
        eps += '1'
    else:
        gamma += "1"
        eps += "0"


print(gamma, eps)
print(int(gamma, 2) * int(eps, 2))


for x in range(len(reports2[0])):
    counts = Counter(a[x] for a in reports2) 
    
    if counts['0'] > counts['1']:
        reports2 = [i for i in reports2 if i[x] == '0']

    elif counts['0'] < counts['1']:
        reports2 = [i for i in reports2 if i[x] == '1']
    else:
        reports2 = [i for i in reports2 if i[x] == '1']
print(reports2)


for x in range(len(reports3[0])):
    counts = Counter(a[x] for a in reports3) 
    
    if counts['0'] > counts['1']:
        reports3 = [i for i in reports3 if i[x] == '1']
    elif counts['0'] < counts['1']:
        reports3 = [i for i in reports3 if i[x] == '0']
    else:
        reports3 = [i for i in reports3 if i[x] == '0']
    if len(reports3) == 1:
        print(reports3)
        break

print(int(reports2[0], 2) * int(reports3[0], 2))

