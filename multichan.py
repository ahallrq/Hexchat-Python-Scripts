import hexchat

__module_name__ = "multichan"
__module_version__ = "1.0"
__module_description__ = "runs a command on multiple channels"


def command_cb(word, word_eol, userdata):
    if len(word) >= 3:
        targets = word[1].split(",")
        command = " ".join(word[2:])
        for target in targets:
            targetctx = hexchat.find_context(hexchat.get_info("server"), target)
            if targetctx:
                fmt_command = command.format(ch=target)
                targetctx.command(fmt_command)
    else:
        hexchat.command("HELP MASSCMD")

    return hexchat.EAT_ALL


def say_command_cb(word, word_eol, userdata):
    word.insert(2, "SAY")
    return command_cb(word, word_eol, userdata)

def act_command_cb(word, word_eol, userdata):
    word.insert(2, "ACTION")
    return command_cb(word, word_eol, userdata)

def kick_command_cb(word, word_eol, userdata):
    word.insert(2, "CS KICK {ch}")
    return command_cb(word, word_eol, userdata)

def ban_command_cb(word, word_eol, userdata):
    word.insert(2, "CS ban {ch}")
    return command_cb(word, word_eol, userdata)

def unban_command_cb(word, word_eol, userdata):
    word.insert(2, "CS unban {ch}")
    return command_cb(word, word_eol, userdata)

#def mute_command_cb(word, word_eol, userdata):
#    word.insert(2, "CS mute {ch}")
#    return command_cb(word, word_eol, userdata)

#def unmute_command_cb(word, word_eol, userdata):
#    word.insert(2, "CS unmute {ch}")
#    return command_cb(word, word_eol, userdata)

@hexchat.hook_unload
def onunload(userdata):
    print(__module_name__, "unloaded")

hexchat.hook_command("XCMD", command_cb, help="USAGE: /XCMD target1,target2 command")
hexchat.hook_command("XSAY", say_command_cb, help="Usage: /XSAY target1,targetN... text")
hexchat.hook_command("XACT", act_command_cb, help="Usage: /XACT target1,targetN... action")
hexchat.hook_command("XKICK", kick_command_cb, help="Usage: /XKICK target1,targetN... user reason")
hexchat.hook_command("XBAN", ban_command_cb, help="Usage: /XBAN target1,targetN... +t[s,m,h,d,y] user reason")
hexchat.hook_command("XUNBAN", unban_command_cb, help="Usage: /XUNBAN target1,targetN... user")
#hexchat.hook_command("XMUTE", mute_command_cb, help="Usage: /XMUTE target1,targetN... user")
#hexchat.hook_command("XUNMUTE", unmute_command_cb, help="Usage: /XUNMUTE target1,targetN... user")

print(__module_name__, "loaded")
