import json
from src.oaep import oaepPad, oaepUnpad


def encrypt(args):
    # Make sure content was provided
    if args.content is None:
        raise ValueError("Encryption needs content")

    # Get the key
    with open("publicKey.json", "r") as keyFile:
        publicKey = json.loads(keyFile.read())

        # Get e and n
        n, e = publicKey

    # Convert content to number
    messageBytes = args.content.encode("utf-8")
    messageNumber = int.from_bytes(messageBytes, "little")

    # Apply oaep
    paddedMessageNumber, padLength = oaepPad(messageNumber)

    # Apply exponentiation
    cypher = pow(paddedMessageNumber, e, n)

    # Save it
    with open("cypher.json", "w") as cypherFile:
        cypherFile.write(json.dumps((str(cypher), padLength)))


def decrypt(args):
    # Get the key
    with open("privateKey.json", "r") as keyFile:
        privateKey = json.loads(keyFile.read())

        # Get e and n
        n, d = privateKey

    # Get cypher and padLength
    with open("cypher.json", "r") as cypherFile:
        content, padLength = json.loads(cypherFile.read())

    # Convert content to number
    paddedCypher = int(content)

    # Apply exponentiation
    paddedMessageNumber = pow(paddedCypher, d, n)

    # Unpad it
    messageNumber = oaepUnpad(paddedMessageNumber, padLength)

    # Turn message back to string
    messageBytes = messageNumber.to_bytes(
        (messageNumber.bit_length() + 7) // 8, "little"
    )
    message = messageBytes.decode("utf-8")

    # Save it
    with open("message.txt", "w") as messageFile:
        messageFile.write(str(message))
