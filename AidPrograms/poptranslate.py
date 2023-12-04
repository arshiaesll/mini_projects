# Copyright Sep 2023 AE

import subprocess
from pynput.keyboard import Controller, Key, Listener
import requests
from plyer import notification

keyboard = Controller()

def findTranslate(text):
    api_url = "https://api.dictionaryapi.dev/api/v1/entries/en/" + text
    ans='' 
    try:
        response = requests.get(api_url)
        res_j = response.json()
        res_dict = res_j[-1]
        keys = res_dict.keys()
        meaning = res_dict['meaning']
        ans = ''
        for key in meaning.keys():

            try:
                aMeaning = meaning[key]
                ans += (aMeaning[0]['definition'])
            except(ValueError):
                print('DIDN"T FOUND')
            ans +='\n\n'
    except KeyError:
            ans += "TRY AGAIN" 
    return ans

def popup_window(text):
    print('------------------')
    print(text)
    notification.notify( title = "word" , message = text, timeout = 20)
    print('------------------')


def on_press_key(key):
    try: 
        if(key.char == "`"):
            keyboard.press(Key.ctrl_l)
            keyboard.press('c')
            keyboard.release(Key.ctrl_l)
            clipboard_contents = subprocess.check_output([
                "xclip", "-selection", "clipboard", "-o"]).decode("utf-8")
            popup_window(findTranslate(clipboard_contents))
    except(AttributeError):
        print("No match for ` key!")

with Listener(on_press=on_press_key) as listener:
    listener.join()

