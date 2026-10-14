#9392 문자열 - 연습문제 8
s = input()

for i in range(len(s)):
    if i == len(s) - 1:
        print(s[i])
    else:
        print(s[i], end=",")

