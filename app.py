import os
import discord
from discord.ext import commands
from discord.utils import get

TOKEN = os.environ['ENV_TOKEN']

bot = commands.Bot(command_prefix='?') #COMMANDS START WITH THIS PREFIX


@bot.command()
async def test(context):
    embed=discord.Embed(title="Hello!", url="https://google.com", type="rich", description="Bot testing")
    await context.send(embed=embed)

# WHEN A NEW MEMBER JOINS THE SERVER
# bot.get_channel('665042600096432139') WELCOME CHANNEL ID
# @bot.event
# async def on_member_join(member):
# 	msg = 'Hello There, {0.mention}! Please set your discord name to match your SWGOH name. '.format(member)
#   await bot.say(msg)

# When bot loads, do this stuff.
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')