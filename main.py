import random
import string


with open('names.txt', 'r') as rf:
    with open('new_names.txt', 'w') as wf:
        for line in rf:
            stripLine = line.strip()

            wf.write(stripLine + ";" + stripLine.replace(random.choice(stripLine), '', 1))
            wf.write("\n" + stripLine + ';' + random.choice(string.ascii_letters).upper() + stripLine)
            wf.write("\n" + stripLine + ';' + stripLine[::-1])
            wf.write("\n" + stripLine + ';' + stripLine[::2] + "\n")

