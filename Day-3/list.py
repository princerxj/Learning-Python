# Lists - A built in data type that stores set of values . It can store values of different datatypes
# Example : marks = [87, 64, 33, 95, 76]
# student = ["karan", 85, "Delhi"] #student[0] = karan
# len(student) : returns the length of the list
marks = [87, 64, 33, 95, 76]
print(marks)

# List slicing : Similar to the string slicing , syntax : ,marks[starting_index : ending_index] with ending index not included,
# negative indices in the slicing similar to the string slicing
print(marks[1: 2])
print(marks[-3: -1])

# List methods
marks.append(4)  # adds one element at the end
marks.sort()  # sorts in ascending order
marks.sort(reverse=True)  # sorts in descending order
marks.reverse()  # reverse the list
marks.insert(0, 12)  # insert element at i index
print(marks)
marks.remove(12)  # removes the first occurence of element
marks.pop(1)  # removes the element at index i
print(marks)
