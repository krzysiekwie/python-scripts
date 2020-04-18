#looped and extended version of a dictionary search from a udemy course

import json
import glob
from difflib import get_close_matches

for f in glob.glob("*.json"):
    print(f)

dict = input("what termbase do you need? ('Enter' for default) ")
if dict == "":
    data = json.load(open("terms.json"))
else:
    data = json.load(open(dict))


def translate(w):
    w = w.lower()
    if w != "":
        if w in data:
            return data[w]
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean ''%s'? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
            if yn.lower() == "y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn.lower() == "n":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."
        else:
            return "The word doesn't exist. Please double check it."
    else:
        return "Bye!"

word = "none"
while (word != ""):
    word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
