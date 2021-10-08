import json


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

    # Apply exponentiation
    cypher = pow(messageNumber, e, n)

    # Save it
    with open("cypher.txt", "w") as cypherFile:
        cypherFile.write(str(cypher))


def decrypt(args):
    # Make sure content was provided
    if args.content is None:
        raise ValueError("Decryption needs content")

    # Get the key
    with open("privateKey.json", "r") as keyFile:
        privateKey = json.loads(keyFile.read())

        # Get e and n
        n, d = privateKey

    # Convert content to number
    cypher = int(args.content)

    # Apply exponentiation
    messageNumber = pow(cypher, d, n)

    # Turn message back to string
    messageBytes = messageNumber.to_bytes(
        (messageNumber.bit_length() + 7) // 8, "little"
    )
    message = messageBytes.decode("utf-8")

    # Save it
    with open("message.txt", "w") as messageFile:
        messageFile.write(str(message))
