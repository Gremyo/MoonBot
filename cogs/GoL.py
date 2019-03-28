import discord
from discord.ext import commands
import ast
import numpy as np
from scipy.signal import convolve2d
import asyncio


class GoL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def GoLReply(self, ctx, arg):  # simple reply
        await ctx.send(type(arg), arg)

    @commands.command()
    async def GoL(self, ctx, seed="random", steps = 10, step_speed=5):

        if seed.lower() != "random":
            try:
                inputseed = ast.literal_eval(seed)
                if type(inputseed[0]) != tuple:
                    raise ValueError
            except ValueError:
                await ctx.send("Invalid Input, please input at least 2 points as (x0,y0),(x1,y1),...")
                return 1
            await ctx.send("Valid Input Data")
            board = GameOfLifeClass(inputseed)
        else:
            await ctx.send("Valid Input Random")
            board = GameOfLifeClass()

        message = await ctx.send(board.BoolBoard)
        print("got here")
        if type(steps) != int:
            await ctx.send("Step must be int")
            return 1
        elif steps<5:
            steps = 5
        elif steps>50:
            steps = 50

        if type(step_speed) != int:
            await ctx.send("step speed must be int")
            return 1
        elif step_speed<1:
            step_speed = 1
        elif step_speed>10:
            step_speed=10

        for j in range(int(steps)):
            board.Step()
            await asyncio.sleep(int(step_speed))
            await message.edit(content=board.BoolBoard)
        return 0


class GameOfLifeClass:
    def __init__(self, seed=False):
        self.seed = seed
        if seed:
            tempBoard = np.zeros((10, 10), dtype=int)
            for x in seed:
                tempBoard[x[0], x[1]] = 1
            self.BoolBoard = tempBoard
        else:
            self.BoolBoard = np.around(np.random.rand(10, 10), 0).astype(int)
        self.kernel = np.ones((3, 3), dtype=int)
        self.kernel[1, 1] = 0  # creates an np array of 1s with the center being 0

    def Step(self):  # runs in O(n^3) with board size
        NeighborCount = convolve2d(self.BoolBoard, self.kernel, mode='same', boundary='wrap')
        self.BoolBoard = (NeighborCount == 3) | (self.BoolBoard & (NeighborCount == 2))
        # | and & are overloaded to run as 'logical or' and 'logical and' from numpy for numpy arrays


def setup(bot):
    bot.add_cog(GoL(bot))
