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
        password = ""

        letterLarge = list(string.ascii_uppercase)
        letterSmall = list(string.ascii_lowercase)
        number = list(string.digits)

        for i in range(3):
                password += random.choice(letterLarge)

        password += "_"

        for i in range(4):
                password += random.choice(letterSmall)

        for i in range(4):
                password += random.choice(number)

        print("\n Password: " + passName + " - " + password)

        f = open("pass.txt", "a")
        f.write(passName + " - " + password + "\n")
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
            print(" [3] Generate key")
            print(" [4] Delete key")

    print()
    menu()

    option = int(input("\n Choose option: "))
    
    if option == 1:

        passList = "pass.txt"
        
        if os.path.exists("key.key") is True:
                
                key = Fernet.generate_key()
                                
                with open(passList, "rb") as theFile:
                        contents = theFile.read()
                
                contents_encrypted = Fernet(key).encrypt(contents)
                
                with open(passList, "wb") as theFile:
                        theFile.write(contents_encrypted)
                
                print("\n Encrypting...")
        else:
                print("\n Key is missing!")

        input("\n Press any key to exit...")


    elif option == 2:

        print("\n Decrypting...")

        passList = "pass.txt"
        
        if os.path.exists("key.key") is True:

                key = Fernet.generate_key()

                with open("key.key", "rb") as key:
                        decryptKey = key.read()

                with open(passList, "rb") as theFile:
                        contents = theFile.read()
                
                contents_decrypted = Fernet(decryptKey).decrypt(contents)
                
                with open(passList, "wb") as theFile:
                        theFile.write(contents_decrypted)
        
        else:
                print("\n Key is missing!")

        input("\n Press any key to exit...")

    elif option == 3:
        
        key = Fernet.generate_key()
        
        with open("key.key", "wb") as theKey:
                        theKey.write(key)

        print("\n Generating key... \n")

    elif option == 4:
        
        os.remove("key.key")

    else:
        input("\n Press any key to exit...")

else:
    input("\n Press any key to exit...")
