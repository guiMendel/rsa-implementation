from os import remove
from src.oaep import sessionKeyLength
from random import randrange
import json


def generateSessionKey(_):
    # Generate a session key of the appropriate length
    sessionKey = randrange(2 ** (sessionKeyLength - 1), 2 ** sessionKeyLength)

    # Store it
    with open("sessionKey.json", "w") as file:
        file.write(json.dumps(sessionKey))


def eraseSessionKey(_):
    # Simply delete key file
    try:
        remove("sessionKey.json")
    except Exception as error:
        print(
            "Failed to end session: sessionKey.json not found, is a folder or is in use",
            error,
            sep="\n",
        )
