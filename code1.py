import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp		


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0xf9fcfc)
client = commands.Bot(description="marcos bot", command_prefix=commands.when_mentioned_or("!!"), pm_help = True)

client.remove_command('help')


"""async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='!!help | marcos.#0290', type=2)) 
        await asyncio.sleep(120)
        await client.change_presence(game=discord.Game(name='BETA VERSION')) 
        await asyncio.sleep(120)
        await client.change_presence(game=discord.Game(name='with ' +str(len(set(client.get_all_members())))+' users', type=3))
        await asyncio.sleep(120)"""
		
	
@client.event
async def on_ready():
    #print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started New here ')
    print('Created by marcos')
    #client.loop.create_task(status_task())
	
	
@client.command(pass_context = True)
async def meme(ctx):
    embed = discord.Embed(title="meme", color=0XF9FCFC)
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()          
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
	
@client.command(pass_context=True)
async def test(ctx):
	await ctx.send("Hello")
	
@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, number: int):
  await ctx.message.channel.purge(limit=number+1)


@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(title='User: {}'.format(ctx.message.author.name), color=0Xf9fcfc)
        embed.set_image(url = ctx.message.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f'{ctx.message.author.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='User: {}'.format(user.name), color=0Xf9fcfc)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url = user.avatar_url)
        await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def poll(ctx, question, *options:str):
    if len(options) <=1:
        await ctx.send('Joker needs more than one option to conduct poll!!')
        return
    if len(options) > 10:
        await ctx.send("Joker Can't accept more than 10 options to conduct poll!")
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['👍', '👎']

    else:
        reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description), color=0XFF69B4)
            react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
            embed.set_footer(text='poll ID: {}'.format(react_message.id))
            await react_message.edit(embed=embed)	
	

@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    if user == None:
        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    if user.id == ctx.message.author.id:
        await client.say("Goodluck slaping yourself {}".format(ctx.message.author.mention))
    else:
        gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color=0Xf9fcfc)
        embed.set_image(url=random.choice(gifs))
        await ctx.send(embed=embed)	

	
@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    embed = discord.Embed(color=0Xf9fcfc)
    embed.set_author(name="Command prefix: !!")
    embed.add_field(name="__Administrator commands__", value="`serverinfo  :` server's information . \n`membercount  :` how many servers mamber in. \n`poll  :` Polling . \n`ban  :` ban the user. \n`clear  :` clear messages. \n`announce  :` To announce the entered **#channel** n **matter** . ", inline=True)
    embed.add_field(name="__Fun commands__", value="`virus  :` virus. \n`joke  :` tell you a joke ! . ")	
    embed.add_field(name="__Music commands__", value="`play  :` play the music you want. \n`pause  :` will pause the audio. \n`resume  :` will resume the audio. \n`skip  :` will skip the music. \n`stop  :` will Bot disconnected. \n`song  :` To Check The Current playing song. ") 
    embed.add_field(name="__Animals commands__", value="`fox  :` fox images. \n`dog  :` dog images. \n`cat  :` cat images. \n`bird  :` bird images. ")
    embed.add_field(name="__Games commands__", value="`rps  :` play the rock, paper and scissors.\n`rolldice  :` roll the dice and get 1 to 6 numbers. \n`flipcoin  :` flip the coin. ")
    embed.add_field(name="__Information commands__", value="`botinfo  :` Information about this BOT. \n`userinfo  :` user's information. \n`ping  :` pong.")
    embed.add_field(name="__Images commands__", value="`meme  :` meme image. \n`avatar  :` Avatar. \n`dc  :` DC GIF \n`marvel  :` Marvel GIF. \n`joker  :` Joker GIF. \n`slap  :` slap the user. \n`hug  :`  hug a user. \n`kiss  :` kiss the user. \n`lovedetect  :` lovedetect.  \n\n__support server__ - [click here](https://discord.gg/dFM9HG6) \n__bot invite__ - [click here](https://discordapp.com/api/oauth2/authorize?client_id=520267296506249216&permissions=8&scope=bot) \n\n__**more feautures coming soon...**__")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/537866862600650773/541121180921495554/maxresdefault.jpg') 
    embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()  	
    await ctx.send(embed=embed)
	

client.run(os.getenv('Token')) 
