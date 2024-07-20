import random

chars = '1234567890abcdefghijklmnopqrstuvwxyz'

print("Your password:")

password = ''
for x in range(6):
    password += random.choice(chars) #for loop iterates 6 times - the range - and adds from the chars

print(password)

translated_password = ''
def letter_to_numpad(letter):
    numpad_mapping = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    return numpad_mapping.get(letter.lower(), letter)

for letter in password:
    translated_password += letter_to_numpad(str(letter))

print("Your translated password is: " + translated_password)