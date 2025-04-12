# Write a program to take the marks as input and give grades based on that
marks = int(input("Enter your marks : "))
if (marks >= 90):
    print("You got A grade")
elif (marks < 90 and marks >= 80):
    print("You got B Grade")
elif (marks < 80 and marks >= 70):
    print("You got C Grade")
elif (marks < 70):
    print("You got D grade")

# Write a program to take number as input and print if it is odd or even
num = int(input("Enter a number : "))
if (num % 2 == 0):
    print(num, "is even")
else:
    print(num, "is odd")

# Write a program to find the greatest of three numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
max = num1
if (num2 > max):
    max = num2
if (num3 > max):
    max = num3
print("The max of", num1, num2, "and", num3, "is", max)
