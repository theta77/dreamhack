data = """52h, 0DFh, 0B3h, 60h, 0F1h, 8Bh, 1Ch, 0B5h, 57h, 0D1h
.data:0000000140003000                                         ; DATA XREF: sub_140001000+50↑o
.data:000000014000300A                 db 9Fh, 38h, 4Bh, 29h, 0D9h, 26h, 7Fh, 0C9h, 0A3h, 0E9h
.data:0000000140003014                 db 53h, 18h, 4Fh, 0B8h, 6Ah, 0CBh, 87h, 58h, 5Bh, 39h
.data:000000014000301E                 db 1Eh, 0"""

def parser(data):
    result = []
    for i in range(2,len(data),1):
        if data[i] == "h":
            result.append(data[i-2] + data[i-1])
        if data[i] == "p":
            if data[i+3] == ")":
                result.append(data[i+2])
                result.append(data[i+2])
            else:
                result.append(data[i+3] + data[i+4])
        for j in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
            if data[i] == j:
                try:
                    if data[i+1] == ",":
                        result.append(data[i])
                except:
                    result.append(data[i])
    
    ret = []
    for i in result:
        ret.append(int(i, 16))
    return ret

data = parser(data)
print(data)

flag = []
for i in range(0,32,1):
    data[i] ^= i

    for j in range(0, i & 7, 1):
        b8 = data[i] % 2
        b7 = data[i] // 2 % 2
        b6 = data[i] // 2 // 2 % 2
        b5 = data[i] // 2 // 2 // 2 % 2
        b4 = data[i] // 2 // 2 // 2 // 2 % 2
        b3 = data[i] // 2 // 2 // 2 // 2 // 2 % 2
        b2 = data[i] // 2 // 2 // 2 // 2 // 2 // 2 % 2
        b1 = data[i] // 2 // 2 // 2 // 2 // 2 // 2 // 2 % 2
        data[i] = b1 * 64 + b2 * 32 + b3 * 16 + b4 * 8 + b5 * 4 + b6 * 2 + b7 + b8 * 128

    flag.append(data[i])

for i in flag:
    print(chr(i), end="")