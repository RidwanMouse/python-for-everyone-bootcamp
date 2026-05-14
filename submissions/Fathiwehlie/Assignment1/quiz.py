
#Quiz program
print("Welcome to the quiz!")

name = input("What is your name? ")
print("Hello, " + name + "! Let's get started.")

score = 0

#Question 1:

print("Question 1: What is python file extension?")
answer=input("Your answer: ")

if answer==".py" or answer=="py":
    print("You're amizing! That's correct.")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is .py.")




print("Question 2: What is the result of 5 != 5? (True/False)")
answer=input("Your answer: ")

if answer=="false" or answer=="False":
    print("You're amizing! That's correct.")
    score += 1

   
else:
    print("Sorry, that's incorrect. The correct answer is False.")



print("Question 3: Which keyword is used for decision making?")
answer=input("Your answer: ")

if answer=="if"or answer=="IF":
    print("You're amizing! That's correct.")
    score += 1
   
else:
    print("Sorry, that's incorrect. The correct answer is if")

print("Question 4: Which operator is used for logical AND?")
answer=input("Your answer: ")

if answer.lower()=="and":
    print("You're amizing! That's correct.")
    score += 1
   
else:
    print("Sorry, that's incorrect. The correct answer is and.")

print("Question 5: What is the result of True AND False? (True/False)")
answer=input("Your answer: ")

if answer=="false" or answer=="False":
    print("You're amizing! That's correct.")
    score += 1
   
else:
    print("Sorry, that's incorrect. The correct answer is False.")

print("Quiz finished!")
print(name + ", your total score is:", score, "out of 5") 




