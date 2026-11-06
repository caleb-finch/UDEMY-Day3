print(r'''
*******************************************************************************
             ____ _____ ___     ____      _____ ____    _____ _ ___
            / __//____//__ \   /__  \    /____//__  \  /____//_X__/
           ( (    __   __| |   ___) /     __   ___) / ____  ___
            \ \  / / ,/,/| |  /   _/     / /  /   _/ / __/ / _ \
         ____) )/ /,/ /__| | / /\ \     / /  / /\ \ / /__ / / \ \
        /_____//_//________|/_/ /_/    /_/  /_/ /_//____//_/   \_\

  ___      _          _    ___     __   _       _  _  __  ___    __
   |  |_| |_    |\ | |_ \/  |     | _  |_ |\ | |_ |_)   |  |  | |  | |\ |
   |  | | |_    | \| |_ /\  |     |__| |_ | \| |_ | \ /_|  |  | |__| | \|
*******************************************************************************
''')
print("Welcome to Enterprise-D")
print("Your mission is to seek out new life and new civilizations.")
print("You are Captain Picard and you must make the decisions.")

choice = input("There is a blackhole in front of you. You must go either left or right. What do you choose?\n")

if choice == "left" or choice == "Left":
    print("Good move! You have move out of the way of danger. For now....")

else:
    print("You turned into a large army of Romulans. They begin to fire and destroy your ship. You are dead!")


choice = input("Your ship has been encountered an unknown planet. Would you like to send an away team to check it out?\n")

if choice == "yes" or choice == "Yes":
    print("You sent an away team to check it out. Worf and Riker discover a new civilization just post-Bronze age! This will be an amazing new discovery.")

else:
    print("You missed a huge discovery. You will never feel okay with yourself...")

choice = input("This new planet has some major shifts in their tectonic plates. They will not be able to survive without your help. What do you do? Wait, Intervene, or Nothing\n")

if choice == "Wait" or choice == "wait":
    print("You chose to wait and the civilization died as the result :(")

elif choice == "Nothing" or choice == "nothing":
    print("You chose nothing. This is NOT the Picard way. You die from confusion.")

else:
    print("You have chosen to help, breaking the Prime Directive, but saving the civiilization in the process. This is the correct choice as Picard!!")