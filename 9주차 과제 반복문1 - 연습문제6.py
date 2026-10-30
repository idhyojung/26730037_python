m = 0

for i in range(100): 
    n = int(input())
    if n == 0: 
        break
    if n > m:  
        m = n

print(m)
