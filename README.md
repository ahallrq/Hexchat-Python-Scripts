### Python Scripts for Hexchat

Scripts I've written/adapted for Hexchat are in this repo. Below is an overview of what's available.

##### multichan.py

Allows you to execute commands across multiple channels. Useful for banning a user from more than one channel at once.

Commands can also take a `{ch}` tag to specify that the targeted channel's name be used in the command.

This is based on a script written by [A_D](https://github.com/A-UNDERSCORE-D) on [Snoonet](https://snoonet.org/).

Current commands are:

`XCMD` - Execute any command

`XSAY` - Send a message to multiple channels

`XACT` - Send an action (/me) to multiple channels

`XBAN` and `XUNBAN` - Ban/Unban a user from multple channels - uses chanserv. This might change in the future

`XKICK` - Kick a user from multiple channels