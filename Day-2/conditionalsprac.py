# Write a program to take the marks as input and give grades based on that
marks = (int)(input("Enter your marks : "))
if (marks >= 90):
    print("You got A grade")
elif (marks < 90 and marks >= 80):
    print("You got B Grade")
elif (marks < 80 and marks >= 70):
    print("You got C Grade")
elif (marks < 70):
    print("You got D grade")
