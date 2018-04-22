import os
from string import punctuation, digits
import re
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
        pass_estimate += 1

    if re.search('[A-ZА-Я]', password):
        pass_estimate += 1

    if re.search('[a-zа-я]', password):
        pass_estimate += 1

    if re.search('\d', password):
        pass_estimate += 2

    if any(char in special_characters for char in password):
        pass_estimate += 2

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
