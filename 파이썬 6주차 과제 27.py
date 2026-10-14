#9403 문자열 - 형성평가 7
s = input()

# 거꾸로 출력
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")
print()

# 원래대로 출력
print(s)
