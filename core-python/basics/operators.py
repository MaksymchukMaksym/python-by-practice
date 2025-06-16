def task_1():
    # precedence operations
    a = 5 + 2 * 3

    # parentheses take precedence over multiplication
    b = (5 + 2) * 3
    # 5 power by 2
    c = 5 ** 2 ** 1
    # floor division
    d = 15 // 4
    # modulo operation
    e = 15 % 4

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


# comprasion
def task_2():
    a = 10
    b = 5
    c = 2

    print()
    print(a > b > c)
    print(a == b or c)
    print(a and b < c)
    print(not a > b)


# operation with bits
def task_3():
    x = 5  # 0b0101
    y = 3  # 0b0011
    print()
    print(bin(x & y))
    print(bin(x | y))
    print(bin(x ^ y))
    print(bin(~x))
    print(bin(x << 1))
    print(bin(y >> 1))

    x = 5
    num_bits = 4
    mask = (1 << num_bits) - 1  # 0b1111
    print(bin(~x & mask))

    print(x << 3)  # x*8
    print(y >> 1)  # x/2


# count ones in bytes
def task_4(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


# invert_8bit
def task_5(n):
    result = 0
    for _ in range():
        result <<= 1
        result |= (n & 1)
        n >>= 1
    return result


# is and ==
def task_6():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(a == b)
    print(a is b)
    print(a is c)

    # and, or
    # and - перший хидний/останній вірний, or - останній хибний/прший вірний
    print()
    print(True and False)
    print(True and 5)
    print(0 or 3)
    print("" or "text")


# max_of_two
def task_7(a, b):
    print(((a > b) and a) or b)


# coprasion
def task_8():
    res1 = not True or False
    res2 = True or False and False
    res3 = (True or False) and False
    # 1 - not, 2- and, 3 - or
    print()
    print(res1)
    print(res2)
    print(res3)


if __name__ == "__main__":
    while True:
        n = input("Choose the number of task: ")
        print("q. Quit")
        try:
            eval(f"task_{n}()")
        except:
            print("Invalid number")
