import requests
import re
import sys

PREVIOUS_WORD = ""
victims = [("1111111111", "Verizon"), ("222222222", "T-Mobile")]

# Set victims if they were passed in
def getVictims():
    if(len(sys.argv) < 3):
       return victims
    if(len(sys.argv) % 2 == 0):
        print("Please enter victim phone numbers and providers in the format: \"python wordleRuiner.py XXXXXXXXXX <Provider>\"")
        exit(1)
    newVictims = []
    for i in range(1, len(sys.argv), 2):
        newVictims.append((sys.argv[i], sys.argv[i+1]))
    return newVictims

# Get Wordle word from tomsguide.com because pulling it from the NYT JavaScript kinda sucks
def getWordleWord():
    resp = requests.get('https://www.tomsguide.com/news/what-is-todays-wordle-answer')
    if (resp.ok):
        match = re.search("(?<=Drumroll, please &mdash; it's <strong>)([A-Z]{5})(?=\.<\/strong>)", resp.text)
        if(match):
            return match.group(1)
    else:
        print("[ERROR]: Failed to find match from tomsguide.com")
        exit(1)

def sendText():
    pass

if __name__ == "__main__":
    victims = getVictims()
    print(victims)