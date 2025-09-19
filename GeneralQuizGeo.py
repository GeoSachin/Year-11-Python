import math
import random
RangeUpper = 50 #Simply used as placeholder values until changed later in the code
RangeLower = 1 #Simply used as placeholder values until changed later in the code
def Discriminant(a,b,c): #A function to calculate how many x intercepts a quadratic equation has
    Discrim = b*b-4*a*c
    if Discrim > 0:
        return 2
    elif Discrim == 0:
        return 1
    else:
        return 0
def SelectSubject(): #This function is used to select the subject that the user wants to learn
    #Possible subjects is Maths, Physics, General Knowledge
    print("Which subject would you like to learn?")
    Subject = input("Choose from maths, physics, and general knowledge: ")
    if "math" in Subject.lower(): #lower is used to ensure that even if the input is capitalised, the code will work
        return "maths" #The return value makes the value of the function, whenever it is called, equal to whatever is returned
        print("Answer each question as an integer with no decumals or units")
    elif "phy" in Subject.lower():
        return "physics"
        print("Answer each question as an integer with no decumals or units")
    elif "general" in Subject.lower() or "knowledge" in Subject.lower():
        return "General Knowledge"
        print("Answer each question as an integer with no decumals or units")
    else:
        return SelectSubject()
Subject = SelectSubject() #Calling the function so it runs
def DifficultySelect():
    print("What difficulty would you like to learn?") #Asking which difficulty to learn
    if Subject == "General Knowledge":
        Difficulty = "General Knowledge"
    else:    
        Difficulty = input("Choose from primary, preliminary, HSC or random: ")
        if "prim" in Difficulty.lower():
            return "easy"
        elif "prelim" in Difficulty.lower():
            return "medium"
        elif "hsc" in Difficulty.lower():
            return "hard"
        elif "rand" in Difficulty.lower():
            return "random"
        else:
            return DifficultySelect() #This 'return' value will be the value of the function whenever it is called
Difficulty = DifficultySelect()
Answers = { #An empty table to be used later when answers are added into it
}
Questions = {#An empty table to be used later when questions are added into it
}
def GetRangeUpper(): #Getting the maximum question number that the questions can be asked from
    if Subject == "maths":
        if Difficulty == "easy":
            return 5
        elif Difficulty == "medium":
            return 10
        elif Difficulty == "hard":
            return 15
        else:
            return 15
    elif Subject == "physics":
        if Difficulty == "easy":
            return 20
        elif Difficulty == "medium":
            return 25
        elif Difficulty == "hard":
            return 30
        else:
            return 30
    elif Subject == "General Knowledge":
            return 40
def GetRangeLower():#Getting the minimum question number that the questions can be asked from
    if Subject == "maths":
        if Difficulty == "easy":
            return 0
        elif Difficulty == "medium":
            return 6
        elif Difficulty == "hard":
            return 11
        else:
            return 0
    elif Subject == "physics":
        if Difficulty == "easy":
            return 16
        elif Difficulty == "medium":
            return 21
        elif Difficulty == "hard":
            return 26
        else:
            return 16
    elif Subject == "General Knowledge":
            return 31
def GetRandomNumber(First,Last): #A function that makes it much easier to get a random number, given the range
    RandomNumber = math.floor(random.randint(int(First),int(Last)))
    return RandomNumber
