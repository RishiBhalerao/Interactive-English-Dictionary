import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

print("\nWelcome to the Interactive English Dictonary\n")

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        ans = input(f"Were you looking for {get_close_matches(word, data.keys(), cutoff=0.8)[0].upper()} instead ? If yes enter Y, if no enter N: ")
        if ans.lower() == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif ans.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry we don't understand your entry."    
    else:
        return "The word doesn't exist. Please double check it."  

user = input("Enter any word: ")

output = meaning(user)

if isinstance(output,list):
    for items in output:
        print(f"~ {items}")
else:
    print(output)
