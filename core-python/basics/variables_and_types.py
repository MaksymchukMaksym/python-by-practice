import math


# basic variables
def task_1():
    a = 10
    b = 10.0
    c = "10"
    d = True

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))


# explecit type conversion
def task_2():
    x = "25"
    print(int(x) + 10)

    # implicit type conversion
    print(type(3.0 + 2))

    # dynamic typing: variable type is determined at runtime
    z = 5
    print(type(z), z)
    z = "5"
    print(type(z), z)
    z = True
    print(type(z), z)


# is_instance practice/check_type
def task_3(x):
    if isinstance(x, (int, float)):
        print("This is number")
    else:
        print("This is not number")


# concatenation
def task_4():
    lenght = 5.2
    width = 3.1
    print(f"area {lenght * width:.2f}")

    name = "Маx"
    age = 22
    print(f"Hello my name is {name}, I am {age}")


# tape string
def task_5():
    x = 17
    print("Number: {}".format(x))
    name = "Max"
    print("{}".format(name))
    first = "Ada"
    last = "Lovelace"
    print("{} {}".format(first, last))
    print("My name is {first} {last}".format(first="Alan", last="Turing"))
    print("{:.2f}".format(math.pi))
    num = 42
    print("|{:>5}|".format(num))
    print("|{:^5}|".format(num))
    print("|{:<5}|".format(num))


if __name__ == "__main__":
    while True:
        n = input("Choose number of task:")
        print("q. Quit")
        if n == "q":
            break
        try:
            eval(f"task_{n}()")
        except:
            print("Invalid number")
