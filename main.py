import json;
from difflib import get_close_matches;

def load_data(fpath):
    return json.load(open(fpath))

def search_data(key):
    key = key.lower()
    if key in data:
        return data[key]
    else:
        words = get_close_matches(key, data.keys())
        if len(words) > 0:
            ans = input("Did you mean \"%s\" instead? Press Y or N: " % words[0])
            if ans == "Y":
                return search_data(words[0])
            else:
                return "It doesn't exist."
        else:
            return "It doesn't exist."

data = json.load(open("resources/data.json"))
word = input("Enter a word :")
print(search_data(word))
