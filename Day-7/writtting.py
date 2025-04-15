# f = open("demo.txt", "w")
# f.write("this is a new line")  # it overwrites the entire file

f = open("demo.txt", "a")
f.write("\nThis is a new line")  # adds to the file
