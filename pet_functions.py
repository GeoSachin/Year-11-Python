name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num): #Checks if the credit card number is valid
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False


help()
increase_age()
print(age)

print(verify_credit_card("1234433410010000")) #Get the users credit card number

ccard = input('Enter your credit card number: ')
if verify_credit_card(ccard):
  print("Valid credit card")
  account_balance -= 39
  account_balance = round(account_balance, 2) #Rounds the account balance to 2 decimal places
  if account_balance > 39: #Checking if there are sufficient funds for the vaccination
    vaccinated = True
    print("Vaccination successful")
    print(round(account_balance,2))
  else:
    print("Insufficient funds")
    print("Vaccination failed")