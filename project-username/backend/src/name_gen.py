from itertools import combinations

import random

vowels = ['a', 'e', 'i', 'o', 'u']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def firstLetter_lastName(names):
    '''
    Generates a list of usernames by concatenating the first letter
    of a user's first name with letters in the user's last name.

    Arguments:
        names (list) - List indexed with the user's full name.
    
    Exceptions:
        InputError - names is empty
    
    Return Value:
        A list of possible usernames
    '''
    first_l = names[0][0].lower()
    last_name = names[-1].lower()
    if len(last_name) > 2:
        # Take the first 3 letters of the username.
        first_three_surname = last_name[:3]
        all_cons = True
        for char in first_three_surname:
            if char in vowels:
                all_cons = False
                break
        # If all_cons is still true, all 3 letters are consonants which is ugly.
        if all_cons is True:
            # Take the first 2 letters
            new_surname = first_three_surname[:2]
        else:
            # Otherwise, there is at least a vowel in the first_three_letters
            new_surname = first_three_surname
    else:
        # last name is 2 letters or less.
        new_surname = last_name

    username = first_l + new_surname

    return username

def add_number(username, inc_num):
    '''
    Adds a random number to the username.

    Arguments:
        username (string) - A generated username.
    
    Exceptions:
        InputError - username is empty
    
    Return Value:
        username + random number
    '''
    num = ""
    if inc_num.lower() == 'yes':
        num = random.randint(1, 1000)

    return username + str(num)

def add_specialChar(username, inc_sChar):
    '''
    Adds a random special character to the username.

    Arguments:
        username (string) - A generated username.
    
    Exceptions:
        InputError - username is empty
    
    Return Value:
        username + special character
    '''
    if inc_sChar.lower() == 'no':
        return username

    all_sChars = ['!', '#', '$', '%', '^', '&', '*', '(', '{', '[', '<', '_', '.', ',', '/', '?']

    selected = random.choice(all_sChars) 
    num = random.randint(1, 3)

    # Each sChar should have a special position to be inserted in.
    signs = ['!', '#', '$', '%', '*', '?', '.']
    if selected in signs:
        sChar = selected * num
        username = front_back_attach(sChar, username)
    
    # If an open bracket is selected, a closed bracket must be followed.
    brackets = ['(', '{', '[', '<', '/']
    elif selected in brackets:
        # First separate the number str from normal word str
        num_str = ""
        for char in username:
            if char in numbers:
                num_str += char
                # Remove the number from the username
                username.remove(char)
        # Then we RANDOMLY splice the word str
        spl_num = random.randint(0, len(username))

    # Separators split first name & last name.
    # separators = ['^', '&', '_', ',']
    # elif selected in separators:

    return username

# --------------------------------------------------------------------------------------- #
# ----------------------------- Helper Functions ---------------------------------------- #
# --------------------------------------------------------------------------------------- #
def front_back_attach(sChar, username):
    '''
    Attaches a string of special characters to the front and/or back of a username.
    '''
    new_uname = [
        sChar + username,
        sChar + username + sChar,
        username + sChar
    ]

    return random.choice(new_uname)

if __name__ == '__main__':
    # full_name is a list with each index containing a name.
    full_name = input('Enter your full name: ').split(" ")
    username = firstLetter_lastName(full_name)

    inc_num = input('Fancy a number? ')
    username = add_number(username, inc_num)

    inc_sChar = input('Any special characters? ')
    username = add_specialChar(username, inc_sChar)
    print(username)