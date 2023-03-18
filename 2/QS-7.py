'''Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
 {"merry": "god", "christmas":"jul", "and": "och", "happy":"gott" "new": "nytt", "year": "ar"}

and use it to translate your Christmas wishes from English into Swedish.

That is, write a python function translate() that accepts the bilingual
dictionary and a list of English words (your Christmas wish) and returns
a list of equivalent Swedish words.'''

def translate(dict,english_list):
    swedish_list = []
    for x in english_list:
        swedish_list.append(dict[x])

    return swedish_list

dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_list=["merry","christmas"]
print("The bilingual dict is:",dict)
print("The english words are:",english_list)

swedish_words=translate(dict, english_list)
print("The equivalent swedish words are:",swedish_words)