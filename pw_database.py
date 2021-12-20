import psycopg2

def insert_pw(app, username, email, password, url):
    try:
        connection = psycopg2.connect(user='soham', password='soham', host='127.0.0.1', database='password_manager')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts"""
        cursor.execute(postgres_select_query)
        id = cursor.rowcount + 1
        postgres_insert_query = """ INSERT INTO accounts (app, username, email, password, url, id) VALUES (%s, %s, %s, %s, %s, %s)"""
        record_to_insert = (app, username, email, password, url, id)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_password(app):
    try:
        connection = psycopg2.connect(user='soham', password='soham', host='127.0.0.1', database='password_manager')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE app = '""" + app + "'"
        cursor.execute(postgres_select_query, app)
        if cursor.rowcount == 0:
            print('No accounts with app name ' + app + ' exist')
        else:
            connection.commit()
            result = cursor.fetchone()
            print('Password is: ' )
            print(result[0])
            print('')
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_users(email):
    data = ('App: ', 'Username: ', 'Email: ', 'Password: ', 'URL: ') 
    try:
        connection = psycopg2.connect(user='soham', password='soham', host='127.0.0.1', database='password_manager')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts WHERE email = '""" + email + "'"
        cursor.execute(postgres_select_query, email)
        if cursor.rowcount == 0:
            print('No accounts with email ' + email + ' exist')
        else:
            connection.commit()
            result = cursor.fetchall()
            print('')
            print('RESULT')
            print('')
            for row in result:
                for i in range(0, len(row)):
                    print(data[i] + row[i])
            print('')
    except (Exception, psycopg2.Error) as error:
        print(error)

def delete_account(app):
    try:
        connection = psycopg2.connect(user='soham', password='soham', host='127.0.0.1', database='password_manager')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE app = '""" + app + "'"
        cursor.execute(postgres_select_query, app)
        if cursor.rowcount == 0:
            print(app + ' does not exist')
        else:
            postgres_select_query = """ DELETE FROM accounts WHERE app = '""" + app + "'"
            cursor.execute(postgres_select_query, app)
            connection.commit()
            print('Deleted successfully')
            print('')
    except (Exception, psycopg2.Error) as error:
        print(error)

def get_all():
    data = ('App: ', 'Username: ', 'Email: ', 'Password: ', 'URL: ') 
    try:
        connection = psycopg2.connect(user='soham', password='soham', host='127.0.0.1', database='password_manager')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts"""
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            print(row[5])
            for i in range(0, len(row) - 1):
                print(data[i] + row[i])
            print('\n')
    except (Exception, psycopg2.Error) as error:
        print(error)

def delete():
    get_all()
    print('Please provide the number of the corresponding account you want to delete')
    id = input()
    try:
        connection = psycopg2.connect(user='soham', password='soham', host='127.0.0.1', database='password_manager')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE id = '""" + id + "'"
        cursor.execute(postgres_select_query, id)
        if cursor.rowcount == 0:
            print('Account #' + id + ' does not exist')
        else:
            postgres_select_query = """ DELETE FROM accounts WHERE id = '""" + id + "'"
            cursor.execute(postgres_select_query, id)
            connection.commit()
            
            postgres_select_query = """ SELECT * FROM accounts"""
            cursor.execute(postgres_select_query)
            connection.commit()
            result = cursor.fetchall()
            for row in result:
                if(row[5] > int(id)):
                    postgres_select_query = """ UPDATE accounts SET id = """ + str(row[5] - 1) + """ WHERE id = """ + str(row[5]) + """ """
                    cursor.execute(postgres_select_query, id)
                    connection.commit()

            print('Deleted successfully')
            print('')
    except (Exception, psycopg2.Error) as error:
        print(error)