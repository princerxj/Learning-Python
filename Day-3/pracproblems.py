# Write a program to ask the user of his three favourite movies and store the names in a list
moviesList = []
movie1 = input("Enter your first favourite movie : ")
moviesList.append(movie1)
movie2 = input("Enter your second favourite movie : ")
moviesList.append(movie2)
movie3 = input("Enter your third favourite movie : ")
moviesList.append(movie3)
print(moviesList)

# Write a program to check if a list contains a palindrome of elements
nums = [1, 2, 3, 2, 1]
numsCpy = nums.copy()
nums.reverse()
if (nums == numsCpy):
    print("Palindromic")
else:
    print("Not palindromic")

# Write a program to count the number of students with A grade in the following tuple
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))
