import string
import random


def registration_code_generator(prefix, size=12, chars=string.ascii_uppercase + string.digits):
    return prefix + ''.join(random.choice(chars) for _ in range(size))

