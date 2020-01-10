import threading

import hexchat
import requests
import emoji

__module_name__ = "ircemoji"
__module_version__ = "0.1000000003"
__module_description__ = "Converts emoji shortcodes in the text field to emojis."

KEYIDs = {
    "65293": "enter",
}


def on_key(word, word_eol, userdata):
    keyid = word[0]
    if keyid not in KEYIDs:
        return
    key_name = KEYIDs[keyid]
    if key_name == "enter":
        if bool(int(word[1]) & 0b1):
            input_box = hexchat.get_info("inputbox")
            if input_box.startswith("//"):
                hexchat.command(f"say {input_box[1:]}")
            elif input_box.startswith("/"):
                hexchat.command((input_box[1:]))
            else:
                hexchat.command(f"say {input_box}")
            hexchat.command("settext ")
            return hexchat.EAT_NONE
        return parse_emojis()


def parse_emojis():
    input_box = hexchat.get_info("inputbox")
    hexchat.command(f"settext {emoji.emojize(input_box, use_aliases=True)}")
    return hexchat.EAT_NONE

def emoji_cmd(word, word_eol, userdata):
    return parse_emojis()


@hexchat.hook_unload
def onunload(userdata):
    print(__module_name__, "unloaded")


hexchat.hook_print("Key Press", on_key, priority=hexchat.PRI_HIGH)
hexchat.hook_command("EMOJI", emoji_cmd)

print(__module_name__, "loaded")
