import os
import sys
from string import punctuation
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits



MIN_PASS_LENGTH = 8
special_characters = set(punctuation)

def get_password_strength(password):
    pass_estimate = 0
    if password != '':
        pass_estimate += 1

    if len(password) < MIN_PASS_LENGTH:
        pass_estimate = 1
        return pass_estimate
    elif len(password) >= MIN_PASS_LENGTH:
        pass_estimate += 1


    if any(chracter.islower() for chracter in password) and \
        any (character.isupper() for character in password):
        pass_estimate += 1

    if any(character.isdigit() for character in password):
        pass_estimate += 1


    if any(character in special_characters for character in password):
        pass_estimate += 1




    # more than 2 identical characters
    identical_character_count = 0
    for char_iter in range(0,len(password)-2):
        if  password[char_iter] == password[char_iter+1] == password[char_iter+2]:
            identical_character_count += 1
    if identical_character_count == 0:
            pass_estimate += 1

    # more than 2 consecutive characters
    consecutive_character_count = 0
    for char_ite in range (0, len(password)-2):
        three_consec_char = password[char_ite:char_ite+3]
        if three_consec_char in ascii_lowercase and \
                three_consec_char in ascii_uppercase and \
                three_consec_char in digits:
            consecutive_character_count += 1
    if consecutive_character_count == 0:
        pass_estimate += 1


    # Commonly used passwords
    if os.path.exists('john.txt'):
        with open('john.txt', 'r') as input_file:
            common_used_passwords = input_file.read()
        if password in common_used_passwords:
            pass_estimate = 1
        else:
            pass_estimate += 1
    else:
        print('The file with commonly used passwords ("john.txt") doesn\'t exitst')
        return None


    return pass_estimate


if __name__ == '__main__':
    pass
    password = input("Enter the password: ")
    pass_estimate = get_password_strength(password)
    print('Password estimate: ', pass_estimate)


