import os

def clear_screen():
    os.system('cls')

def get_option(prompt, options):
    print(prompt, options, end=" ")
    while True:
        option = input().upper()
        if option in options:
            return option
        else:
            print("Invalid option try again!")