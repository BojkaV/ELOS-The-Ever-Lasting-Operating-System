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

print("ELOS 1 [Build 3] Ever Lasting Project")
print("(C) ELP ELOS License")

while True:
    commands = ['help', 'shutdown', 'info', 'clear']
    com = input('> ')
    if com.lower() not in commands:
        print('Invalid Command')
    if com.lower() == 'help':
        print('Here are all available commands:')
        print('help - lists all available commands')
        print('shutdown - shuts down ELOS')
        print('info - shows information about ELOS')
        print('clear - clears the contents of the terminal')
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

sleep(3)

