li = [124, 112, 59, 73, 167, 100, 105, 75, 59, 23, 16, 181, 165, 104, 43, 49, 118, 71, 112, 169, 43, 53]

pie = 1
for k in range(100):
    for i,j in enumerate(li, 0):
        li[i] ^= pie
        pie = ((pie ^ 0xff) + (i * 10) & 0xff)

for i in li:
    print(chr(i), end="")