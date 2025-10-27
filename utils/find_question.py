
async def find(obj: str, find_from: list) -> list:
    result = []
    for question in find_from:
        if obj.lower() in question.lower():  # регистронезависимый поиск
            result.append(question)
    return result
