from cryptography import fernet
import random
import string
import os

print(
 "\n _____         _____ _____  _____ ______ _   _\n"
 "|  __ \ /\    / ____/ ____|/ ____|  ____| \ | |\n"
 "| |__) /  \  | (___| (___ | |  __| |__  |  \| |\n"
 "|  ___/ /\ \  \___ \\___  \| | |_ |  __| | . ` |\n"
 "| |  / ____ \ ____) |___) | |__| | |____| |\  |\n"
 "|_| /_/    \_\_____/_____/ \_____|______|_| \_|\n"
 "\n-------------------------------------------------\n"                                               
)

def menu ():
    print("[1] Create new list")
    print("[2] Delete list")
print()
menu()

option = int(input("\nChoose option: "))
while option != 0:
    if option == 1:
        passName = input("Note for password: ") 
        letterLarge = list(string.ascii_uppercase)
        letterSmall = list(string.ascii_lowercase)
        number = list(string.digits)

        first1 = random.choice(letterLarge)
        first2 = random.choice(letterLarge)
        first3 = random.choice(letterLarge)

        part1 = first1 + first2 + first3

        second1 = random.choice(letterSmall)
        second2 = random.choice(letterSmall)
        second3 = random.choice(letterSmall)
        second4 = random.choice(letterSmall)

        part2 = second1 + second2 + second3 + second4

        third1 = random.choice(number)
        third2 = random.choice(number)
        third3 = random.choice(number)
        third4 = random.choice(number)

        part3 = third1 + third2 + third3 + third4

        f = open("pass.txt", "a")
        f.write(passName + " - " + part1 + "_" + part2 + part3 + "\n")
        f.close
    
    elif option == 2:
        os.remove('pass.txt')
        



#################################################################
