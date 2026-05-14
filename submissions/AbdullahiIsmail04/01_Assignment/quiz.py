# Abdullahi Ismail
# This is a simple quiz program that asks the user three questions about Somalia and keeps track of their score.

user_name = input("Enter your name: ")
print("Welcome, ", user_name)
print("===================")

# Tracking variables
score = 0
total_questions = 3

# Question 1
print("What is the capital of Somalia? ")
answer = input("Your answer: ") # Accepts only 'Mogadishu' and 'mogadishu'

if answer == "Mogadishu" or answer == "mogadishu":
    print("Correct! The capital of Somalia is Mogadishu.")
    score += 1
else:
    print("Incorrect. The capital of Somalia is Mogadishu.")

# Question 2
print("What is the largest city in Somalia? ")
answer = input("Your answer: ") # Accepts only 'Mogadishu' and 'mogadishu'

if answer == "Mogadishu" or answer == "mogadishu":
    print("Correct! The largest city in Somalia is Mogadishu.")
    score += 1
else:
    print("Incorrect. The largest city in Somalia is Mogadishu.")

# Question 3
print("What is the official language of Somalia? ") 
answer = input("Your answer: ") # Accepts only 'Somali' and 'somali'

if answer == "Somali" or answer == "somali":
    print("Correct! The official language of Somalia is Somali.")
    score += 1
else:    
    print("Incorrect. The official language of Somalia is Somali.")

print(user_name, "You've scored ", score, " out of", total_questions)