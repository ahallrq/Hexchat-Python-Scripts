import hexchat, datetime

__module_name__ = "opmsmsg"
__module_version__ = "0.01"
__module_description__ = "Reports override/ojoin incidents to channel ops via MemoServ."

templ_header = "Greetings {f_target}, an incident occured in {f_channel} at {f_time} {f_tz}on {f_date} requiring a Snoonet staff member briefly take control of your channel as no channel ops were available. The user \"{f_nick}\" was {f_action} in {f_channel} for {f_reason}. "

templ_log = "An incident log is available at {f_url}. "

templ_footer = "For more info please contact a staff member in #optalk or #help. Cheers."

def command_cb(word, word_eol, userdata):
        user_list = hexchat.get_list("users")
        if(len(word) > 4):
            url = word[4]
        else:
            url = None

        if user_list:
            ops = [item.nick for item in user_list if item.prefix in ("@", "&", "~") and item.nick != hexchat.get_info("nick")]
            for op in ops:
                send_report(op, hexchat.get_info("channel"), word[1], word[2], word[3], url)
            
        return hexchat.EAT_ALL

def send_report(f_target, f_channel, f_nick, f_action, f_reason, f_url=None, dt=datetime.datetime.now()):
    comm = f"MS RSEND {f_target} " + templ_header
    if f_url not in ["", None]:
        comm += templ_log
    comm += templ_footer

    f_date = dt.strftime("%d/%m/%Y")
    f_time = dt.strftime("%H:%M:%S")
    f_tz = dt.strftime("(offset %z) ")
    if f_tz == "(offset ) ":
        f_tz = ""

    hexchat.command(comm.format(f_target=f_target, f_channel=f_channel, f_nick=f_nick, f_action=f_action,
        f_url=f_url, f_date=f_date, f_time=f_time, f_tz=f_tz, f_reason=f_reason))

    #hexchat.prnt(comm.format(f_target=f_target, f_channel=f_channel, f_nick=f_nick, f_action=f_action,
    #    f_url=f_url, f_date=f_date, f_time=f_time, f_tz=f_tz, f_reason=f_reason))

hexchat.hook_command("MSREPORT", command_cb, help="/MSREPORT <nick> <action> <reason> [logurl] - Report an override/ojoin incident to a channel's ops.")
