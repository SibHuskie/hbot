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
    
@client.event
async def on_message(message, timeout=10,):
    await client.process_commands(message)
    if message.content.lower().startswith('hey new bot'):
        await client.send_message(message.channel, "HELLLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        
    if message.content.lower().startswith('hbmc'):
        author = ctx.message.author
        msg = discord.Embed(colour=0xc90000, description= "")
        msg.title = ":closed_book: Member Count :closed_book:"
        msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
        await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
