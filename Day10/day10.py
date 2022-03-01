from collections import Counter, defaultdict

"""
()
[]
{}
<>

"""

values_left = {'(':')','[':']','<':'>','{':'}'}
values_right = {')':'(',']':'[','>':'<','}':'{'}



left = ['(', '[', '<', '{']
right = [')', ']', '>', '}']

total = 0

points = {'(': 1, '[': 2, '{': 3, '<': 4}
scores = []

valid_lines = []

lines = [x.strip() for x in open('day10.txt').readlines()]
# print(lines)
score = 0
for line in lines:
    encountered = []
    navs = line.split()
    # print(navs)
    good = True
    for nav in navs:
        for n in nav:
            print(n)
            if n in left:
                encountered.append(n)
            else:
                if encountered[-1] != values_right[n]:
                        print("Expected {}, got {} instead".format(values_left[encountered[-1]],n))
                        match n:
                            case ')':
                                total += 3
                            case ']':
                                total += 57
                            case '}':
                                total += 1197
                            case '>':
                                total += 25137
                        good = False
                        break
                        
                else:
                    encountered = encountered[:-1]
        # print(encountered)
        if good:
            valid_lines.append(nav)

scores = []
for valid in valid_lines:
    score = 0
    encountered = []
    rows = valid.split()
    # print(navs)
    for row in rows:
        for r in row:
            print(r)
            if r in left:
                encountered.append(r)
            else:
                # if encountered[-1] != values_right[r]:
                #         print("Expected {}, got {} instead".format(values_left[encountered[-1]],r))
                #         # break
                        
                # else:
                    encountered = encountered[:-1]
        print(encountered)

        for i, value in enumerate(encountered[::-1]):
            score = score * 5
            score += points[value]
            # print(score)
        scores.append(score)
                

# print(valid)
# print(total)
z = sorted(scores)
print(z)
print(z[len(z) // 2])
# print(sorted(scores[23]))

# guessed : 4832654334
# guessed : 10832523682
# guessed : 3299349968
# correct is: 3260812321



        
    
    