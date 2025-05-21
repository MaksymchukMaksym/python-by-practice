#temperature_classifier
def task_1(temp):
    if temp<0: return "Freezing"
    elif 0 <= temp <10: return "Cold"
    elif 10 <= temp < 20: return "Cool"
    elif 20 <= temp < 30: return "Warm"
    elif temp>=30: return "Hot"

#password check
def task_2():
    password="OpenAI2025"
    temp = input("Input password")
    if temp  == password:
        print("Access granted")
    else:
        print("Access dinied")

#calculator
def task_3(a,b,op):
    if op=="+":
        print(a+b)
    elif op =="-":
        print(a-b)
    elif op =="*":
        print(a*b)
    elif op == "/":
        if(b==0):
            print("divider ==0")
            return None
        print(a/b)

    else:
        print("don't correct operation")

if __name__=="__main__":
    while True:
        number = input("Input number of task for testing")
        if number == 'q':
            break
        try:
            eval(f"task_{number}")
        except:
            print("Invalid number")