# Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# Print multiplication table of a number n
n = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(n, "X", i, "=", n*i)
    i += 1

# Print the elements of the following list using a loop :
lst = [1, 4, 9, 16, 25, 356, 49, 64, 81, 100]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# Search for a number in a tuple using loop
tple = (1, 4, 9, 16, 25, 356, 49, 64, 81, 100)
n = int(input("Enter the number to search : "))
flag = 0
i = 0
while i < len(tple):
    if (tple[i] == n):
        flag = 1
        print(n, "is present at index", i, "in the tuple")
    i += 1

if (flag == 0):
    print("Number not found")
