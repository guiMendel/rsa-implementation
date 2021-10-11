import json

# Get the session key length as a fraction of n

# Get the key
with open("publicKey.json", "r") as keyFile:
    # Get n
    n, _ = json.loads(keyFile.read())

# Session key will be half the size of n
sessionKeyLength = n.bit_length() // 2
