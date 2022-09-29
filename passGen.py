from cryptography.fernet import Fernet
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

def menu():
        print(" [1] Password")
        print(" [2] Encryption")
        print(" [0] Exit")
print()
menu()

option = int(input("\n Choose option: "))
if option == 1:
    def menu():
        print(" [1] Generate password")
        print(" [2] Delete password file")
        print(" [0] Exit")
    print()
    menu()
    option = int(input("\n Choose option: "))
    if option == 1:
        passName = input("\n Note for password: ") 

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

        print("\n Password: " + passName + " - " + part1 + "_" + part2 + part3)


        f = open("pass.txt", "a")
        f.write(passName + " - " + part1 + "_" + part2 + part3 + "\n")
        f.close

        input("\n Press any key to exit...")
    elif option == 2:
        os.remove("pass.txt")

    else:
        input("\n Press any key to exit...")

###########################################################
#                       DECRYPTION                        #
###########################################################

elif option == 2:
    def menu():
            print(" [1] Encrypt")
            print(" [2] Decrypt")
            print(" [3] Delete key")
    print()
    menu()

    option = int(input("\n Choose option: "))
    if option == 1:
        print("\n Encrypting...")

        passList = "pass.txt"

        key = Fernet.generate_key()

        with open("key.key", "wb") as theKey:
                theKey.write(key)

        with open(passList, "rb") as theFile:
                contents = theFile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(passList, "wb") as theFile:
                theFile.write(contents_encrypted)

        input("\n Press any key to exit...")


    elif option == 2:
        print("\n Decrypting...")

        passList = "pass.txt"

        with open("key.key", "rb") as key:
                decryptKey = key.read()

        with open(passList, "rb") as theFile:
                contents = theFile.read()
        contents_decrypted = Fernet(decryptKey).decrypt(contents)
        with open(passList, "wb") as theFile:
                theFile.write(contents_decrypted)

        input("\n Press any key to exit...")

    elif option == 3:
        os.remove("key.key")
    else:
        input("\n Press any key to exit...")
else:
    input("\n Press any key to exit...")
