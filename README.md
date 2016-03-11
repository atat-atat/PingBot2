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
email=Email
password=Password
prefix=Command prefix.
description=Your bot description.
pm_help=Whether the bot should send the help messages via PM. (recommended)

[messages]
no_permission=When a user attempts a command that they don't have permission to use.
only_owner=When a user attempts a command that they must be the server owner to use.
nuisance_msg=The nuisance message.
divide_zero=When the user attempts to divide by zero via !calc.
no_kick_perm=When a user attempts to use !kick, but they aren't the server owner.
kick_forbidden=When the bot does not have permission to kick users.
kick_success=When the bot successfully kicked the user.
no_command_pm=When a user attempts to run a command via PM that cannot be ran through PM.
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