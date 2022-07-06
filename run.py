import random


def guess_number():
    random_number = random.randint(1, 3)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number betwwen 1 and 3: \n"))
        if guess != random_number:
            print("Sorry! You lost")
            break
        else:
            print(f"Congradulations!You've guesed the number{random_number}!")
            print("You get acces to the next level")
            print("The Kingdom's gates are opening...")
            break


def mad_lib():
    print("Oh no! He fell down in the well")
    print("A scared magic frog transforms him in a fly to eat him")
    print("He escapes the well but as fly has one day to live")
    print("Help the prince to break out the spell and become human again")
    magic_word = input("Magic word: \n").lower().capitalize()
    adj = input("Adjective: \n").lower()
    spell = f"{magic_word}! Shall the {adj} spirit transform me back to human!"
    print(spell)
    print("Looking handsome again!")


def yes_or_no():
    while True:
        choice = input("Type in: yes/ no: \n").lower().split()
        if choice == "yes":
            last_round()
        elif choice == "no":
            mad_lib()
            break
        else:
            input("Please type in correctly: \n").lower()
            break


def intro():
    print("The story begins in ancient times")
    print("There was Green Emperor, rulling over The Edge Of The World")
    print("He had one doughter and no son to inherit his kongdom")
    print("'But his brother had two boys!'")
    round_one()


def round_one():
    print("Choose which one of them should go and merry")
    while True:
        choice = input("Type in: oldest / youngest: \n").lower()
        if choice == "youngest":
            round_two()
        elif choice == "oldest":
            print("After long journey he stopped to drink water")
            mad_lib()
            last_round()
            break
        else:
            input("Please type in correctly: \n").lower()


def round_two():
    print("An old woman advices the young man")
    print("to ask his father for his horse and his sword")
    print("The king offeres him to choose between the two of them")
    while True:
        choice = input("Type in horse / sword: \n").lower()
        if choice == "horse":
            round_three()
        elif choice == "sword":
            print("Dressed in a bear fur the king put his son to test")
            print("The prince took out his sword and fought.")
            print("Unfortunately he got a wound and had to come back home")
            print("GAME OVER!")
            break
        else:
            input("Please type in correctly: \n").lower()


def round_three():
    print("Dressed in a bear fur the king put his son to test")
    print("The horse is able to fly and avoid the confrontation")
    print("On the road he meets the Sparrow and the Redman")
    print("Which one of them should become the prince slave?")
    while True:
        choice = input("Type sparrow / redman: \n").lower()
        if choice == "sparrow":
            print("They wonder for long time until the Sparrow")
            print("tricks the boy to go down to a well to cool off")
            print("To spare his life, the Sparrow forces him to obey him")
            yes_or_no()
            last_round()
        elif choice == "redman":
            print("Redman, an evel wisard transforms the Prince into a fly")
            mad_lib()
            last_round()
        else:
            input("Please type in correctly \n").lower()


def last_round():
    print("After 3 months crossing the mountains and the seas ")
    print("he is finally in front of the kingdom's gate")
    print("To open it he need to guess a number between 1 and 3")
    guess_number()


round_one()
