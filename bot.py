import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

client = commands.Bot(command_prefix="h!")
footer_text = "Horny Hubbies"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Horny Hubbies (18+)'))
    
    
#COMMANDS FOR EVERYONE    

# membercount
@client.command(pass_context=True)
async def mc(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ":closed_book: Member Count :closed_book:"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)
    
# }ping
@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.set_footer(text=footer_text)
    msg.title = ""
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    msg.add_field(name=":satellite: ", value="`Yes, I am here. No need to ping me.`\n`Ping: {}ms`".format(round((t2-t1)*1000)))
    await client.say(embed=msg)
    print("============================================================")
    print("}ping")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
client.run(os.environ['BOT_TOKEN'])
