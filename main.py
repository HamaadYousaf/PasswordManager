import os
from dotenv import load_dotenv
from server import insert, get, update, delete
from genPassword import genPassword
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from cryptography.fernet import Fernet
import pyperclip

load_dotenv()
console = Console()
key = os.getenv("KEY").encode()
f = Fernet(key)


def addEntry():
    website = input("Enter the name of the website: \n")
    username = input("Enter username: \n")
    genPass = input("Would you like to generate a password? (y/n) \n")
    if genPass == 'y':
        password = genPassword()
        print(f"Generated password: {password}")
    else:
        password = input("Enter password: \n")

    pyperclip.copy(password)
    print('Password copied to clipboard')
    encrypted = f.encrypt(password.encode())
    insert(website, username, encrypted)


def updateEntry():
    website = input("Enter the name of the website: \n")
    username = input("Enter the new username: \n")
    genPass = input("Would you like to generate a password? (y/n) \n")
    if genPass == 'y':
        password = genPassword()
        print(f"Generated password: {password}")
    else:
        password = input("Enter the new password: \n")

    pyperclip.copy(password)
    print('Password copied to clipboard')
    encrypted = f.encrypt(password.encode())
    update(website, username, encrypted)


def deleteEntry():
    website = input("Enter the name of the website: \n")
    console.print(
        f"Are you sure you want to delete all info for {website}?", style="red bold")
    confirm = Prompt.ask("(y/n)")

    if confirm == 'y':
        delete(website)


def showEntries():
    entries = get()

    if len(entries) == 0:
        print("No entries found")
    else:
        table = Table(box=box.HORIZONTALS, padding=(0, 3), show_lines=True)
        table.add_column("Website", justify="center")
        table.add_column("Username", justify="center")
        table.add_column("Password", justify="center")

        for entry in entries:
            decrypted = f.decrypt(entry[3].encode())
            table.add_row(entry[1], entry[2], str(decrypted, 'utf8'))
        console.print(table)


def main():
    verify = Prompt.ask("Enter the master password to begin")
    while verify != os.getenv('MASTER_PASSWORD'):
        verify = Prompt.ask("Enter the master password to begin")

    print()
    print("---------------------MENU---------------------")
    print("1. Add an entry")
    print("2. Show all passwords")
    print("3. Update an entry")
    print("4. Delete an entry")
    print("0. Quit\n")
    print("Enter the number corresponding to the option.\n")

    options = {
        '1': addEntry,
        '2': showEntries,
        '3': updateEntry,
        '4': deleteEntry
    }

    val = Prompt.ask("What would you like to do?")
    while val != '0':
        if not val or int(val) <= 0 or int(val) > 4:
            print("Invalid input")
        else:
            options[val]()
            print()

        val = Prompt.ask("What would you like to do?")

    console.print("Goodbye!", style="bold")


main()
