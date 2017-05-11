from sys import exit
import random

def forest():
    print "You entered into the forest."
    print "Here you see the cave and the hut."
    print "Which one would you prefer?"

    choice = raw_input("> ")

    if choice == "cave":
        print "You see a witcher in the cave."
        print "You can do: 1. Tell me fortunes, witcher! 2. Teleport me to the forest now! 3. Bit him!!!"

        choice = raw_input("> ")

        if choice == "1":
            print "You will be lucky guy! See you!"
            start()
        elif choice == "2":
            print "You are teleporting to forest now!"
            forest()
        elif choice == "3":
            print "You are bastard! Go to the hell!!!"
            dead("Justin Bieber sings songs forever!")
        else:
            print "Make your choice!"
            choice = raw_input("> ")
    elif choice == "hut":
        print "Here you can see a Cyclope."
        print "And you can: 1. Bit him to the eye! 2. Give him some meat. 3. Promote Amway!"
        choice = raw_input("> ")

        if choice == "1":
            print "He break your bones"
            dead("Welcome to hell")
        elif choice == "2":
            print "Nyam-Nyam"
            dead("Nyam-Nyam your legs.")
        elif choice == "3":
            print "He buy shampoo and Nyam-Nyam!"
            dead("Nyam-Nyam anyway. Ha-ha!")
        else:
            print "Make you choice!"
            choice = raw_input()
    else:
        print "Make your choice!"
        choice = raw_input("> ")

def lake():
    print "You fall into the lake."
    print "You have no choice and it would be random..."
    choice = random.randint(0, 1)
    if choice == 0:
        print "You have a trip to the HELL"
        dead("It's just Fortuna")
    elif choice == 1:
        print "Welcome to Poseidon!"
        print "Poseidon says: Hi! Maybe: 1. Boiyabes? 2. Oysters? or 3. Diving school?"
        choice = raw_input("> ")
        if choice == "1":
            print "He shred you into slices"
            dead("It's you wanted boiyabes!")
        elif choice == "2":
            print "He boiled you and put in the shell"
            dead("You are oyster now")
        elif choice == "3":
            print "He tie a stone to your legs"
            dead("Diving for ever")
        else:
            dead("Anyway")
    else:
        dead("Anyway")

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in the forest."
    print "You can enter or get round."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "enter":
        forest()
    elif choice == "get round":
        lake()
    else:
        dead("You stumble around the room until you starve.")


start()
