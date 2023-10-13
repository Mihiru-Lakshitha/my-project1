def add_numbers(*args):
    return sum(args)

# Get input from the user
num_count = int(input("Enter the number of values you want to add: "))

# Initialize an empty list to store the numbers
numbers = []

# Get the numbers from the user
for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Calculate the sum using the add_numbers function
result = add_numbers(*numbers)

# Print the result
print("The sum of the numbers is:", result)
