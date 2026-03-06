import string
import random

def generate_str(
    len_str: int,
    lowercase=True,
    numb=True,
    both_cases=False,
) -> str:
    """
    Random string generator
    :param len_str:  string length
    :param lowercase: True - lowercase, False - uppercase
    :param numb: True - include digits, False - exclude digits
    :param both_cases: True - use both cases
    :return: random string
    """
    uppercase_lat = string.ascii_uppercase
    lowercase_lat = string.ascii_lowercase
    digits = string.digits

    res_str = []

    if both_cases:
        letters = lowercase_lat + uppercase_lat
    else:
        letters = lowercase_lat if lowercase else uppercase_lat

    chars = letters + digits if numb else letters # add numbers if needed

    for i in range(len_str):
        res_str.append(random.choice(chars))

    # res_str = ''.join(random.choice(chars) for _ in range(len_str))

    return "".join(res_str)


print(generate_str(len_str=5, lowercase=True, numb=True))       # lowercase + numbers
print(generate_str(len_str=5, lowercase=False, numb=False))     # uppercase
print(generate_str(len_str=10, lowercase=True, numb=False))     # lowercase
print(generate_str(len_str=10, both_cases=True, numb=True))     # both_cases + numbers