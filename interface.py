from secret import get_secret_key
from pw_hash import password
import subprocess 
from pw_database import delete_account, delete, insert_pw, find_users, find_password, get_all
import pyperclip

def menu():
    print(('-'*13) + ' Options ' + ('-' *13))
    print('1. Create new password')
    print('2. Get all accounts connected to an email')
    print('3. Get an account for a specific app')
    print('4. Get all saved accounts')
    print('5. Select and delete an account')
    print('6. Delete saved password for a specific app')
    print('7. Change Password')
    print('Q. Exit')
    print('-'*35)
    return input('-> ')

def create():
    print('Please provide the name of the app you want to generate and save a password for: ')
    app = input()
    print('Please provide a password for this site: ')
    plaintext = input()
    passw0rd = password(plaintext, app, 12)
    pyperclip.copy(passw0rd)
    print('-'*30)
    print('')
    print('Your password has been created and saved to your clipboard')
    print('')
    print('-' *30)
    print('Please provide an email for this app or site:' )
    email = input()
    print('Please provide a username for this app or site (optional): ')
    username = input()
    if username == None:
        username = ''
    print('Please paste the url to the site that you are creating the password for (optional): ')
    url = input()
    insert_pw(app, username, email, passw0rd, url)
    print('Account added successfully')

def find():
    print('Please provide the name of the app you want to find the password to: ')
    app = input()
    find_password(app)

def find_accounts():
    print('Please provide the email that you want to find accounts for: ')
    email = input() 
    find_users(email)

def delete_app():
    print('Please provide the name of the site or app you want to delete: ')
    app = input()
    delete_account(app)

def get():
    get_all()

def change_master():
    secret = get_secret_key()
    print('Current Password: ')
    curr = input()
    if curr == secret:
        print('New Password: ')
        new = input()
        with open('secret.py', 'r') as file:
            filedata = file.read()

        filedata = filedata.replace(curr, new)

        with open('secret.py', 'w') as file:
            file.write(filedata)

        print('Password Changed Successfully')
    else:
        print('Incorrect Password')
         
def select_and_delete():
    delete()