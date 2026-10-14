#9395 문자열 - 연습문제 9
a, b = input().split()

triple_a = a * 3

if b in triple_a:
    print(a + b)
else:
    print(b * 2)
