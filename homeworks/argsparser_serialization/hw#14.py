import argparse
import json


def create_file():
    file = open("users_data.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("users_data.json", 'r')


def user_add(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="person_username")
    parser.add_argument("-s", "--status", help="person_status")
    parser.add_argument("-e", "--email", help="person_email")
    args = parser.parse_args()

    try:
        users['username'] = args.username
        users['email'] = args.email
        users['status'] = args.status
    except IndexError:
        raise Exception('U wrote wrong person info')


def check_user_exists(users_data, user):
    for users in users_data:
        if user['username'] == users['username'] or \
                user['email'] == users['email']:
            return True

    return False


def add_user(user):
    try:
        read_file = open('users_data.json', 'r')
    except FileNotFoundError:
        read_file = create_file()

    try:
        users_data = json.loads(read_file.read())
    except ValueError:
        with open('users_data.json', "w") as write_file:
            write_file.write(json.dumps([]))
        users_data = []
    read_file.close()

    if not check_user_exists(users_data, user):
        users_data.append(user)
        with open('users_data.json', 'w') as write_file:
            write_file.write(json.dumps(users_data, indent=4, sort_keys=True))
    else:
        raise "User with username or email already exist"


if __name__ == "__main__":
    new_user = {}
    user_add(new_user)
    add_user(new_user)
