import  math
#basic variables
a = 10
b = 10.0
c = "10"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#explecit type conversion
x="25"
print(int(x)+10)

#implicit type conversion
print(type(3.0+2))

#dynamic typing: variable type is determined at runtime
z=5
print(type(z), z)
z="5"
print(type(z), z)
z=True
print(type(z), z)

#is_instance practice
def check_type(x):
    if isinstance(x, (int, float)):
        print("This is number")
    else:
        print("This is not number")


lenght=5.2
width=3.1
print(f"area {lenght*width:.2f}")

#concatenation
name="Маx"
age=22
print(f"Hello my name is {name}, I am {age}")

#tape string
x=17
print("Number: {}".format(x))
name="Max"
print("{}".format(name))
first ="Ada"
last="Lovelace"
print("{} {}".format(first,last))
print("My name is {first} {last}".format(first="Alan", last="Turing"))
print("{:.2f}".format(math.pi))
num=42
print("|{:>5}|".format(num))
print("|{:^5}|".format(num))
print("|{:<5}|".format(num))