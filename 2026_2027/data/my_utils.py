import random

def generate_string(n, alphabet):
    s = ""
    for i in range(n):
        s += random.choice(alphabet)

    return s
