# Convert decimal to binary (without built-in functions)

# Taking input from user
num = int(input("Enter a decimal number: "))

# Store original number
original_num = num

binary = ""

# Convert to binary
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

# Output
print("Binary of", original_num, "is:", binary)
