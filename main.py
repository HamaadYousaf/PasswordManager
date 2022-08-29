from server import insert, get, update, delete


def addEntry():
    website = input("Enter the name of the website: \n")
    username = input("Enter username: \n")
    password = input("Enter password: \n")
    insert(website, username, password)


def updateEntry():
    website = input("Enter the name of the website: \n")
    username = input("Enter the new username: \n")
    password = input("Enter the new password: \n")
    update(website, username, password)


def deleteEntry():
    website = input("Enter the name of the website: \n")
    confirm = input(
        "\033[91m {}\033[00m" .format(f"Are you sure you want to delete all info for {website}? (y/n): \n"))
    if confirm == 'y':
        delete(website)


def showEntries():
    entries = get()

    if len(entries) == 0:
        print("No entries found")
    else:
        print(entries)


def main():
    options = {
        '1': addEntry,
        '2': updateEntry,
        '3': deleteEntry,
        '4': showEntries
    }

    val = input("What would you like to do?\n")
    while val != 'q':
        if not val or int(val) <= 0 or int(val) > 4:
            print("Invalid input")
        else:
            options[val]()

        val = input("What would you like to do?\n")


main()
