name=input("What is your name? ")
print("Hello, " + name + "! lets start the quiz!")
score=0
print("Besides Laas Geel, what is the second major prehistoric rock art site near Hargeisa?")
answer1=input("your answer: ")
if answer1.lower()=="laasgeele":
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is laasgeel.")
print("Your score is: " + str(score)) 
print("What is 2 + 2?")
answer2=input("your answer: ")
if answer2=="4":
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is 4.")  
print("Your score is: " + str(score))
print("In which year was Radio Hargeisa established?")
answer3=input("your answer: ")
if answer3.lower()=="1943":
    print("Correct!")
    score+=1    
else:
    print("Wrong! The correct answer is 1943.")
print("Your score is: " + str(score))
print("Besides Laas Geel, what is the second major prehistoric rock art site near Hargeisa?")
answer4=input("your answer: ")
if answer4.lower()=="dhagah kure":
    print("Correct!")
    score+=1
else:    print("Wrong! The correct answer is dhagah kure.")
print("Your score is: " + str(score))
print("What is the largest mammal?")
answer5=input("your answer: ")
if answer5.lower()=="blue whale":
    print("Correct!")
    score+=1    
else:    print("Wrong! The correct answer is Blue Whale.")
print("Your score is: " + str(score))
print("Quiz completed! Your final score is: " + str(score) + "/5")
# The code is a simple quiz program that asks the user five questions and keeps track of their score. It uses conditional statements to check the user's answers and provides feedback on whether they are correct or wrong. Finally, it displays the user's final score out of 5.
