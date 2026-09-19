def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


result = sum_all(1, 2, 3, 4, 5)
print("가변인수의 합계:", result)
