## Python Scripts for Hexchat

Scripts I've written/adapted for Hexchat are in this repo. Below is an overview of what's available.

#### multichan.py

Allows you to execute commands across multiple channels. Useful for banning a user from more than one channel at once.

Commands can also take a `{ch}` tag to specify that the targeted channel's name be used in the command.

This is based on a script written by [A_D](https://github.com/A-UNDERSCORE-D) on [Snoonet](https://snoonet.org/).

Current commands are:

`XCMD` - Execute any command

`XSAY` - Send a message to multiple channels

`XACT` - Send an action (/me) to multiple channels

`XBAN` and `XUNBAN` - Ban/Unban a user from multple channels - uses chanserv. This might change in the future

`XKICK` - Kick a user from multiple channels

#### opmsmsg.py

Sends a msg to every op in the current channel via MemoServ telling them why you were required to override or ojoin their channel.

This is extremely useful for IRC staff to let chanops know if you needed to kick/ban someone and no one is around.

You may want to change the template before using as it's currently suited for Snoonet.

###### Usage
`MSREPORT <nick> <action> <reason> [logurl]` - Sends a report to chanops viua MemoServ. Optionally takes a URL for a log or whatever.