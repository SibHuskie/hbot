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
    
# }ship <user1> <user2>
@client.command(pass_context=True)
async def ship(ctx, userName1: discord.Member = None, userName2: discord.Member = None):
    percent = random.randint(0, 101)
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName1 == None or userName2 == None:
        msg.add_field(name=":bangbang: ",value="`h!ship <user1> <user2>`")
    else:
        if percent >= 1 and percent <= 10:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Shit\n```\n:sob: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 11 and percent <= 20:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Awful\n```\n:cry: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 21 and percent <= 30:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Really Bad\n```\n:frowning2: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 31 and percent <= 40:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Bad\n```\n:slight_frown: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 41 and percent <= 50:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Okay\n```\n:neutral_face: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 51 and percent <= 60:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Good\n```\n:slight_smile: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 61 and percent <= 70:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Very Good\n```\n:smiley: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 71 and percent <= 80:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Fantastic\n```\n:blush: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 81 and percent <= 90:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Amazing\n```\n:heart_eyes: ".format(userName1.display_name, userName2.display_name, percent))
        else:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Perfect\n```\n:revolving_hearts: ".format(userName1.display_name, userName2.display_name, percent))
    await client.say(embed=msg)
    print("============================================================")
    print("}ship <user1> <user2>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.set_footer(text=footer_text)
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value=(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value=(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value=(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value=(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value=(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value=(ctx.message.server.created_at), inline=True)
    msg.add_field(name="RELEASE DATE:", value="9th of March 2018", inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}serverinfo")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }chocolate <user> <number>
@client.command(pass_context=True)
async def chocolate(ctx, userName: discord.Member = None, number: int = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None or number == None:
        msg.add_field(name=":warning: ", value="`h!chocolate <user> <amount>`")
    else:
        if number > 100:
            msg.add_field(name=":warning: ", value="`You can't give over 100 chocolates to someone! They gon get real fat...`")
        else:
            msg.add_field(name=":smiley: ", value="`{} gave {}` :chocolate_bar: `to {}!`\n`Be like {}!`".format(author.display_name, number, userName.display_name, author.display_name))
    await client.say(embed=msg)
    print("============================================================")
    print("}chocolate <user> <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }cookie <user> <number>
@client.command(pass_context=True)
async def cookie(ctx, userName: discord.Member = None, number: int = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None or number == None:
        msg.add_field(name=":warning: ", value="`h!cookie <user> <amount>`")
    else:
        if number > 100:
            msg.add_field(name=":warning: ", value="`You can't give over 100 cookie to someone! Tryna give them diabetes?!`")
        else:
            msg.add_field(name=":smiley: ", value="`{} gave {}` :cookie: `to {}!`\n`Be like {}!`".format(author.display_name, number, userName.display_name, author.display_name))
    await client.say(embed=msg)
    print("============================================================")
    print("}chocolate <user> <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
client.run(os.environ['BOT_TOKEN'])
