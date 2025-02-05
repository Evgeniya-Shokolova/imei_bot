import os

WHITELIST = set(map(int, os.getenv('WHITELIST', '').split(',')))


def is_user_allowed(user_id: int) -> bool:
    return user_id in WHITELIST
