#Python Hello World
#Try
x = "Hello"
y = "World"
print(x)
# You can add "\n" to force a new line after printing World.
print(y+"\n")

# Experiements with variables and strings
# Make a string all upper case.
x="Green eggs and ham".upper()
print(x)

# Remove spaces by replacing with an empty string.
x=x.replace(" ", "")
print(x)

# Remove GREEN.
x=x.replace("GREEN","")
print(x)

# Remove ANDHAM.
x=x.replace("ANDHAM","")
print(x+"\n")

# We could have done all this in one assignament to be REALLY FANCY...
x="Green eggs and ham".upper().replace(" ", "").replace("GREEN","").replace("ANDHAM","")
print(x+"\n")

# We could also have done it without even using a variable!
print("All in one shot: \n"+"Green eggs and ham".upper().replace(" ", "").replace("GREEN","").replace("ANDHAM",""))

# All finished!
