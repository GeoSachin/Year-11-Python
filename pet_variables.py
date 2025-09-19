name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95
#Finished initializing variables

age += 1
billing_address = '17 Park Street'
vaccinated = False
ccard = input('Enter your credit card number: ')
owner_name = 'Alex Jones'
account_balance -= 25 #Deducts 25 from account balance BUT it is not a terminating decimal
account_balance = round(account_balance, 2) #Rounds the account balance to 2 decimal places
#Finished updating the variables

print(age)
print(billing_address)
print(vaccinated)
print(ccard)
print(owner_name)
print(account_balance)
#Prints the values to check whether the changes were made