print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5. Modulo du turfu")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", num1 + num2)

elif choice == 2:
    print(num1, "-", num2, " = ", "<place_subtract_result_here>")

elif choice == 3:
    print(num1, "*", num2, "=", num1*num2)

elif choice == 4:
    print(num1, "/", num2, " = ", "<place_divide_result_here>")
    
elif choice == 5:
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Invalid input")
