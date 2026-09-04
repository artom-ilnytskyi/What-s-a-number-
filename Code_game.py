import random
Players_try = 0
Player_choice = None
Computer_variant = random.randint(1, 100)
while Player_choice != Computer_variant:
    Player_choice = input("chose a number 1-100: ")
    if not Player_choice.isdigit():
        print("please write a number 1-100")
        print("won't use numbers like 1.02")
        print("or words")
        continue
    Number = int(Player_choice)
    if not ( 1 <= Number <= 100 ):
        print (" you choose bigger than 100")
        print("please chose 1-100")
        continue
    if Number < Computer_variant:
            print("more")
            Players_try += 1
    elif Number > Computer_variant:
            print("less")
            Players_try += 1
    if Number == Computer_variant:
            print("you make it congratulations 👏")
            Players_try += 1
            print(Players_try)
            break
