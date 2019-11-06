import string
import secrets


def gen_key(parts=4, chars_per_part=8):
    alphabet = string.ascii_uppercase + string.digits
    choices = []
    for _ in range(parts):
        choices.append(''.join(secrets.choice(alphabet) 
                               for _ in range(chars_per_part)))
    return '-'.join(choices)
        