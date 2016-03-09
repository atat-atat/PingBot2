##PingBot2
PingBot is a Discord.py bot made using Python (discord.py)

This is still in development.

##Running the Bot

To run PingBot, simply execute bot.py.

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
This file holds the server IDs where PingBots message-delete message should be disabled on. (Especially if that server has a cleanup command.)

```
12345678910,132435465654
```


You will also need the requiring modules, of course.

To get a user to join a channel, send the bot the Discord invite link.

##Requirements

- Python 3.5+
- discord.py
- BeautifulSoup
- wikipedia
- cleverbot
- Pillow