import random
import string
import os
import json

os.urandom(1099)

names = json.load(open(file="names.json"))
chars = string.ascii_letters + string.digits + "-_@"

def generate_id(n):
    _id = random.choice(names).lower()
    extra_digits = (random.choice(string.digits) for i in range(n))
    extra_digits = "".join(extra_digits)
    switcher = [0,1]
    if random.choice(switcher) == 1:
        full_id = _id + extra_digits
    else:
        full_id = extra_digits + _id
    return full_id


def generate_pass(n):
    password = (random.choice(chars) for i in range(n))
    password = "".join(password)
    return password


def generate_email(n):
    domains = ['gmail.com', 'yahoo.com']
    prefix = generate_id(n)
    email = prefix + "@" + random.choice(domains)
    return email

# print out 5 random credentials
for i in range(5):
    print("ID GENERATED: " + generate_id(4))
    print("EMAIL GENERATED: " + generate_email(4))
    print("PASSWORD GENERATED: " + generate_pass(10) + '\n')

