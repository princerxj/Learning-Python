# Python can be used to perform operations on a file . (read and write data)
# Types of all files :
# 1.) Text Files : .txt, .docx, .log etc.
# 2.) Binary Files : .mp4, .mov, .png, .jpeg etc.

# We have to open a file before reading or writing .
# syntax : f = open("file_name", "mode")
# mode ---> r : read mode , w : write mode
# data = f.read()
# f.close()
# Chars and their meaning :
# r - open for reading by default
# w - open for writing and reuncating the file first
# x : create a new file and open it for writing
# a : open for writing and appending at the end of the ffile if it exists
# b : binary mode
# t : text mode
# + : open a disk file for updating(reading and writing)


# Reading a file :
# We can pass some parameters too in the read function
# for example ---> data = f.read(5) : now it will read upto 5 characters only
# data = f.readline() -- Now it will read line by line
f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()
# data = f.read()
# print(data)
# print(type(data))
# f.close()
