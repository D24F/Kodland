import random
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    meme = random.choice(os.listdir('images'))
    with open(f'images/{meme}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

bot.run("MTEyMTc4NDczNjkyMzI3MTE5OA.GvVXcb.OQiAXkJhlFUIhp8xxLLxGA1RXvPKiG7iE3uzr8")