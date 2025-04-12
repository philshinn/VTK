# https://pocketsphinx.readthedocs.io/en/latest/pocketsphinx.html
from pocketsphinx import LiveSpeech
import sys

def recognizeSpeech():
    while True:
        for phrase in LiveSpeech():
            print(phrase)
            print(type(phrase))
            #return phrase
            #if phrase == 'stop':
            #    return phrase

if __name__ == "__main__":
    phrase = recognizeSpeech()
