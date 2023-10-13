def add_numbers(a, b, c, d, e, f):
    return a + b + c + d + e + f
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))
num6 = float(input("Enter the sixth number: "))
result = add_numbers(num1, num2, num3, num4, num5, num6)
print("The sum of {}, {}, {}, {}, {}, and {} is: {}".format(num1, num2, num3, num4, num5, num6, result))
