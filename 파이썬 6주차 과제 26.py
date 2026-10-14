#9402 문자열 - 형성평가 6
s = input()

for i in range(len(s)):
    if i == len(s) - 1:
        print(s[i])
    else:
        print(s[i], end=".")
