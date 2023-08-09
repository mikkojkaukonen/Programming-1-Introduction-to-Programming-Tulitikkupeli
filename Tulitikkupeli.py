"""
COMP.CS.100  Tulitikkupeli

Pelissä on kaksi pelaajaa, jotka vuorotellen poistavat 21 tulitikun kasasta
1-3 tikkua. Se pelaaja joka poistaa viimeisen tikun on häviäjä.

Tekijä: Mikko Kaukonen
"""

def main():

    print("Game of sticks")

    STICKS_AT_BEGINNING = 21
    sticks_to_remove = int

    for sticks_to_remove in range(1, 4):

        while STICKS_AT_BEGINNING > 0:

            sticks_to_remove = \
                int(input("Player 1 enter how many sticks to remove: "))
            while sticks_to_remove < 1 or sticks_to_remove > 3:
                print("Must remove between 1-3 sticks!")
                sticks_to_remove = \
                    int(input("Player 1 enter how many sticks to remove: "))
                
            else:
                STICKS_AT_BEGINNING = STICKS_AT_BEGINNING - sticks_to_remove
                if STICKS_AT_BEGINNING <= 0:
                    print("Player 1 lost the game!")
                    break
                else:
                    print("There are", STICKS_AT_BEGINNING, "sticks left")


            sticks_to_remove = \
                int(input("Player 2 enter how many sticks to remove: "))
            while sticks_to_remove < 1 or sticks_to_remove > 3:
                print("Must remove between 1-3 sticks!")
                sticks_to_remove = \
                    int(input("Player 2 enter how many sticks to remove: "))
            else:
                    STICKS_AT_BEGINNING = \
                        STICKS_AT_BEGINNING - sticks_to_remove
                    if STICKS_AT_BEGINNING <= 0:
                        print("Player 2 lost the game!")
                        break
                    else:
                        print("There are", STICKS_AT_BEGINNING, "sticks left")


if __name__ == "__main__":
        main()