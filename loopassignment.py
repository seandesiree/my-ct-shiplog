import random


for i in range(2, 5):
    print(i)


moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    current_feeling = random.choice(moods)
    print("On", day, "I feel", current_feeling)

num = [0]
for num in range(11,1, -1):
    print(num)


for i in range(1):
    for j in range(3):
        print("***")


times_of_day = ["morning", "afternoon", "evening"]

for day in days:
    for mood in moods:
        current_time = random.choice(times_of_day)
        print("On", day, "I feel", mood, "in the", current_time)


number = [1,5]
for count in range(1, 5): 
   for num in number:     
        print (num, 'x', count, '=', num * count) 


for i in range(1, 11):
    if i == 5:
        continue
    print(i)


mood_swings = ["angry", "happy", "anxious", "depressed"]

for hour in range(1, 24):
    current_mood = random.choice(mood_swings)
    if hour == 12:
        continue
    print("At", hour, "I feel", current_mood)

        
list_numbers = [15, 16, 17, 18, 19, 20, 21]       

for a in list_numbers:
    if a in list_numbers == 18:
        break
else:
    print("The number was not found")


# The += is telling the code to keep interatiing through the while lopp, adding 1 until the marshmallow count is no longer less than 5. 
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")


# Because the += is after the first iteraction the 0 is allowed to print. It also does print the 5 for the same reason the += being after the print makes it 5 when going through it doesn't print because it is already greater. 
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

#Off by one error condition met 
marshmallows = 0
while marshmallows < 10:
     marshmallows += 1
     print("there are now ", marshmallows, "in the bag")
   

#The count controls the amount of times the print statement will run before the break stops the code. 
count = 0
while True:
    print("Inside the infinite loop statement.")
    count += 1
    if count >= 5:
        break
    print("Natural Termination")
    

#Combining conditions using OR create more variation. When trying to use AND there were no true outputs
chocolate = 10
while marshmallows > 1 or chocolate < 9:
    print("I have ", marshmallows, "and ", chocolate)
    marshmallows -= 1
    chocolate += 1

# This loops is looking for all numbers below 5. Once 5 is hit the else clause states we've reach too many apples and the loop stops. 
apples = 0
while apples < 5:
    apples += 1
    print(apples, "is not too many apples")
else:
    print(apples, "is too many apples")


#The loop break stops the loop from running indefinitely. Without the break the code will continue to run because the condition of greater than 0 will always be met. 
time = 1
while time > 0:
    print("It is", time, "o'clock")
    time += 1
    if time == 10:
        break


# The continue tells the code to ignore the condition set.
no_threes = 0
while no_threes < 10:
    no_threes += 1
    if no_threes % 3 == 0:
        continue
    print(no_threes)


# If I did not figure out what I wanted to write yet for the code above I would use the pass statement so that I can continue writing code without errors. 
while no_threes < 10:
    pass


# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")


human_roll = input()
computer_roll = random.randint(1, 6)
print(computer_roll)
if human_roll == computer_roll:
    print("You guessed correctly")
else:
    print("You guessed incorrectly")


cards = ["Hearts", "Spades", "Clubs", "Diamonds"]
for card in range(5):
    random.shuffle(cards)
    print(cards)
    

human_guess = int(input("Pick a number between 1-10 "))
computer_guess = random.randint(1, 10)
if human_guess == computer_roll:
    print("You guessed correctly")
elif human_guess > computer_roll:
    print("Your guess is too high")
else:
    print("You guessed is too low")


advice = ["Always go with you first instinct", "Go for a walk and at the end the answer will be clear", "It's never too late to start over"]
question = input("How can the magic ball help? ")
response = random.choice(advice)
print(response)


suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
player_guess = input("Guess the suit ")
suit_guess = random.choice(suit)
if suit_guess == player_guess:
    print("You got it right!")
else:
    print("Sorry you guessed wrong")


# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track number
track_number = 1

# Spinning through the genres
for genre in genres:
    print(f"Track {track_number}: Now playing {genre}")
    track_number += 1


# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track


# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'


# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track


# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)


# List comprehension to append "Music" to each genre
music_genres = [genre + " Music" for genre in genres]
print(music_genres)


# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")