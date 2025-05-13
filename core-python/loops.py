#Вивести всі числа від 1 до 100, що діляться на 3 без остачі.
def task_1():
    for x in range(1,100):
        if x % 3 == 0:
            print(x)
#Обчислити факторіал введеного користувачем числа (n!).
def task_2(n):
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел")

    if n ==0 or n ==1:
        return 1

    result=1
    for i in range (2, n+1):
        result*=i
    return result

#Знайти суму всіх парних чисел у діапазоні від a до b.
def task_3(a,b):
    sum=0
    for n in range(a, b):
        if n%2==0:
            sum+=n
    return sum

#Вивести таблицю множення (від 1 до 10).
def task_4():
    for number in range(1,10):
        for multiplier in range(1,11):
            print(f"{number}: {number} * {multiplier} = {number*multiplier}")

#Вивести перші n чисел послідовності Фібоначчі.
def task_5(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

#Зчитувати числа, поки користувач не введе 0. Потім вивести їхню суму.
def task_6():
    sum=0
    while True:
        try:
            number = int(input("Enter number, zero for stop: "))
        except:
            print("Invalid input.")
            continue
        if number == 0:
            break
        sum+=number

    print("Sum: ",sum)

#Намалювати прямокутник з зірочок розміром NxM (вкладений цикл).
def task_7(n, m):
    for _ in range(n):
        for _ in range(m):
            print("*", end="")

#Знайти перше число від 1 до 1000, яке ділиться на 17, 13 і 19 одночасно.
def task_8():
    for number in range(1, 1000):
        if number%17 == 0 and number%13 == 0 and number%19 == 0:
            return number

#Вивести всі прості числа до 100.
def task_9(n):
    # Виключаємо числа менші або рівні 1
    if n <= 1:
        return False
    # 2 — єдине парне просте число
    if n == 2:
        return True
    # Виключаємо парні числа (крім 2)
    if n % 2 == 0:
        return False
    # Перевіряємо непарні дільники до sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

#Порахувати кількість цифр у введеному числі.
def task_10(n):
    count=0
    n=abs(n)
    if n == 0:
        return 1
    while n>0:
        count+=1
        n//=10
    return count

if __name__=="__main__":
    while True:
        n = input("Enter task number (1-20) or 'q' to quit: ")
        if n == 'q':
            break
        try:
            eval(f"task_{n}()")
        except:
            print("Invalid task number")