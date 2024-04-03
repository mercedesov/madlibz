import random

def custom_int(number: str):
	numbers = "0123456789"
	
	for i in range(10):
		if number == numbers[i]:
			return i;

print("To choose the story to play the game please type 1-3 or type 4 for a random story")
a = input("Type a number 1-4: ")
a = custom_int(a)

if a == 4:
    a = random.randint(1, 3)

if a == 1:
    number = input("Input a number:")
    time_measure = input("Input a measure of time:")
    transportation_mode = input("Input a mode of transportation:")
    adjective1 = input("Input an adjective:")
    adjective2 = input("Input another adjective:")
    noun1 = input("Input a noun:")
    color = input("Input a color:")
    body_part = input("Input a part of the body:")
    verb = input("Input a verb:")
    number2 = input("Input a number:")
    noun2 = input("Input a noun:")
    noun3 = input("Input a noun:")
    body_part2 = input("Input a part of the body:")
    verb2 = input("Input a verb:")
    noun4 = input("Input a noun:")
    adjective3 = input("Input an adjective:")
    silly_word = input("Input a silly word:")
    noun5 = input("Input a noun:")

    print(f"It was about {number} {time_measure} ago when I arrived at the hospital in a {transportation_mode}. The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here. There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!")

elif a == 2:
    person_name = input("Input a proper noun (person's name):")
    noun = input("Input a noun:")
    adjective_feeling = input("Input an adjective (feeling):")
    verb = input("Input a verb:")
    adjective_feeling2 = input("Input another adjective (feeling):")
    animal = input("Input an animal:")
    verb2 = input("Input a verb:")
    color = input("Input a color:")
    verb_ing = input("Input a verb (ending in ing):")
    adverb = input("Input an adverb (ending in ly):")
    number = input("Input a number:")
    time_measure = input("Input a measure of time:")
    color2 = input("Input a color:")
    animal2 = input("Input an animal:")
    number2 = input("Input a number:")
    silly_word = input("Input a silly word:")
    noun2 = input("Input a noun:")

    print(f"This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective_feeling} to {verb} in a tent. I am {adjective_feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ing}. Then we will {adverb} hike through the forest for {number} {time_measure}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!")

elif a == 3:
    person_name = input("Input a proper noun (person's name):")
    adjective = input("Input an adjective:")
    color = input("Input a color:")
    animal = input("Input an animal:")
    place = input("Input a place:")
    adjective2 = input("Input another adjective:")
    magical_creature_plural = input("Input a magical creature (plural):")
    adjective3 = input("Input another adjective:")
    magical_creature_plural2 = input("Input another magical creature (plural):")
    room_in_a_house = input("Input a room in a house:")
    noun = input("Input a noun:")
    noun2 = input("Input a noun:")
    plural_noun3 = input("Input a plural noun:")
    adjective4 = input("Input an adjective:")
    plural_noun4 = input("Input a plural noun:")
    number = input("Input a number:")
    time_measure = input("Input a measure of time:")
    verb_ing = input("Input a verb ending in ing:")
    adjective5 = input("Input an adjective:")
    noun5 = input("Input a noun:")
    
    print(f"Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature_plural} and {adjective3} {magical_creature_plural2} here! In the {room_in_a_house} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {plural_noun3} and dream of {adjective4} {plural_noun4}. It feels as though I have lived here for {number} {time_measure}. I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!")