def QuestionsAndAnswer():
        Rand1 = GetRandomNumber(1,10)
        Rand2 = GetRandomNumber(1,10)
        Rand3 = GetRandomNumber(1,10)
        Rand4 = GetRandomNumber(4,10)
        Rand5 = GetRandomNumber(6,10)
        Rand6 = GetRandomNumber(1,5)
        Rand7 = GetRandomNumber(1,89)
        Rand8 = GetRandomNumber(6,10)
        #Here, the quesitons and answers will be defined:
        Questions[0] = "What is " + str(Rand1) + " + " + str(Rand2) + "? "
        Answers[0] = Rand1 + Rand2
        Questions[1] = "What is " + str(Rand3) + " * " + str(Rand4) + "? "
        Answers[1] = Rand3 * Rand4
        Questions[2] = "What is " + str(Rand5) + " - " + str(Rand6) + "? "
        Answers[2] = Rand5 - Rand6
        Questions[3] = "A triangle has angles of 90 and " + str(Rand7) + " degrees, what is other angle (answer with just an integer)"
        Answers[3] = 90-int(Rand7)
        Questions[4] = "What is the value of " + str(Rand1) + " squared?"
        Answers[4] = Rand1*Rand1
        Questions[5] = "What is the square root of " + str(Rand2*Rand2) +"?"
        Answers[5] = Rand2
        Questions[6] = "Rounded DOWN to the nearest integer, what is the area of a circle with a radius of " + str(Rand1) +"cm?"
        Answers[6] = int(math.pi*Rand1*Rand1)
        Questions[7] = "Write an an integer, how many ways " + str(Rand3) + " people be arranged in a line?"
        Answers[7] = math.factorial(Rand3)
        Questions[8] = "Write an an integer, how many ways " + str(Rand4) + " people be arranged around a circle?"
        Answers[8] = math.factorial(Rand4-1)
        Questions[8] = "Write an an integer, how many ways " + str(Rand4) + " people be arranged around a circle if two people can not sit together?"
        Answers[8] = math.factorial((Rand4)-2)*2
        Questions[9] =  "Rounded DOWN to the nearest integer, what is the circumference of a circle with a radius of " + str(Rand1) +"cm?"
        Answers[9] = int(2*math.pi*Rand1)
        Questions[10] = "At how many points does the following equation cut the x-axis? y="+str(Rand1)+"x²+"+str(Rand2)+"x"+ "+"+str(Rand3)
        Answers[10] = int(Discriminant(Rand1,Rand2,Rand3))
        Questions[11] = "What is the gradient of the tangent of the function y=" + str(Rand2) + "x^" + str(Rand3)
        Answers[11] = int(Rand2*Rand3)
        Questions[12] = "If f(x) = x²+2x+1, find f(" + str(Rand2) + ")"
        Answers[12] = int(Rand2*Rand2+2*Rand2+1)
        Questions[13] = "What is the absolute value of " + str(Rand1*-1) +"?"
        Answers[13] = int(Rand1)
        Questions[14] = "What is the gradient of the line y=" + str(Rand1) + "x+" + str(Rand2) + "?"
        Answers[14] = int(Rand1)
        Questions[15] = "As as integer, what is the y intercept of the equation y=" + str(Rand4) + "x+" + str(Rand3)
        Answers[15] = int(Rand3)
        Questions[16] = "If I moved " + str(Rand1) + "metres and then "+ str(Rand2) + " metres, what is my total distance? (Answer as an integer without providing units)"
        Answers[16] = int(Rand1+Rand2)
        Questions[17] = "I waited " + str(Rand2) + " seconds. Then I waited another " + str(Rand3) + " seconds. How many seconds did I wait in total? (Answer as an integer with no units)"
        Answers[17] = int(Rand2+Rand3)
        Questions[18] = "If Speed = Distance/Time, what is the speed when the Distance is " + str(Rand5*Rand8) + "m and the time is " + str(Rand5) + "s? (Answer as an integer with no units)"
        Answers[18] = int(Rand8)
        Questions[19] = "If Force = Mass*Acceleration, what is the Force when the mass is " + str(Rand1) + "kg and the acceleration is " + str(Rand5) + "m/s^2? (Answer as an integer with no units)"
        Answers[19] = int(Rand1*Rand5)
        Questions[20] = "If Speed = Distance/Time, what is the distance when the speed is " + str(Rand1) + "m and the time is " + str(Rand5) + "s? (Answer as an integer with no units)"
        Answers[20] = int(Rand1*Rand5)
        Questions[21] = "Assuming gravity is 10m/s^2, how much is the gravitational force applied on an object with a mass of "+ str(Rand1) + "kg? (Answer as an integer with no units)"
        Answers[21] = int(Rand1*10)
        Questions[22] = "What is the coefficient of static friction if the static friction force is " + str(Rand5*Rand8) + "and the Normal force is " + str(Rand8) +"newtons? (Answer as an integer with no units)"
        Answers[22] = int(Rand5)
        Questions[23] = "Assuming gravity is 10m/s^2 and the object is on a flat surface, how much is the normal force applied on an object with a mass of "+ str(Rand1) + "kg? (Answer as an integer with no units)"
        Answers[23] = int(Rand1*10)
        Questions[24] = "What is the weight force of an object if the gravitational acceleration is " + str(Rand1) + "m/s^2 and the mass is " + str(Rand2) + "kg. (Answer an an integer with no units)"
        Answers[24] = int(Rand1*Rand2)
        Questions[25] = "An object goes from rest to " + str(Rand1*Rand2) + "m/s in " + str(Rand2) + " seconds. What is the magnitude of its acceleration. (Answer as an integer with no units)"
        Answers[25] = int(Rand1)
        Questions[26] = "What is the potential energy of a mass of " + str(Rand1) + "kg, " + str(Rand2) + " metres? (Assume g = 10 and answer as an integer with no units)"
        Answers[26] = int(Rand1*Rand2*10)
        Questions[27] = "What is the kinetic energy of a mass of " + str(Rand1*2) +"kg with a velocity of " + str(Rand2) + "m/s? (Answer as an integer with no units)"
        Answers[27] = int(Rand1*Rand2*Rand2)
        Questions[28] = "What is the work done by a " + str(Rand1) +"kg object that moved " + str(Rand2) + "m? (Answer as an integer with no units)"
        Answers[28] = int(Rand1*Rand2)
        Questions[29] = "What is voltage if the current is " + str(Rand1) + " amps and the resistance is " + str(Rand2) + " ohms? (Answer as an integer with no units)"
        Answers[29] = int(Rand1*Rand2)
        Questions[30] = "What is the mass, correct to nearest integer, with no units, if the density is " + str(Rand1) + "kg/m^3 and the volume is " + str(Rand2) + "m^3"
        Answers[30] = str(Rand1*Rand2)
        Questions[31] = str("How many pieces are on the board at the start of a game of chess?")
        Answers[31] = 32
        Questions[32] = "Which year was the 9/11 attack?"
        Answers[32] = 2001
        Questions[33] = "Which year was the federation of Australia taken place?"
        Answers[33] = 1901
        Questions[34] = "How many pillars of Islam are there?"
        Answers[34] = 5
        Questions[35] = "How many commandments are there, according to Christian teaching"
        Answers[35] = 10
        Questions[36] = "In which year did WW1 start?"
        Answers[36] = 1914
        Questions[37] = "In which year did WW1 end?"
        Answers[37] = 1918
        Questions[38] = "In which year did WW2 begin?"
        Answers[38] = 1939
        Questions[39] = "In which year did WW2 end?"
        Answers[39] = 1945
        Questions[40] = "What is the atomic number of oxygen?"
        Answers[40] = 8

def Correct(Answer, RandQ): #A function to check if the answer is correct
    if int(Answer) == Answers[RandQ]:
        return True #Answer was correct!
    else:
        print("Incorrect")
        print("The correct answer was: " + str(Answers[RandQ]))
        return False # Answer was wrong, so False will be returned      
def AskQuestions():
    
    Score = 0
    while True: #Always unless the loop is broken
            QuestionsAndAnswer()
            RangeLower = GetRangeLower() #Getting the lower range
            RangeUpper = GetRangeUpper() #Getting the upper range
            RandQ = random.randint(RangeLower,RangeUpper) #Getting a random question
            print(Questions[RandQ]) #Asking the questions
            Answer = input("Answer: ") #Getting the users answer
            if Correct(Answer,RandQ):
                Score = Score + 1 #Increasing score if correct
            else:
               if Score == 1:
                print("You answered 1 question correctly")
                break
               else:
                 print("You answered " + str(Score) + " questions correctly!")
                 break #Breaking the loop
AskQuestions()