import difflib


# signals = [x.split('|') for x in open("day8.txt").readlines()]
# counts = 0
# for s in signals:
#     segments = s[1].split(' ')
#     # print(segments)
#     for seg in segments:
#         seg = seg.strip()
#         if len(seg) == 2 or len(seg) == 3 or len(seg) == 4 or len(seg) == 7:
#             counts += 1

# print(counts)
#idea borrowed from 4HbQ on reddit


s = 0
for x,y in [x.split('|') for x in open(0)]:  # split signal and output
  l = {len(s): set(s) for s in x.split()}    # get number of segments

  n = ''
  for o in map(set, y.split()):              # loop over output digits
    match len(o), len(o&l[4]), len(o&l[2]):  # mask with known digits
      case 2,_,_: n += '1'
      case 3,_,_: n += '7'
      case 4,_,_: n += '4'
      case 7,_,_: n += '8'
      case 5,2,_: n += '2'
      case 5,3,1: n += '5'
      case 5,3,2: n += '3'
      case 6,4,_: n += '9'
      case 6,3,1: n += '6'
      case 6,3,2: n += '0'
  s += int(n)

print(s)

"""
explained :

0: abcefg
1: cf
2: acdeg
3: acdfg
4: bcdf
5: abdfg
6: abdefg
7: acf
8: abcdefg
9: abcdfg

len(0) = 6       
len(1) = 2
len(2) = 5
len(3) = 5
len(4) = 4
len(5) = 5
len(6) = 6
len(7) = 3
len(8) = 7
len(9) = 6

If a wire has a length of 6 segments and when compared to segment(4) which has a length of 4
the resulting segment is of length 4 has a length of 3, and when compared to segment(1) which has a length of two
it has a length of two - then we know that segment is '0'.

segment(1) and segment(4) can be used to determine all other segments


"""

