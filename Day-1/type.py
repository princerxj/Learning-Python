# type conbersion
a = 3
b = 8.33

# Prints float value :: Implicit conversion as Float is superior as compared to int
print(a + b)

c = "2"
# print(a + c) #Will Give error , but we can evaluate the result using typecasting instead of type conversion
c = int(c)  # Typecasted C to int type
print(a + c)
# Will give output as string class as we typecasted a to string type
print(type(str(a)))
