
def questions():
    # First, open the file to read its contents
    with open("data/data.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Now, open the file again in append mode to write new data
    with open("data/only_questions.txt", "a", encoding="utf-8") as file:
        for line in text.split("\n"):
            # Assuming you're trying to split based on two spaces and get the second part
            if len(line.split("  ")) > 1:  # Check to ensure there's a second part
                l = line.split("  ")[1]
                file.write(l + "\n")  # Add a newline after writing each part


def answare():
    with open("data/answares.txt", 'r', encoding='utf-8') as answares:
        text_answares = answares.read()

    with open("data/only_answares.txt", "a", encoding="utf-8") as answares:
        for line in text_answares.split("\n"):
            if len(line.split("  ")) > 1:
                l = line.split("  ")[1]
                answares.write(l + "\n")


def two_in_one():
    with open("data/only_answares.txt", "r", encoding="utf-8") as answares:
        ans = answares.read().split('\n')

    with open("data/only_questions.txt", "r", encoding="utf-8") as questions:
        ques = questions.read().split('\n')

    data = {}
    for i in range(0, 100):
        data[ques[i]] = ans[i]

    return data


def full_data():
    with open("data/only_answares.txt", "r", encoding="utf-8") as answares:
        ans = answares.read().split('\n')


    with open("data/only_questions.txt", "r", encoding="utf-8") as questions:
        ques = questions.read().split('\n')


    with open("data/full_data.txt", "a", encoding="utf-8") as file:

        mix = []

        for i in range(0, 100):
            mix.append(f"{ques[i]} == {ans[i]}\n")
        
        file.writelines(mix)
        

def nasty_data():
    with open('data/nasty_data.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    return text


def cleaning_data(text: str) -> list:
    cleaned_data = []
    all_questions = text.split("\n\n")

    for question in all_questions:
        if "➡️" in question:
            question = question.replace("➡️", " == ")
        if "👉" in question:
            question = question.replace("👉", " == ")

        question += "|||"
        # Optionally warn if neither symbol is found
        if "==" not in question:
            print("Warning: no marker found in question ->", question[:50])

        cleaned_data.append(question.strip())

    return cleaned_data


def set_data(cleanned_data: list):
    with open("data/cleaned_data_from_nasty.txt", "a", encoding="utf-8") as file:
        file.writelines(cleanned_data)
        

set_data(cleaning_data(nasty_data()))