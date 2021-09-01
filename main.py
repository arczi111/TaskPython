import random
import string


def removeEverySecondLetter(name):
    newName = ''
    for i in range(0, len(name), 2):
        newName += name[i]

    return newName


with open('names.txt', 'r') as rf:
    with open('new_names.txt', 'w') as wf:
        for line in rf:
            stripLine = line.strip()

            wf.write(stripLine + ";" + stripLine.replace(random.choice(stripLine), '', 1))
            wf.write("\n" + stripLine + ';' + random.choice(string.ascii_letters).upper() + stripLine)
            wf.write("\n" + stripLine + ';' + stripLine[::-1])
            wf.write("\n" + stripLine + ';' + removeEverySecondLetter(stripLine) + "\n")

