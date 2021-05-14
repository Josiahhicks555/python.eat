import random

name = "Josiah"
question = "What to eat"
answer = ""

random_number = random.randint(1,6)

if random_number == 1:
    answer = "Pizza" + (" - (Thats my #3 favorite food)")

elif random_number == 2:
    answer = "Chicken" + (" - (Thats my #1 favorite food)")
    
elif random_number == 3:
    answer = "Cheeseburger" + (" - (Thats my #2 favorite food) ")

elif random_number == 4:
    answer = "Fish"

elif random_number == 5:
    answer = "Pasta"

elif random_number == 6:
    answer = "I Don't Know"

else:
    answer = "Error"

print(name + " asks: " + question)
print("You want to eat: " + answer)
