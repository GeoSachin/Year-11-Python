number = int(input("Number? "))
Current = 0
while True:
    if number == 99:
        print(Current)
        break
    else:
        Current=Current+number
        number = int(input("Number? "))
