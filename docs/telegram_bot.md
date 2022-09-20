# Telegram Bot API

The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram.

## Authorizing your bot

Each bot is given a unique authentication token when it is created. The token looks something like ```123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11```. 

## Generating an authentication token

If your existing token is compromised or you lost it for some reason, use the /token command to generate a new one.

## Creating a new bot

Use the /newbot command to create a new bot. The BotFather will ask you for a name and username, then generate an authentication token for your new bot.

The name of your bot is displayed in contact details and elsewhere.

The Username is a short name, to be used in mentions and t.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username must end in 'bot', e.g. 'tetris_bot' or 'TetrisBot'.

The token is a string along the lines of ```110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw``` that is required to authorize the bot and send requests to the Bot API. Keep your token secure and store it safely, it can be used by anyone to control your bot.

## Botfather commands

The remaining commands are pretty self-explanatory:

* /mybots — returns a list of your bots with handy controls to edit their settings
* /mygames — does the same for your games

Edit bots

* /setname – change your bot's name.
* /setdescription — change the bot's description, a short text of up to 512 characters, describing your bot. Users will see this text at the beginning of the conversation with the bot, titled 'What can this bot do?'.
* /setabouttext — change the bot's about info, an even shorter text of up to 120 characters. Users will see this text on the bot's profile page. When they share your bot with someone, this text is sent together with the link.
* /setuserpic — change the bot's profile pictures. It's always nice to put a face to a name.
* /setcommands — change the list of commands supported by your bot. Users will see these commands as suggestions when they type / in the chat with your bot. Each command has a name (must start with a slash ‘/’, alphanumeric plus underscores, no more than 32 characters, case-insensitive), parameters, and a text description. Users will see the list of commands whenever they type '/' in a conversation with your bot.
* /deletebot — delete your bot and free its username.

Edit settings

* /setinline — toggle inline mode for your bot.
* /setinlinegeo - request location data to provide location-based inline results.
* /setjoingroups — toggle whether your bot can be added to groups or not. Any bot must be able to process private messages, but if your bot was not designed to work in groups, you can disable this.
* /setprivacy — set which messages your bot will receive when added to a group. With privacy mode disabled, the bot will receive all messages. We recommend leaving privacy mode enabled. You will need to re-add the bot to existing groups for this change to take effect.

Manage games

* /newgame — create a new game.
* /listgames — get a list of your games.
* /editgame — edit a game.
* /deletegame — delete an existing game.

Please note, that it may take a few minutes for changes to take effect.

