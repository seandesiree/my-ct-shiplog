place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    lighting = input ("Do you want to light a torch or proceed in the dark ")
    if lighting == "light a torch":
        print("Blaze ahead")
    elif lighting == "proceed in the dark":
        print("Be careful creatures are about")
    else:
        print("You find a hidden treasure!")


attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > "100" else "conference room"
print(venue)

speakers = "Needs Speakers" if attendees > "100" else "Acoustic is great!"
print(speakers)

projector = "Needs Projector" if attendees > "100" else "Use a laptop"
print(projector)

vegetarian = input("Are you a vegetarian? Yes/No")
meal = "Veggie Delight Caterers" if vegetarian == "Yes" else "Gourmet Meals Caterers"
print(meal)


try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide a 0")


try:
    y = 1 / "apple"
except TypeError:
    print("You can't divide a integer and a string")


file = input("What is the name of your file? ")
user_input = open("thisfile.txt")
try:
    user_input = open("thisfile.txt")
    print("There is something here!")
except:
    pass


weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

accessories = "hat" if weather == "sunny" else "boots"
print(accessories)

sun_burn = "sunscreen" if weather == "sunny" else "sunglasses"



try:
    user_input = open("thisfile.txt")
    print('there is something herre!')
except:
    pass


import random

memory_usage = random.randint(0, 100)
space = random.randint(0, 100)
cpu_usage = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

if memory_usage > 90:
    print("High Memory usage!")
elif memory_usage > 80 and memory_usage <= 90:
    pass

if space > 90:
    print("High Space usage!")
elif space > 80 and space <= 90:
    pass