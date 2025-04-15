# Recursion - When a function calls itself repeatedly
# Recursive calls for printing n to 1
def show(n):
    if (n == 0):
        return
    print(n)
    show(n - 1)


show(5)

# Factorial of n


def fac_n(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fac_n(n-1)


print(fac_n(6))

# Write a recursive function to find the sum of first n numbers


def sum_n(n):
    if (n == 0 or n == 1):
        return n
    else:
        return n + sum_n(n - 1)


n = int(input("Enter a number : "))
print(sum_n(n))
