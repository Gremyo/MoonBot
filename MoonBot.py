import discord
import asyncio
from discord.ext import commands
import platform
import KeyModule

cogList = ["cogs.commands",
           "cogs.GoL"]


class MoonBot(commands.Bot):

    def __init__(self):
        super().__init__(description="MoonBot", command_prefix="%", pm_help=False)
        for cog in cogList:
            self.load_extension(cog)

    async def on_ready(self):  # Tells us info about the bot and readys the bot for taking commands
        print(f'Logged in as {self.user.name} (ID:{self.user.id}')
        # Username and ID
        print('--------')
        print(
            f'Current Discord.py Version: {discord.__version__} | Current Python Version: {platform.python_version()}')
        # Discord and Python version
        print('--------')
        print(f'Use this link to invite {self.user.name}:')
        print(f'https://discordapp.com/oauth2/authorize?client_id={self.user.id}&scope=bot&permissions=8')
        # link that allows us to invite the bot to servers we are admin on, kinda useless since its only for desucartes
        print('--------')
        print('Written by BabySnake#6314')


if __name__ == "__main__":
    client = MoonBot()
    client.run(KeyModule.private_key)
