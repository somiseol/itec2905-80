import re

phrase = input("phrase: ")

# check if str is valid
if not re.fullmatch("^[a-zA-Z ]+$", phrase):
    print("invalid")
    quit()

phrase = phrase.lower()
new_phrase = ""

i = 0

# python reassigns i when using for loop !!!
while i < len(phrase):
    if phrase[i] == " ":
        new_phrase += phrase[i + 1].upper()
        i += 2
    else:
        new_phrase += phrase[i]
        i += 1

print(new_phrase)
