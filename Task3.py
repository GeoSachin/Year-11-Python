import random
num1 = random.randint(1,45)
print(num1)
num2 = random.randint(1,45)
while num1 == num2:
    num2 = random.randint(1,45)
num3 = random.randint(1,45)
while num3 == num1 or num3 == num2:
    num3 = random.randint(1,45)
num4 = random.randint(1,45)
while num4 == num1 or num4 == num2 or num4 == num3:
    num4 = random.randint(1,45)
num5 = random.randint(1,45)
while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    num5 = random.randint(1,45)
num6 = random.randint(1,45)
while num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
    num6 = random.randint(1,45)
print("The numbers are: ", num1, num2, num3, num4, num5, num6)