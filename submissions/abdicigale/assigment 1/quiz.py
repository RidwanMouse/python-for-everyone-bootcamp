# waydiinta magaca qofka
name=input("Enter Your Name ")
print("Soo Dhawaaw ", name)
# suaasha 1aad sheeg qaarada ay ku taal Somaliya
score=0
print("1. Waa maxay qaaradda ay ku taal Soomaaliya?")
suaasha1=input("Jawaabta ")
if suaasha1.lower()=="afrika" or suaasha1.lower()=="africa":
    print("waa saxantahay ") 
    score+=2
else:
    print("Khalad waayay ")
# Suaasha 2aad python luqad programing miyaa?
print("Ma run baa in Python yahay luuqad programmer-ka loo isticmaalo?")
suaasha2=input("Jawaabta ")
if suaasha2.lower()=="Haa"or suaasha2.lower()=="haa":
    print("Waa saxantahay")
    score+=2
else:
    print("Khalad waayay")
# Suaasha 3aad meeqa waayay 15x2 ?
print("Waa maxay natiijada 15 x 2? ")
suaasha3=input("Jawaabta ")
suaasha4=int(suaasha3)
if suaasha4==30:
    print("Waa saxantahay ")
    score+=2
else:
    print("Khalad waayay")

# Natiijada Ugu Dambaysa 
print("-"*30)
print(f"Hambalyo {name}!")

suaalo_saxan = score//2
print(f"Waxaa si sax ah uga jawaabtay {suaalo_saxan} suaal oo kamid ah 3 suaal oo lagu waydiiyay  ")
