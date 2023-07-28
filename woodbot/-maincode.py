import discord
import random
import time
import os

from discord.ext import commands
from botlogic import *


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

#notification
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


#commands
    #hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am {bot.user}!')

    #heh
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

    #pwgen (random password generator)
@bot.command()
async def pwgen(ctx):
    await ctx.send("*generating password...")
    time.sleep(2)
    await ctx.send(gen_pass(8))

    #smile (random emoji generator)
@bot.command()
async def smile(ctx):
    await ctx.send(gen_emoji())

    #coin (coin flipping)
@bot.command()
async def coin(ctx):
    await ctx.send("*the coin is flipping...")
    time.sleep(2)
    await ctx.send(flip_coin())

    #meme (random meme generator)
@bot.command()
async def meme(ctx):
    meme = random.choice(os.listdir('woodbot/memes'))
    with open(f'woodbot/memes/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    #dice (dice rolling)
@bot.command()
async def dice(ctx):
    await ctx.send("*rolling the dice...")
    time.sleep(2)
    await ctx.send(roll_dice())


#run bot
bot.run("MTEyMTc4NDczNjkyMzI3MTE5OA.GxPt23.mKJyVH4xZi0Q-KGkM1x93MIAlSFLoFihnU7bN4")