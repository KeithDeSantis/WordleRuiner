import requests
import re
import sys
import time
import smtplib

with open("email.txt", "r") as f:
        EMAIL = f.read()
with open("pass.txt", "r") as f:
        PASS = f.read()
HOST = "smtp.gmail.com"
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

PREVIOUS_WORD_FILE = "prev.txt"
LOG_FILE = "wordleRuinerLog.txt"
victims = [("7819297124", "verizon")]

# Write to log
def writeToLog(message):
    with open("wordleRuinerLog.txt", 'a') as f:
        f.write(message + "\n")

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
        writeToLog("[ERROR]: Failed to find match from tomsguide.com")
        exit(1)

# Save the Wordle word to prev.txt so we don't send multiple texts in a day
def saveWord(word):
    with open(PREVIOUS_WORD_FILE, "w") as f:
        f.write(word)

# Get the last word we sent
def getPreviousWord():
    with open(PREVIOUS_WORD_FILE, "r") as f:
        return f.read()

# Text the victims the Wordle word
def sendText(victim_number, victim_carrier, message):
    victim = victim_number + CARRIERS[victim_carrier]
    auth = (EMAIL, PASS)
    server = smtplib.SMTP(HOST, 587)
    server.starttls()
    server.login(auth[0], auth[1])
    server.sendmail(auth[0], victim, message)

# This function ruins someone's day
def ruinWordle():
    while(True):
        # Get the Wordle word from tomsguide.com
        word = getWordleWord()

        # If the word hasn't changed, don't send a new text
        if(getPreviousWord() != word):
            # Get our victim info (either hardcoded or passed in as command line args)
            victims = getVictims()

            # Send texts
            for v in victims:
                sendText(v[0], v[1], f"{word} is today's Wordle word")
                writeToLog(f"Sent to {v}...")

            # Save the word to our prev.txt file to remind ourselves we've already sent a text for today
            saveWord(word)

        # Repeat every hour
        time.sleep(3600)

if __name__ == "__main__":
    ruinWordle()
