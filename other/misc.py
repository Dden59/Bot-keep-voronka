def create_ref_link(base_url: str, user_id: int) -> str:
    """
    Генерирует правильную реферальную ссылку,
    автоматически определяя нужный разделитель (? или &).
    """
    if not base_url:
        return "https://google.com"
        
    # Убираем пробелы и лишние знаки вопроса в конце
    clean_url = base_url.strip().rstrip("?")
    
    # Если в ссылке уже есть параметры (знак ?), используем &, иначе ?
    separator = "&" if "?" in clean_url else "?"
    
    return f"{clean_url}{separator}sub1={user_id}"