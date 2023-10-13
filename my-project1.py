Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add_numbers(a, b, c, d):
...     return a + b + c + d
... num1 = float(input("Enter the first number: "))
... num2 = float(input("Enter the second number: "))
... num3 = float(input("Enter the third number: "))
... num4 = float(input("Enter the fourth number: "))
... result = add_numbers(num1, num2, num3, num4)
... print("The sum of {}, {}, {}, and {} is: {}".format(num1, num2, num3, num4, result))
