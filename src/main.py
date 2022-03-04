
def main():
    print("Welcome to the Game")

    PlayerName=input("what is your name? ")
    print("Hello " + PlayerName)

    lives = 3
    print(f"You have {lives } Remaining lives")

    print("directions avilible north,south,east,west")
    TravelDirection=input("which direction would you like to go ?")

    if TravelDirection == "north":
            print("you went north")

    elif TravelDirection == "south":
            print("you went south")

    elif TravelDirection == "east":
            print("you when east")
        
    else:
            print("you went west")






main()
