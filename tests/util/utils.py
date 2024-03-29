import random
import string
from typing import Any


def random_str_to_lowercase() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def gen_random_email() -> str:
    return f"{random_str_to_lowercase()}@{random_str_to_lowercase()}.com"


def gen_random_password() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))
