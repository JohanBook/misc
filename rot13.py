"""
CLI for ROT13 encryption/decryption.
"""

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = LETTERS.upper()


def _crypt_char(char: str, shift: int):
    if char in LETTERS:
        index = (LETTERS.find(char) + shift) % len(LETTERS)
        return LETTERS[index]
    if char in UPPER_LETTERS:
        index = (UPPER_LETTERS.find(char) + shift) % len(LETTERS)
        return UPPER_LETTERS[index]
    return char


def caesar_crypt(message: str, shift: int):
    """
    Encrypt using a Caesar cipher with given shift. Non-standard alphabetic
    letters are conserved.
    """
    return "".join([_crypt_char(char, shift) for char in message])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt data with ROT13", add_help=True
    )
    parser.add_argument("data", type=str, help="textual data to encrypt/decrypt")

    command_group = parser.add_mutually_exclusive_group(required=True)
    command_group.add_argument(
        "-e",
        "--encrypt",
        default=False,
        action="store_true",
        help="encrypt supplied data",
    )
    command_group.add_argument(
        "-d",
        "--decrypt",
        default=False,
        action="store_true",
        help="decrypt supplied data",
    )

    args = parser.parse_args()

    message = args.data
    if args.encrypt:
        message = caesar_crypt(message, 13)
    elif args.decrypt:
        message = caesar_crypt(message, -13)
    print(message)
