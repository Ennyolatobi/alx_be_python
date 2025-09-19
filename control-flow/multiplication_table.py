number = int(input("Enter a number to see its multiplication table: "))
for count in range(1, 11):
    product = number * count
    print(f"{number} * {count} = {product}")