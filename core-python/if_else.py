def temperature_classifier(temp):
    if temp<0: return "Freezing"
    elif 0 <= temp <10: return "Cold"
    elif 10 <= temp < 20: return "Cool"
    elif 20 <= temp < 30: return "Warm"
    elif temp>=30: return "Hot"

def password_check():
    password="OpenAI2025"
    temp = input("Input password")
    if temp  == password:
        print("Access granted")
    else:
        print("Access dinied")

def calculator(a,b,op):
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

