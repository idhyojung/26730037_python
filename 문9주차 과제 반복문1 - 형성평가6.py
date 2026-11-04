count = 0  

for i in range(100):  
    n = int(input())
    if n == 0:  
        break
    if n % 2 == 0: 
        count += 1 
print(count)
