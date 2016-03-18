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

Be sure to edit the `bot.json` file located in `\core\config\`.

Below is a documentation of the `bot.json` file.

##bot.json
This file holds PingBot's configurations.

```
	"admins" : [
	List of bot-admin IDs. Bot admins are able to use commands like !load, !set, !set_show, etc.
	],

	"no_delete": [
	List of server IDs that the message-delete function should be disabled on.
	],

	"banned_say_words": [
	List of words that the !say command will not display.
	],

	"no_say": [
	List of server IDs that the !say command should be disabled on.
	],

	"no_welcome": [
	List of server IDs that the welcome-messenger function should be disabled on.
	],

	"startup_cogs": [
	Startup cogs.
	],

	"bot_name": The bot's username,
	"email": The bot's email,
	"password": The bot's password,
	"prefix": The command prefix,
	"pm_help": Whether the user should send the Help commands to the command author via PM,
	"enable_delete_msg": If the delete-message function should be enabled,
	"enable_welcome_msg": If the welcome messenger should be enabled,
	"enable_offline_messenger": If the offline user-messenger should be enabled,
	"enable_custom_commands": Whether custom commands should be enabled,
	"enable_osu": If osu! commands should be enabled,
	"enable_wunderground": If weather/Wunderground commands should be enabled,
	"random_games": If the currently-playing game should change to a random game from the list,
	"user_bot_changes": Whether commands like !change_name, and !change_game can be used by normal users,

	"description": The bot description,
	"no_perm_msg": When the user does not have permission to run the command,
	"only_owner": When the command author attempts to use a server-owner-only command,
	"annoyed": "Nice try.",
	"no_kick_perm": When the command author does not have the permission to kick users,
	"kick_forbidden": When the bot does not have sufficient permissions to kick users,
	"kick_success": When the bot successfully kicks a user,
	"no_ban_perm": When the command author does not have permission to ban users,
	"ban_forbidden": When the bot does not have the sufficient permissions to ban users,
	"ban_success": When the bot successfully bans a user,
	"no_command_pm": When a user attempts to use a no-PM command in a PM,
	"no_user_found": When the bot fails to find a user,

	"games": [
	List of currently-playing games that the random games function selects. (You can disable this feature via random_games)
	],

	"osu_key": Your osu! API key. You can disable osu! commands via enable_osu,
	"wunderground_key": Your Wunderground API key. You can disable weather/wunderground commands via enable_wunderground.
```

##Requirements

- Python 3.4+
- discord.py
- BeautifulSoup
- wikipedia
- cleverbot
- Pillow