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
    pass

try:
    y = 1 / "apple"
except ValueError:
    pass


file = input("What is the name of your file? ")


weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

accessories = "hat" if weather == "sunny" else "boots"
print(accessories)

sun_burn = "sunscreen" if weather == "sunny" else "sunglasses"

