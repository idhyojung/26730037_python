#9401 문자열 - 형성평가 5
name, height, weight = input().split()

height = int(height)
weight = float(weight)

print(f"NAME: {name}")
print(f"HEIGHT: {height}cm")
print(f"WEIGHT: {weight:.2f}kg")
