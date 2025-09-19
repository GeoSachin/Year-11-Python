pet1 = {
'name' : 'Bonnie',
'animal category' : 'Cat',
'age' : 3,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95,
}

#Making the changes to the dictionary
pet1['name'] = 'Miss Bonnie'
pet1['age'] += 1
dog = pet1.copy() # Copying pet1 to dog by cloning the dictionary
dog['animal category'] = 'Dog' #Changing the animal category to dog since it is a different pet
print(dog)
print(pet1)
#Printing the values to check whether the changes were made