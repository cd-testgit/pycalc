import math

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, " = ", num1 + num2)

elif choice == 2:
    print(num1, "-", num2, "=", "<place_subtract_result_here>")

elif choice == 3:
    print(num1, "*", num2, "=", "<place_multiply_result_here>")

elif choice == 4:
    print(num1, "/", num2, "=", "<place_divide_result_here>")
else:
    print("log(", num1, ") = ", math.log(num1))
