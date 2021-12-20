from secret import get_secret_key
from interface import delete_app, select_and_delete, menu, create, find, find_accounts, get, change_master

secret = get_secret_key()

passw = input('Password: ')

if passw != secret:
    print('Incorrect Password')
    exit()

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
        choice = menu()
    if choice == '2':
        find_accounts()
        choice = menu()
    if choice == '3':
        find()
        choice = menu()
    if choice == '4':
        get()
        choice = menu()
    if choice == '5':
        select_and_delete()
        choice = menu()
    if choice == '6':
        delete_app()
        choice = menu()
    if choice == '7':
        change_master()
        exit()
    else:
        choice = menu()
exit()