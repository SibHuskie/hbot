import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

client = commands.Bot(command_prefix="hb")
footer_text = "Horny Hubbies"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Horny Hubbies (18+)'))

@bot.event
async def on_message(message):
    if message.content.lower().startswith('hello hb'):
        author = str(message.author).split("#")[0]
        msg = "Hey {}! :3".format(author)
        await bot.send_message(message.channel, msg)

client.run(os.environ['BOT_TOKEN'])
