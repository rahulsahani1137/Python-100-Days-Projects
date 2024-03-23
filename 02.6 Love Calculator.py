print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?

combined_name = name1.lower() + name2.lower()

true_occurance = 0
love_occurance = 0

for name_char in combined_name:
    #Considering Indian Audiance
    for true_char in "saccha":
        if name_char == true_char:
            true_occurance += 1
            
    for love_char in "pyaar":
        if name_char == love_char:
            love_occurance += 1
            
score = int(str(true_occurance) + str(love_occurance))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"You score is {score}.")