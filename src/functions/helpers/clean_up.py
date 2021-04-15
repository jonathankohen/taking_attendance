import re


def cleanUp(word):
    bad = '[]()-"'

    if len(word) < 3:
        return False

    capitalCounter = 0

    for i in range(0, len(word)):
        if word[i] in bad:
            return False

        if type(word[i]) == int:
            return False

        if capitalCounter == 2:
            return False

        if word[i].isupper():
            capitalCounter += 1

    return True


def spaces_bt_caps(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
