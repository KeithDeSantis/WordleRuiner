import requests
import re

PREVIOUS_WORD = ""

def getWorldeWord():
    resp = requests.get('https://www.tomsguide.com/news/what-is-todays-wordle-answer')
    if (resp.ok):
        match = re.search("(?<=Drumroll, please &mdash; it's <strong>)([A-Z]{5})(?=\.<\/strong>)", resp.text)
        if(match):
            PREVIOUS_WORD = match
            return match.group(1)
    else:
        return False

if __name__ == "__main__":
    print(getWorldeWord())