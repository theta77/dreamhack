data = [172, 243, 12, 37, 163, 16, 183, 37, 22, 198, 183, 188, 7, 37, 2, 213, 198, 17, 7, 197]
flag = []

for i in range(0, 20, 1):
    for j in range(0,127,1):
        if ((-5 * j) == data[i]):
            flag.append(j)

for i in flag:
    print(chr(i), end="")


# C 코드
# #include <stdio.h>
# #pragma warning (disable:4996)

# int main() {
# 	int data[20] = { 172, 243, 12, 37, 163, 16, 183, 37, 22, 198, 183, 188, 7, 37, 2, 213, 198, 17, 7, 197 };
# 	int flag[20] = {0};
# 	for (int i = 0; (unsigned __int64)i < 20; i++) {
# 		for (int j = 0; j < 127; j++) {
# 			if ((unsigned __int8)(- 5 * j) == data[i]) {
# 				flag[i] = j;
# 			}
# 		}
# 	}

# 	for (int i = 0; i < 20; i++) {
# 		printf("%c", flag[i]);
# 	}
# }