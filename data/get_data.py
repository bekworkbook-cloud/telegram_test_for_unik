
async def get_data(*sort) -> list:
    with open('data/full_data.txt', 'r', encoding='utf-8') as file:
        questions = file.read()

    questions = questions.split('\n')

    if sort and callable(sort[0]):
        return sort[0](questions)

    return questions

async def get_nasty_data():
    with open("data/cleaned_data_from_nasty.txt", "r", encoding="utf-8") as file:
        questions = file.read()

    questions = questions.split("|||")

    return questions
    
