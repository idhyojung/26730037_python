n = int(input())

result = 1  
i = 1       

while True:
    result *= i
    if result >= n:
        print(result)
        break
    i += 1
