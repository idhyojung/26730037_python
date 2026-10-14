#9397 문자열 - 형성평가 1
s = input()

for i in range(len(s) - 1, -1, -1):
    if i == 0:
        print(s[i])
    else:
        print(s[i], end="-")
