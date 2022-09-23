import random
import string

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

passName = input("Note for password: ")

f = open("pass.txt", "a")
f.write(passName + " - " + part1 + "_" + part2 + part3 + "\n")
f.close
