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

To get PingBot to join a server, simply send PingBot the Discord invite link via PM.

Be sure to edit the `bot.info` file located in `\core\config\`, as well as any other files located in there.

Below is a list of config files and what they do...

##bot.info File
This file holds the login information for PingBot.

```
Email:Password
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

##Requirements

- Python 3.5+
- discord.py
- BeautifulSoup
- wikipedia
- cleverbot
- Pillow