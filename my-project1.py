def add_numbers(*args):
    return sum(args)

numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(6)]
result = add_numbers(*numbers)
print("The sum of {} is: {}".format(", ".join(map(str, numbers)), result))
