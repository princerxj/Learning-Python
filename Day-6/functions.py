# Functions - Block of statements that perform a specific task
# Syntax : def func_name(param1, param2.....) : <-- Known as Function definition
#             #some work
#             return value
# func_name(arg1, arg2....) #function call
def sum(a, b):
    s = a + b
    return s


print(sum(1, 8))


def print_hello():
    print("hello")


print_hello()


def avrage(a, b, c):
    sum = a + b + c
    return sum / 3


print(avrage(1, 2, 10))

# Write a program to print the length of a list(list is the param)
list = [1, 2, 3, 5, 983, 9]


def list_len(list):
    count = 0
    for el in list:
        count += 1
    return count


print(list_len(list))

# write a program to print the elements of a list on a single line


def ele_list(list):
    for items in list:
        print(items, end=" ")


ele_list(list)


# Write a program to find the factorial of n
def fac_n(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod


n = int(input("Enter a number to find factorial of : "))
print(fac_n(n))


# Write a program to convert USD to INR
def conv_inr(n):
    return n * 80


n = int(input("Enter amount in USD : "))
print(conv_inr(n))
