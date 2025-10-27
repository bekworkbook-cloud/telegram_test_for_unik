import random

async def get_random_question(questions: list) -> str:
    return random.choice(questions) if questions else "No questions available."
