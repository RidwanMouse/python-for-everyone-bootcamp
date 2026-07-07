
# Greeting
name = input("What is your name? ")
print(f"Welcome, {name}! Let's take a Python quiz.")

# Initialize score
score = 0

# Question 1
print("\nQuestion 1: What is the output of print(2 + 3)?")
answer1 = input("Your answer: ").lower()
if answer1 == "5" or answer1 == "five":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer is 5.")

# Question 2
print("\nQuestion 2: What keyword is used to define a function in Python?")
answer2 = input("Your answer: ").lower()
if answer2 == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer is def.")

# Question 3
print("\nQuestion 3: What does the len() function do? (Give a brief description)")
answer3 = input("Your answer: ").lower()
if "length" in answer3 or "size" in answer3 or "count" in answer3:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The len() function returns the length of a string, list, or other sequence.")

# Final message
print(f"\n{name}, your final score is {score} out of 3.")