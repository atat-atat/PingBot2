##PingBot2
PingBot is a Discord.py bot made using Python (discord.py)

##Features
- searches information from the internet (such as Google, YouTube, and Wikipedia,)
- small miscellaneous features like Cleverbot integration,
- easy to customize,
- welcome messages,
- and more!

PingBot is still in development!

##Running the Bot

To run PingBot, simply execute bot.py.

To get PingBot to join a server, type `!join <invite_link>`

Be sure to edit the `bot.info` file located in `\core\config\`, as well as any other files located in there.

Below is a list of config files and what they do...

##bot.info File
This file holds most of PingBot's configurations.

```
[config]
email=The bot's email address.
password=The bot's password.
original_name=The original bot name. (if you want to quickly revert your bot name back to its original name.)
prefix=The command prefix.
description=The bot description.
pm_help=Sends the user the commands list via PM.
allow_bot_changes=Lets users use !change_game and change_name.
enable_welcome_msg=Enables the welcome message.
enable_delete_msg=Enables the message-delete system. (documented below)

[messages]
no_permission=When a user attempts a command that they do not have permission to use.
only_owner=When a user attempts a command that requires them to be the server owner.
nuisance_msg=Nice try.
divide_zero=When a user attempts to divide by zero via !calc.
no_kick_perm=When the user attempts to use !kick, but they aren't the server owner.
kick_forbidden=When the bot does not have the permission to kick users.
kick_success=When the bot successfully kicked a user.
no_command_pm=When a user attempts a command that cannot be executed in a PM.
```

##command_sets.info File
This file holds what command extensions should be loaded at startup.

```
core.commands.search_cmd,core.commands.commands
```

##admins.info File
This file holds the user IDs who can use commands like !reload, !load and etc.

```
12345678910,122435462121
```

##no_delete.info File
This file holds the server IDs where PingBots `message-delete` system should be disabled on. (Especially if that server has a cleanup command.)

(The `message-delete` system is a feature where whenever a user deletes a message, PingBot will be notified and it will send the deleted message.)

```
12345678910,132435465654
```

##no_welcome.info File
This file holds the server IDs where PingBots welcome messages should be disabled on.

```
12345678910,123243543565
```

##no_say.info File
This file holds the server IDs where PingBot cannot execute !say.

```
12345678910,133343546465
```

##banned_words.info File
This file holds a list of words that if !say contains, it will ignore it and send the `nuisance_msg`.

```
!say|;bank|frick|swear word
```

##Requirements

- Python 3.5+
- discord.py
- BeautifulSoup
- wikipedia
- cleverbot
- Pillow
- win32api