import os
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


def is_password_length_good(password):
    min_pass_length = 8
    return len(password) > min_pass_length


def get_password_strength(password, dictionary):
    password_estimate = 0
    patterns = [
        '\d',
        '[a-zа-я]',
        '[A-ZА-Я]',
        '\W',
    ]

    for pattern in patterns:
        if re.search(pattern, password):
            password_estimate += 1

    if is_password_length_good(password):
        password_estimate += 2

    if dictionary and password not in dictionary:
        password_estimate += 4

    return password_estimate

if __name__ == '__main__':
    password_estimate = 0
    args = get_argument()
    dictionary = get_dictionary(args.dict)
    password = input("Enter the password: ")
    password_estimate = get_password_strength(password, dictionary)
    print('Password estimate: ', password_estimate)
