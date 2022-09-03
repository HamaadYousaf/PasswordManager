import string
import secrets
import re


def genPassword():
    characters = string.ascii_letters + string.digits + "!@#?"

    password = ""
    while re.search('[0-9]', password) is None or re.search('[^a-zA-Z0-9]', password) is None:
        password = ""
        for _ in range(16):
            password += characters[secrets.randbelow(len(characters))]

    return password
