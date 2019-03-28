import discord
from discord.ext import commands
import sqlite3

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.c = sqlite3.connect('currency.db')
        self.connect = self.c.cursor()

    @commands.command()
    async def ping(self, ctx): # simple reply
        await ctx.send("pong!")

    @commands.group()
    async def pong(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("ping")

    @pong.command()
    async def pang(self, ctx):
        await ctx.send("ping pang")


def setup(bot):
    bot.add_cog(Commands(bot))