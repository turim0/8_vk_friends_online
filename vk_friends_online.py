import vk
import getpass
import os


APP_ID = 6871675
API_VERSION = 5.92


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass.getpass('Password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=API_VERSION)
    return api.users.get(user_ids=api.friends.getOnline())


def output_friends_to_console(friends_online):
    print("You have {} friend(s) online".format(len(friends_online)))
    for friend in friends_online:
        print("id{id} - {first_name} {last_name}".format(**friend))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
