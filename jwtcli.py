"""
CLI for inspecting JWT tokens.

Some commands requires `pyjwt` to be installed.
"""
import base64
import json
import re

JWT_REGEXP = re.compile("(^[\w-]*\.[\w-]*\.[\w-]*$)")


def read_file(filepath):
    try:
        content = open(filepath, "r").read()
        return content.replace("\n", "")
    except:
        raise Exception(f"Unable to open file '{filepath}'")


def is_jwt(token):
    return JWT_REGEXP.search(token)


def get_jwt_from_file(filepath):
    token = read_file(filepath)
    if not is_jwt(token):
        raise Exception(f"Is'{token}' is not a valid JWT")
    return token


def decode_base64(data):
    # Add extra padding to avoid `Incorrect padding` error
    data = data.lstrip() + "======"
    return base64.b64decode(data)


def parse_token(token):
    [header, body, _] = token.split(".")
    header = json.loads(decode_base64(header))
    body = json.loads(decode_base64(body))
    return [header, body]


def check_signature(token, secret, algorithm):
    import jwt

    try:
        jwt.decode(token, secret, algorithms=[algorithm])
        return True
    except jwt.DecodeError:
        return False
    except jwt.InvalidTokenError:
        return False


def check_signatures(token, signatures, algorithm):
    for signature in signatures:
        success = check_signature(token, signature, algorithm)
        print(f"x '{signature}'")
        if success:
            print(f"MATCH '{signature}'")
            return signature


def analyze(args):
    token = read_file(args.token)
    parts = token.split(".")
    print(f"FILE: {args.token}")
    print(f"PARTS: {len(parts)}")

    for index in range(len(parts)):
        part = parts[index]
        print(f"\nPART {index+1}/{len(parts)}")
        print(f"LENGTH: {len(part)}")
        try:
            decoded = decode_base64(part)
            print("-> Part was Base64 decoded")
        except:
            print("-> Failed to Base64 decode part")
            print(part)
            continue

        try:
            body = json.loads(decoded)
            print("-> Content is valid JSON")
            print(body)
            continue
        except:
            print("-> Content could not be parsed as JSON")

        try:
            body = decoded.decode("ascii")
            print("-> Could be ASCII decoded")
            print(body)
        except:
            print("-> Could not be ASCII decoded")
            print(decoded)


def crack(args):
    print(f"Trying to crack {args.token}")
    token = get_jwt_from_file(args.token)
    alg = parse_token(token)[0]["alg"]
    signatures = open(args.signatures, "r").read().split("\n")
    check_signatures(args.token, signatures, alg)


def inspect(args):
    token = get_jwt_from_file(args.token)
    [header, body, signature] = parse_token(token)
    print(f"Inspecting {args.token}")
    print("Header:\n", json.dumps(header, indent=4))
    print("Body:\n", json.dumps(body, indent=4))


def create_unsigned(args):
    import jwt

    token = jwt.encode({"id": 1}, "", algorithm="none")
    print(token)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Various JWT utils", add_help=True)
    subparsers = parser.add_subparsers()

    parser_unsigned = subparsers.add_parser(
        "create-unsigned", description="Create a an unsigned JWT"
    )
    parser_unsigned.set_defaults(func=create_unsigned)

    parser_analyze = subparsers.add_parser(
        "analyze", description="Analyze token for parts, encodings, etc."
    )
    parser_analyze.add_argument("token", type=str, help="path to file containing token")
    parser_analyze.set_defaults(func=analyze)

    parser_inspect = subparsers.add_parser(
        "inspect",
        description="Print token header and body. If unsure if token is a JWT, use analyze command instead.",
    )
    parser_inspect.add_argument("token", type=str, help="path to file containing token")
    parser_inspect.set_defaults(func=inspect)

    parser_crack = subparsers.add_parser(
        "crack", description="Attempt to find token secret using a brute force attempt"
    )
    parser_crack.add_argument("token", type=str, help="to file containing token")
    parser_crack.add_argument(
        "--signatures",
        type=str,
        help="path to file containing signatures that should be checked. Each line is interpreted is its own signature",
        required=True,
    )
    parser_crack.set_defaults(func=crack)

    args = parser.parse_args()
    if "func" in args:
        args.func(args)
    else:
        print("Run with -h to see available commands")
