number1 = int(input("Number"))
value = 1
def factorial_calc(number):
    value = 1
    for i in range(1,number+1):
        if i == number:
            value=value*i
            print(value)
            number1 = int(input("Number"))
            factorial_calc(number1)
        else:
            value=value*i
for i in range(1,number1+1):
    if i == number1:
        value=value*i
        print(value)
        number1 = int(input("Number"))
        factorial_calc(number1)
    else:
        value=value*i