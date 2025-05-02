import requests
import re

def getWorldeWord():

    f = open("test.txt")
    txt = f.read()
    word = re.search("(?<=<strong>)WHOSE(?=</strong>)",txt)
    return word.group(10)
    resp = requests.get('https://www.tomsguide.com/news/what-is-todays-wordle-answer')
    if (resp.ok):
        word = re.search(".*\"Drumroll, please &mdash; it's <strong>([A-Z]{5})\.<strong>.*\"", resp.text)
        return word
    else:
        return False

if __name__ == "__main__":
    print(getWorldeWord())