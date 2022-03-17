
def main():
    print("Welcome to the Game")

    PlayerName=input("what is your name? ")
    print(f"Hello " + PlayerName)

    lives = 3
    print(f"You have {lives } Remaining lives")

    backpack = [] # initialise empty list for backpack

    print("you awake in a room to your front is a Blue door, to your right is a Red door, to left is a Green door and behind you there is a Black Door. \nOn the floor in front of you, there is a note ! it read \n( welcome to My game, you need to complete four puzzles and collect there Key to escape. Be aware of hidden threats!) ") 
    print("Upon looking around this central room again you find a backpack and put it on,\n you also notice door like shape in the corner of the room, it has four key like hole init.   ")  

    while True:
        direction = input("Which room do you want to try? please choice from Red, Blue, Green or Black. ")    

        if direction == "Red":
                print("you entered the Red Room. ")
                puzzle_guess_Red = input("What is 2 + 2? ")
                if puzzle_guess_Red == "4":
                        print("correct")
                        # We need to collect Something here - i.e add to Backpack
                        backpack.append("key 1 collected")
                        print("Key 1 collected")
                else:
                        print("Incorrect")
                        lives -= 1
                        print(f"You have {lives} lives remaining.")
        elif direction == "Blue":
                print("you entered the Blue Room. ")

        elif direction == "Green":
                print("you entered the Green Room. ")
        
        elif direction == "Black": 
                print("you entered the Black Room. ")
        else:
                print("Room not recognised!")   

        #if back pack is full, open door and win game.
        if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("key 4" in backpack):
                print(" you input the four keys into the strange door in the corner, it open and you see the outside, you run for freedom\n you escape! game over!!  ") 






main()
