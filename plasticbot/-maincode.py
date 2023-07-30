import discord

from discord.ext import commands


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

    #tips
@bot.command()
async def tips(ctx):
    await ctx.send("""- Remember to always throw your garbage in it's place!
- Don't throw your plastic wastes away, recycle it!
- Don't throw your garbage to the river!
- You can sort you garbage from organic and anorganic!""")


#run bot
bot.run("")