SampleList = ["PetName", "Species", "age", "vaccination status"]
def Print(Pet): #This function takes a list as an argument and prints the values of the list
    for i in range(len(Pet)):
        if i == 0:
            print("Name: ", Pet[i])
        elif i == 1:
            print("Species: ", Pet[i])
        elif i == 2:
            print("Age: ", Pet[i])
        elif i == 3:
            print("Vaccination Status: ", Pet[i])
        else:
            print("Invalid index")
Dog = SampleList.copy() # Copying SampleList to Dog by cloning the list
Dog[0] = "Miss Bonnie"
Dog[1] = "Dog" 
Dog[2] = 4 
Dog[3] = False 
Print(Dog)
Cat = SampleList.copy() # Copying SampleList to Cat by cloning the list
Cat[0] = "Miss Kitty" 
Cat[1] = "Cat"
Cat[2] = 3 
Cat[3] = True
Print(Cat)
Fish = SampleList.copy()  # Copying SampleList to Fish by cloning the list
Fish[0] = "Miss Goldie" 
Fish[1] = "Fish" 
Fish[2] = 1 
Fish[3] = False 
Fish.remove("Miss Goldie") #Removing the name of the fish
Blowfish = SampleList.copy() # Copying SampleList to Cat by cloning the list
Blowfish[0] = "Hootie" 
Blowfish[1] = "Blowfish"
Blowfish[2] = 34 
Blowfish[3] = False
Dog = False
Print(Cat)
Print(Blowfish)
Print(Fish)# Printing the values to check whether the changes were made (Should prink the Fish list without the name)
#This code creates a list of pets and their details, then modifies the list to create new pets with different details.
# The code then prints the details of each pet.
