# is_palindrom
def task_1():
    s = "abba"
    i = 0
    j = -1
    mid = len(s) // 2
    arr1 = s[:mid]
    arr2 = s[mid:]
    if arr1 == arr2[::-1]:
        print("It's Polindrom")


# longest_word in sentence
def task_2():
    s = "Max is good man"
    s = s.split()
    longest = ""
    for el in s:
        if len(el) > len(longest):
            longest = el
    print(longest)


# count_vowels
def task_3():
    count = 0
    data = "Max is good man"
    s = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for el in data:
        if el in s:
            count += 1
    return count


# replace_spaces
def task_4():
    s = "Max is good man"
    s.replace(' ', "_")
    print(s)


# remove_duplicates
def task_5():
    data = "Hello Nikko"
    "".join(dict.fromkeys(data))
    print(set(data))


# char_frequency
def task_6():
    s = "Hello Nikko"
    l = list(s)
    freq = {}
    for el in l:
        freq.update({el: freq.get(el, 0) + 1})
    return freq


# change register to opposite
def task_7():
    s = "Hello NiKko"
    s = "".join([ch.lower() if ch.isupper() else ch.upper() for ch in s])
    return s


# reverse each word separately
def task_8():
    s = "Hello world"
    words = s.split(" ")
    reversed_words = [w[::-1] for w in words]
    print("".join(reversed_words))


# delete all symbols instead letters
def task_9():
    s = "Hello123 world"
    print("".join([ch for ch in s if s.isalpha()]))


# is_email
def task_10():
    s = "something@gmail.com"
    if s.count('@') != 1:
        return False
    parts = s.split('@')
    if len(parts) != 2:
        return False
    username, domain = parts

    if not username:
        return False

    if '.' not in domain:
        return False

    domain_parts = domain.split('.')

    if len(domain_parts) < 2:
        return False

    for part in domain_parts:
        if not part:
            return False

    return True


if __name__ == "__main__":
    n = input("Input number of task:")
    print("q. Quit")
    try:
        eval(f"task_{n}()")
    except:
        print("Invalid number")
