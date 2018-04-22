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


def is_digit_in_password(password):
    return re.search('\d', password)


def is_lowcase_character_in_password(password):
    return re.search('[a-zа-я]', password)


def is_uppercase_character_in_password(password):
    return re.search('[A-ZА-Я]', password)


def is_special_character_in_password(password):
    return re.search('[!"#$%&()*+,-./:;<=>?@\^_`{|}~\'\]\[]', password)


def is_password_length_good(password):
    min_pass_length = 8
    return len(password) > min_pass_length


def is_password_in_dictionary(password, dictionary):
    return password in dictionary


if __name__ == '__main__':
    password_estimate = 0
    args = get_argument()
    dictionary = get_dictionary(args.dict)
    password = input("Enter the password: ")

    if is_lowcase_character_in_password(password):
        password_estimate += 1

    if is_uppercase_character_in_password(password):
        password_estimate += 1

    if is_digit_in_password(password):
        password_estimate += 2

    if is_password_length_good(password):
        password_estimate += 2

    if is_special_character_in_password(password):
        password_estimate += 2

    if dictionary:
        if is_password_in_dictionary(password, dictionary):
            password_estimate += 2


    print('Password estimate: ', password_estimate)
