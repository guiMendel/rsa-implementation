from argparse import ArgumentParser
from src.keyGenerator import generateKey

# Maps script mode to functionality
executionModes = {"gen_key": generateKey}


def get_args():
    """Read arguments from the command line."""
    parser = ArgumentParser("RSA algorithm implementation")
    parser.add_argument(
        "mode",
        choices=executionModes.keys(),
        help="What should the script mode of execution be",
    )

    args = parser.parse_args()
    return args


def main():
    # Get script arguments
    args = get_args()

    # Execute script mode
    executionModes[args.mode]()


if __name__ == "__main__":
    main()
