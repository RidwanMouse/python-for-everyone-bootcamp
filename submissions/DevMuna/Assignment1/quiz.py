#Dev Muna
#This program is a simple Python quiz using input, print, and conditions

# Greeeting
name = input("What is your name? ")
print("Welcome, " + name)

Score = 0

# Question 1
print("Q1: What keyword is used to print output in Python?")
Answer1 = input("Your answer: ")
# Accept answer: "print" only,

if Answer1.lower() == "print":
    print("Correct!")
    Score+=1
else:
    print("Incorrect. The correct answer is 'print'.")


# Question 2
print("Q2: What is the correct file extension for python files?")

Answer2 = input("Your answer: ")
# Accept answer: ".py" only, 
if Answer2.lower() == ".py":
    print("Congratulations! You got it right.")
    Score+=1
else:
    print("Sorry,that's not correct. The correct answer is '.py'.")


# Question 3
print("Q3: What symbol is used to comment a single line comment in Python?")
Answer3 = input("Your answer: ")
# Accept answer: "#" or hash.
if Answer3 == "#" or Answer3.lower() == "hash":
    print("Correct!! You are doing great.")
    Score +=1
else:
    print("Incorrect. The correct answer is '#'.")


# Question 4
print("Q4: What is used  to take a user input in Python?") 
Answer4 = input("Your answer:")
# Accept answer: "input" 
if Answer4.lower() == "input":
    print("Correct! You got it right.")
    Score +=1
else:
    print("Incorrect. The correct Answer is 'input' ")


# Question 5
print("Q5: What data is used to store numbers like 5 or 10?")
Answer5  = input("Your answer:")
# accept answer: "int" or integer
if Answer5 == "int" or Answer5.lower() == "integer":
    print("Correct! You got it right!")
    Score +=1
else:
    print("Incorrect. The correct answer 'int' or 'integer' .")



#FINAL RESULT
print(name + ", you scored " + str(Score) + " out of 5.")
