import random
import string
import argparse

def gen_password(length, digit=8):
    passwds = []
    for _ in range(length):
        chars = string.ascii_letters + string.digits
        password = "".join(random.choice(chars) for i in range(digit))
        passwds.append(password)
    return passwds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", help="Return randomly generated passwords", type=int)
    parser.add_argument("-d", "--digit", help="Specify the number of digits of each password", type=int)
    parser.add_argument("-o", "--output", help="Save output t a file", action="store_true")
    args = parser.parse_args()

    if args.digit:
        print(gen_password(args.length, args.digit))
    else:
        print(gen_password(args.length))
    if args.output:
        with open("passwd_generated.txt", "w") as f:
            if args.digit:
                for i in gen_password(args.length, args.digit):
                    f.write(i)
                    f.write("\n")
            else:
                for i in gen_password(args.length):
                    f.write(i)
                    f.write("\n")
        print("Generated passwords saved to passwd_generated.txt")


if __name__ == "__main__":
    main()
