# Author: Sayidali Mahad

user_name = input("What is your name? ")
print("Welcome", user_name,"!")

score = 0  # Initialize the integer variable for the score

# 2. Question 1

q1 = input("Q1: What Python keyword prints text to the screen? ")

if q1 == "print" or q1 == "print()":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The right answer is 'print'.")


# 3. Question 2

q2 = input("Q2: What is 2 to the power of 3? ")

if q2 == "8" or q2 == "eight":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The right answer is 8.")


# 4. Question 3

q3 = input("Q3: What is the largest mammal on Earth? ")

if q3 == "blue whale":
    print("Spot on! Correct!")
    score += 1
elif q3 == "whale":
    print("Close enough! I will accept 'whale'. Correct!")
    score += 1
else:
    print("Incorrect. The right answer is the Blue Whale.")


# 5. Final Message
print(user_name, "you scored" ,score, "out of 3.")
