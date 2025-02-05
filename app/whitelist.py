WHITELIST = {3123127175}


def is_user_allowed(user_id: int) -> bool:
    """Проверка пользователя по ID в белом списке."""
    return user_id in WHITELIST
