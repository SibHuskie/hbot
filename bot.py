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
    
# }cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":tongue: Emotes :tongue:", value="`{} is crying! *Pat pat pat*`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://media.tenor.com/images/d571f86a5adcb4545444e9d1dc4638f9/tenor.gif",
            "https://i.pinimg.com/originals/73/3d/59/733d5948098702b0d6f156819143b581.gif",
            "https://67.media.tumblr.com/aa7766807df523677bb9c73da94ee049/tumblr_npwxeb2dPp1u7ltf6o1_500.gif",
            "https://static2.fjcdn.com/thumbnails/comments/I+actually+dont+remember+i+think+because+of+the+horns+_78025db895d293c2765eaace345742f0.gif"]

# }slap <user>
@client.command(pass_context=True)
async def slap(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`h!slap <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":tongue: Emotes :tongue: ", value="`{}, you got slapped by {}! Ouch...`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}slap <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]

# }hide
@client.command(pass_context=True)
async def hide(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(hidelinks)))
    msg.add_field(name=":tongue: Emotes :tongue:", value="`{} is hiding!`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

hidelinks = ["http://www.gifbin.com/bin/012011/1295259460_cat-hides-in-box.gif",
             "https://www.cat-gifs.com/w3/Funny-Cat-GIF-Weird-Black-Cat-with-big-round-eyes-tries-to-hide-in-his-small-green-box.gif",
             "http://www.letssmiletoday.com/uploads/images/9642-Quick_hide_in_the_box_20.04.2012.gif",
             "https://i.gifer.com/VfBm.gif",
             "https://i.imgur.com/gFMNHyA.gif",
             "https://i.imgur.com/UXSe4sQ.gif",
             "https://i.chzbgr.com/full/7074625536/hD0F6F5CE/"]

# <punch <user>
@client.command(pass_context=True)
async def punch(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`h!punch <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(punchlinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got a punch from by {}! Ouch...`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
punchlinks = ["http://www.reactiongifs.com/wp-content/uploads/2013/11/punch.gif",
              "https://media.giphy.com/media/7Nsu3HCWLRVgQ/giphy.gif",
              "https://media1.tenor.com/images/3aa0da04ef714f758c9ed215e629c161/tenor.gif?itemid=4902916",
              "https://i.pinimg.com/originals/f6/d9/1c/f6d91c1f8a29b0131d448bad244dbeba.gif"]    

# <sorry <user>
@client.command(pass_context=True)
async def sorry(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`h!sorry <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(sorrylinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, {} is saying sorry!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

sorrylinks = ["https://i.imgur.com/9f2FsAQ.gif",
            "https://i.imgur.com/9f2FsAQ.gif",
            "https://i.imgur.com/9f2FsAQ.gif"]

# <spank <user>
@client.command(pass_context=True)
async def spank(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`h!spank <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{} spanked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}spank <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

# <poke <user>
@client.command(pass_context=True)
async def poke(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`h!poke <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(pokelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got poked by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}poke <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

# <kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xcc1625, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`h!kiss <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got kissed by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

kisslinks = ["https://media1.tenor.com/images/9c92434bdeea2df04d67710f338b212d/tenor.gif?itemid=5223535",
             "https://media1.tenor.com/images/e88bcd916c0da114a8dcac8d9babc77c/tenor.gif?itemid=5052769",
             "https://m.popkey.co/96c6ee/4QVgR_s-200x150.gif",
             "https://i.gifer.com/9NC8.gif",
             "http://gifimage.net/wp-content/uploads/2017/10/morning-kiss-gif-11.gif",
             "https://thumbs.gfycat.com/LateAchingHoatzin-max-1mb.gif",
             "https://media1.tenor.com/images/b7cf0d7ff5c2bb274e8cdc6d5a87d91d/tenor.gif?itemid=5636758"]
client.run(os.environ['BOT_TOKEN'])
