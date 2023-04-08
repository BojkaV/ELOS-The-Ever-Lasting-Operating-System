from time import sleep
import platform
import os

if platform.system() == 'Windows':
    clear = "cls"
    os.system(clear)
else:
    clear = 'clear'
    os.system(clear)

print("ELOS is starting...")
sleep(3)

os.system(clear)

def ELOS():
    print("ELOS 1 [Build 4] Ever Lasting Project")
    print("(C) ELP ELOS License")

    while True:
        commands = ['help', 'shutdown', 'info', 'clear', 'logout']
        com = input('> ')
        if com.lower() not in commands:
            print('Invalid Command')
        if com.lower() == 'help':
            print('Here are all available commands:')
            print('help - lists all available commands')
            print('shutdown - shuts down ELOS')
            print('info - shows information about ELOS')
            print('clear - clears the contents of the terminal')
            print('logout - prompts you to login')
        if com.lower() == 'shutdown':
            os.system(clear)
            print('ELOS is shutting down...')
            sleep(3)
            os.system(clear)
            exit()
        if com.lower() == 'info':
            print("ELOS 1 [Build 3] Ever Lasting Project")
            print("(C) ELP ELOS License")
        if com.lower() == 'clear':
            os.system(clear)
        if com.lower() == 'logout':
            os.system(clear)
            login()

def login():
    while True:
        print('Type password to login')
        print('Type exit to exit')
        passwd = input('Password: ')
        f = open('reg/password', 'r')
        if passwd == f.read():
            os.system(clear)
            ELOS()
        elif passwd == 'exit':
            os.system(clear)
            exit()
        else:
            print('Invalid Password')

login()