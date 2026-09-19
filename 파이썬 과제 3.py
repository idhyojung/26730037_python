def print_pattern(rows, cols, char):
    for r in range(rows):
        for c in range(cols):
            print(char, end="")
        print()  


print_pattern(3, 5, "*")
