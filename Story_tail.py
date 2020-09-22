while True:
    answer=input("what you like to play? (yes/no)").lower().strip()
    # ერთერთი ვარიაცია დაწერეს იმუშავებს
    if answer.lower().strip() == "yes":

        answer=input("you reach a crossroads, woul you like to left or right?").lower().strip()

        if answer=="left":
            answer=input("You encounter a monster, would you like to run or attack?").lower().strip()
            if answer =="attack":
                print("The was not the greates idea,you lost!")
            else:
                print("Good choice,you made it away safely.")
                answer==input("you see a car and a plane. which would you like to take?")
                if answer=="car":
                    print("you won!")

                else:
                    print("you won!")
        elif answer=="right":
            print("You walk aimlessly to the right and fall on a patch of ice. You inhure your leg and cannot continue. Game over")

        else:
            print("Invalid choice, you lost!")


    else:
        print("That's too bad! ")
        break
