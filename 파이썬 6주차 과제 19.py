#9396 문자열 - 자가진단 9
pwd = input()
pattern = input()

repeated_pattern = pattern * 5

if pwd in repeated_pattern:
    print("YES")
else:
    print("NO")
