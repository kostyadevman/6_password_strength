import os
import re
import argparse
import getpass


def get_arguments():
    parser = argparse.ArgumentParser('Password strength')
    parser.add_argument(
        '-b',
        '--blacklist',
        type=str,
        help='file with most common passwords'
    )
    return parser.parse_args()


def get_blacklist(common_used_passwords_file):
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


def get_password_strength(password, blacklist):
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

    if blacklist and password not in blacklist:
        password_estimate += 4

    return password_estimate

if __name__ == '__main__':
    password_estimate = 0
    args = get_arguments()
    blacklist = get_blacklist(args.blacklist)
    password = getpass.getpass(prompt='Enter the password: ')
    password_estimate = get_password_strength(password, blacklist)
    print('Password estimate: ', password_estimate)
