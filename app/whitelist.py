WHITELIST = {12345678, 87654321}


def is_user_allowed(user_id: int) -> bool:
    """Проверка пользователя по id в списке"""
    return user_id in WHITELIST

