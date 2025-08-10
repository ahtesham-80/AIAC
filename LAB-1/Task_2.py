def find_largest_number():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    largest = max(num1, num2, num3)
    print("The largest number is:", largest)

numbers = []
for i in range(3):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)
largest = max(numbers)
print("The largest number is:", largest)
