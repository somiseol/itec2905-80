import re

def banner():
    """ display program name """
    message = "Somi's Awesome camelCase program"
    stars = "*" * len(message)

    print(f"\n{stars}\n{message}\n{stars}\n")

def instructions():
    """ display instructions """
    print("Enter a sentence and this program will convert it ot camelcase")

banner()
instructions()
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

# use .capitalize() next time
# error if trailing white space


print(new_phrase)
