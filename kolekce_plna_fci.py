import random

funky_functions = []


def upper_case(text: str) -> str:
    return text.upper()


def space_to_smile(text: str) -> str:
    return text.replace(" ", ":)")


def charV_to_charW(text: str) -> str:
    return text.replace("V", "W")


def star_to_end_start(text: str) -> str:
    return "*" + text + "*"


def question_to_three_times(text: str) -> str:
    text = text.replace("?", "???")
    return text.replace("!", "!!!!!")


def funky_format(text: str) -> str:
    end = ""
    for i in range(3):
        end += random.choice(funky_functions)(text) + "\n"
    return end


try:
    funky_functions.append(upper_case)
    funky_functions.append(space_to_smile)
    funky_functions.append(charV_to_charW)
    funky_functions.append(star_to_end_start)
    funky_functions.append(question_to_three_times)
    print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))
except Exception as e:
    print(e)
