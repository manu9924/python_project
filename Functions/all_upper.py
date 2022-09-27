def is_all_upper(text: str) -> bool:
    if text.upper() == text:
        return True
    if text.upper() != text:
        return False