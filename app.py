import os
import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from discord import Game

TOKEN = os.environ['ENV_TOKEN']

bot = commands.Bot(command_prefix='?') #COMMANDS START WITH THIS PREFIX


@bot.command()
async def test(context):
    embed=discord.Embed(title="Hello!", url="https://google.com", type="rich", description="Bot testing")
    await context.send(embed=embed)

@bot.command()
async def wonder(context):
    msg = "<:emoji_12:660581303367761920>"
    await context.send(msg)

@bot.command()
async def nerf(context):
    msg = "No u. You no good, scruffy-looking, nerf-herder!"
    await context.send(msg)

# WHEN A NEW MEMBER JOINS THE SERVER
# bot.get_channel('665042600096432139') WELCOME CHANNEL ID
@bot.event
async def on_member_join(member):
    msg = 'Hello There, {0.mention}! Please set your discord name to match your SWGOH name. '.format(member)
    await bot.commands.send_message(bot.get_channel('665042600096432139'), msg)

  #These trigger on any message. Not just commands.
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    # We also want to make sure it checks for commands first
    await bot.process_commands(message)
    if message.author == bot.user:
    	return
    mcont = message.content.lower()
    if mcont.startswith('hello there'):
       message.channel.sendMessage("General Kenobi!")

# When bot loads, do this stuff.
@bot.event
async def on_ready():
    game = Game("Galaxy of Heroes")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)