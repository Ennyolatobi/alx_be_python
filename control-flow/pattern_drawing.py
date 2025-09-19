size = int(input("Enter the size of the pattern: "))
row = 1

while row <= size:
    # For each row, print 'size' number of asterisks side by side
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    row += 1
