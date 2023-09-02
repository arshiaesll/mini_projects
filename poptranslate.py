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
        # print(type(res_j[-1]))
        res_dict = res_j[-1]
        # print(res_dict.keys())
        # print(res_dict['word'])
        keys = res_dict.keys()
        # print(keys)
        meaning = res_dict['meaning']
        ans = ''
        for key in meaning.keys():

            try:
                aMeaning = meaning[key]
                # print(ans.keys())
                ans += (aMeaning[0]['definition'])
                # print(ans)
            except(ValueError):
                print('DIDN"T FOUND')
            ans +='\n\n'
    except KeyError:
            ans += "TRY AGAIN" 
    # print(ans)
    return ans
# definition = meaning["definitions"][0]["definition"]
# example = meaning["definitions"][0]["example"]
# print(definition)
# print(res_j.shape)

# findTranslate('morning')

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
            clipboard_contents = subprocess.check_output([
                "xclip", "-selection", "clipboard", "-o"]).decode("utf-8")
            # print("TRASLATING ", clipboard_contents)
            popup_window(findTranslate(clipboard_contents))
    except(AttributeError):
        print("DIDIN")

with Listener(on_press=on_press_key) as listener:
    listener.join()

