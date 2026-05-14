# Name: Abdisalaam Salad Ali
# Description: A simple English Quiz program for assignment one

# 1. Greeting
name= input("What is your name? ")
print("welcome ," + name)

#2. Questions 
#Q1
score = 0
print("What is the largest planet in our solar system?")
Ans1= input(" your answer:")
if Ans1 == "Jupiter" or Ans1 == "jupiter":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is Jupiter.")
#Q2
print("What does CPU stand for?")
Ans2= input(" your answer:")
if Ans2 == "Central Processing Unit":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is Central Processing Unit.")
#Q3
print("What is the chemical symbol for water?")
Ans3= input(" your answer:")
if Ans3 == "H2O":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is H2O.")
#Q4
print("Which bird is the universal symbol of peace??")
Ans4= input(" your answer:")
if Ans4 == "Dove":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is Dove.")
#Q5 
print("Name two primary colors (Red, Blue, Yellow):")
color1 = input("First color: ")
color2 = input("Second color: ")

if color1 == "Red" and color2 == "Blue":
    print("Correct ")
    score += 1
else:
    print("Wrong! The correct answer is Red and Blue.")
    


#3. Final Score

print(name + " , your final score is: " + str(score) + " out of 5.")