import json
import hashlib

# Get the session key length as a fraction of n

# Get the key
with open("publicKey.json", "r") as keyFile:
    # Get n
    n, _ = json.loads(keyFile.read())

# Session key will be half the size of n
sessionKeyLength = int(n.bit_length() // 2)

# Get X size
xLength = n.bit_length() - sessionKeyLength

# Get G and H
G = lambda input: mgf1(input, xLength)
H = lambda input: mgf1(input, sessionKeyLength)


def toBinary(value):
    if value == "":
        return None

    try:
        return bin(value)[2:]
    # If is bytes, convert to int first
    except TypeError:
        return bin(int.from_bytes(value, "little"))[2:]


def zeroPad(message, length):
    """Convert the message to a binary string then pad it with 0s until it's length is n - sessionKeyLength"""
    # Convert to to binary (exclude first two characters which will always be '0b')
    binaryMessage = toBinary(message)

    # Get padding length
    padLength = length - len(binaryMessage)

    # Pad it
    return (binaryMessage + ("0" * padLength), padLength)


def xor(bits1, bits2):
    """Applies xor to the given bit strings"""
    return "".join([str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(bits1, bits2)])


def i2osp(integer):
    return "".join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(4))])


def mgf1(input, length):
    """Mask generation function"""
    counter = 0
    output = ""

    while len(output) < length:
        C = i2osp(counter)
        output += toBinary(hashlib.sha256((input + C).encode()).digest())
        counter += 1

    return output[:length]


def oaepPad(message):
    """Applies oaep padding to the given message"""
    # Get session key
    with open("sessionKey.json", "r") as keyFile:
        sessionKey = toBinary(json.loads(keyFile.read()))

    # Zero pad
    binaryMessage, padLength = zeroPad(message, xLength)

    # Get X
    X = xor(binaryMessage, G(sessionKey))

    # Get Y
    Y = xor(sessionKey, H(X))

    # Convert from binary to int
    result = int(X + Y, 2)

    return (result, padLength)


def oaepUnpad(paddedMessage, padLength):
    """Removes the application of oaep from a paddedMessage"""
    binaryPaddedMessage = toBinary(paddedMessage)

    # Make sure it totals n length
    binaryPaddedMessage = '0' * (n.bit_length() - len(binaryPaddedMessage)) + binaryPaddedMessage

    # Get X and Y back
    X, Y = (
        binaryPaddedMessage[:-sessionKeyLength],
        binaryPaddedMessage[-sessionKeyLength:],
    )

    # Get session key back
    sessionKey = xor(Y, H(X))

    # Get message back
    binaryMessage = xor(X, G(sessionKey))

    # Remove 0 padding
    binaryMessage = binaryMessage[:-padLength]

    # Convert from binary to int
    return int(binaryMessage, 2)
