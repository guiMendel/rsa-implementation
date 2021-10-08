from argparse import ArgumentParser
from src.keyGenerator import generateKey
from src.cryptography import encrypt, decrypt

# Maps script mode to functionality
executionModes = {"gen_key": generateKey, "enc": encrypt, "dec": decrypt}


def get_args():
    """Read arguments from the command line."""
    parser = ArgumentParser("RSA algorithm implementation")

    parser.add_argument(
        "mode",
        choices=executionModes.keys(),
        help="What should the script mode of execution be",
    )

    parser.add_argument(
        "-c",
        "--content",
        help="When encrypting/decrypting, the target content",
    )

    args = parser.parse_args()
    return args


def main():
    # Get script arguments
    args = get_args()

    # Execute script mode
    executionModes[args.mode](args)


if __name__ == "__main__":
    main()
