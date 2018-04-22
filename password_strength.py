import os
from string import punctuation, digits
from string import ascii_lowercase, ascii_uppercase
import argparse


def get_argument():
    parser = argparse.ArgumentParser('Password strength')
    parser.add_argument('--dict', type=str)
    return parser.parse_args()


def get_dictionary(common_used_passwords_file):
    if not common_used_passwords_file:
        return None
    if not os.path.isfile(common_used_passwords_file):
        return None
    with open(common_used_passwords_file, 'r') as password_file:
        common_used_passwords = password_file.readlines()
    return common_used_passwords


def get_password_strength(password, common_used_passwords):
    min_pass_length = 8
    special_characters = set(punctuation)

    pass_estimate = 0
    if password != '':
        pass_estimate += 1

    if len(password) > min_pass_length:
        pass_estimate += 2

    if any(char.islower() for char in password) and \
        any(char.isupper() for char in password):
        pass_estimate += 1

    if any(char.isdigit() for char in password):
        pass_estimate += 1

    if any(char in special_characters for char in password):
        pass_estimate += 1

    # more than 2 identical characters
    identical_character_count = 0
    for char_number in range(len(password)-2):
        if (password[char_number] == password[char_number+1] ==
                password[char_number + 2]):
            identical_character_count += 1
    if identical_character_count == 0:
        pass_estimate += 1

    # more than 2 consecutive characters
    consecutive_character_count = 0
    for char_number in range(0, len(password)-2):
        three_consec_char = password[char_number:char_number + 3]
        if three_consec_char in ascii_lowercase or \
                three_consec_char in ascii_uppercase or \
                three_consec_char in digits:
            consecutive_character_count += 1
    if consecutive_character_count == 0:
        pass_estimate += 1

    if common_used_passwords:
        if password not in common_used_passwords:
            pass_estimate += 2

    return pass_estimate


if __name__ == '__main__':
    args = get_argument()
    print(args.dict)
    dictionary = get_dictionary(args.dict)
    password = input("Enter the password: ")
    pass_estimate = get_password_strength(password, dictionary)
    print('Password estimate: ', pass_estimate)
