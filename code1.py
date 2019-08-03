import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
from discord import Spotify
import os
import functools
import time
import datetime
import requests
import json
import aiohttp		


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0xf9fcfc)
client = commands.Bot(description="cry n___ bot", command_prefix=commands.when_mentioned_or(">"), pm_help = True)

client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(">help",))
	
	
async def task():
    while True:
        channel = client.get_channel(605305731209494528)
        address = "https://www.rrrather.com/botapi"
        data = requests.get(address).json()
        nsfw_check = data['nsfw']
        if nsfw_check == False:
            embed = discord.Embed(title=data['title'], description=f"**1){data['choicea']} \n \n2){data['choiceb']}** \n \n[Wanna know what others said about this question in www.rrrather.com? Click me...]({data['link']})", color=0xff69bf)
            embed.set_author(name="It's question time folks...", icon_url=channel.guild.icon_url)
            embed.set_footer(text=channel.guild.name)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
            await asyncio.sleep(10)
        elif nsfw_check == True:
            await asyncio.sleep(1)	


@client.event
async def on_ready():
    #print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.guilds))+' guilds | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started new here ')
    print('Created by MARCOS々DMRY')
    client.loop.create_task(status_task()) 

	
@client.event
async def on_member_join(member):
    channel = client.get_channel(593696190730862592)
    person_count = len([member for member in member.guild.members if not member.bot])
    embed = discord.Embed(title=f'Welcome {member.name} to {member.guild.name}', description='**__Thanks for Joining__**', color=0X333233)
    embed.set_thumbnail(url=member.avatar_url) 
    embed.set_image(url=member.avatar_url)
    embed.add_field(name='__Join position__', value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.add_field(name='Time of joining', value=member.joined_at.date(), inline=True)
    await channel.send(channel, embed=embed)    

	
@client.command(pass_context = True)
async def meme(ctx):
    embed = discord.Embed(title=" :sunglasses: meme :sunglasses: ", color=0XF9FCFC)
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()          
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
	
#@client.command(pass_context=True)
#async def test(ctx):
	#await ctx.send("Hello")
	
	
@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, number: int):
  await ctx.message.channel.purge(limit=number+1)


@client.command(pass_context = True)
async def announce(ctx, channel: discord.TextChannel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await ctx.send('```Proper usage is \n\n>announce #channel matter```')
        return
    else:
        if member.guild_permissions.administrator == False:
            await ctx.send('**You Do Not Have Permission To Use This Command**')
            return
        else:
            await channel.send(msg)

	
@client.command(pass_context = True)
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
      await ctx.send('```The proper usage is \n>userinfo <@user>```')
      return
    else:
      gettime = discord.utils.snowflake_time(member.id)
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0Xf9fcfc)
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.add_field(name='Account created at', value=gettime.date(), inline=True)
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
      await ctx.send(embed=embed)
	

@client.command(pass_context=True)
@commands.has_permissions(manage_roles = True)
async def roleinfo(ctx, role: discord.Role=None):
    embed = discord.Embed(title=f"Here's the info of {role} role...", description=" ", color=role.color)
    embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
    embed.add_field(name="ID", value=role.id, inline=False)
    embed.add_field(name="Name", value=role.name, inline=False)
    embed.add_field(name="Permissions", value=role.permissions, inline=False)
    embed.add_field(name="Guild", value=ctx.guild.name, inline=False)
    embed.add_field(name="The role is shown seperately from others", value=role.hoist, inline=False)
    embed.add_field(name="Position of the role", value=role.position, inline=False)
    embed.add_field(name="Time of creation", value=role.created_at.strftime("%d-%m-%Y %H:%M:%S"), inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
	

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(title='user- {}'.format(ctx.message.author.name), color=0Xf9fcfc)
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

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def poll(ctx, question, *options: str):
    if len(options) <= 1:
        await ctx.send('You need more than one option to make a poll!')
        return
    if len(options) > 10:
        await ctx.send('You cannot make a poll for more than 10 things!')
        return
    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['👍', '👎']
    else:
        reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n{} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description), color=0Xf9fcfc)
            react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
            embed.set_footer(text=f"Poll ID: {react_message.id}",)
            await react_message.edit(embed=embed)


@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    if user.id == ctx.message.author.id:
        await ctx.send("Goodluck slaping yourself {}".format(ctx.message.author.mention))
    else:
        gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color=0Xf9fcfc)
        embed.set_image(url=random.choice(gifs))
        await ctx.send(embed=embed)	

	

@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("```Proper usage is\n\n>kiss <mention a user>```")
    if user.id == ctx.message.author.id:
        await ctx.send("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color=0Xf9fcfc)
        embed.set_image(url=random.choice(randomurl))
        await ctx.send(embed=embed)	

	
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("```Proper usage is\n\n>hug <mention a user>```")
    if user.id == ctx.message.author.id:
        await ctx.send("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color=0Xf9fcfc)
        embed.set_image(url=random.choice(randomurl))
        await ctx.send(embed=embed)  	
	
	
@client.command(pass_context = True)
async def botinfo(ctx):
    User = await client.fetch_user('498378677512437762')
    User2 = await client.fetch_user('472128507150073871')
    User3 = await client.fetch_user('591996301311213598')
    User4 = await client.fetch_user('539799864272486411')
    embed = discord.Embed(title="CRY N____ information", color=0Xf9fcfc)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/592605488265428992/593310963034226693/mimikyu-2-622x350.png")
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f"This is Official BOT of {ctx.guild.name} server")
    embed.add_field(name="__**Bot name**___", value="CRY N____", inline = True)
    embed.add_field(name="__**Bot id**__", value="520267296506249216", inline = True)
    embed.add_field(name="__**Bot prefix**__", value="!!", inline = True)
    embed.add_field(name="__**Bot language**__", value="Python", inline = True)
    embed.add_field(name="__**Creator**__", value=User.mention, inline = True)
    embed.add_field(name="__**Special Thanks To**__", value=f"{User2.mention} \n{User3.mention} \n{User4.mention}")
    embed.add_field(name="__**Currently Connected Servers**__", value=str(len(client.guilds)), inline = True)
    embed.add_field(name="__**Currently Connected Users**__", value=str(len(set(client.get_all_members()))), inline = True)
    embed.add_field(name="If you have any queries about this BOT, DM me...", value=User.mention)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)	


@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
    await ctx.trigger_typing()
    if name is None:
        embed=discord.Embed(description = "Please specify a movie, *eg. %movie Bohemian Rhapsody*", color = 0Xf9fcfc)
        await ctx.send(embed=embed)
    key = "4210fd67"
    url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
    response = requests.get(url)
    x = json.loads(response.text)
    embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = 0Xf9fcfc)
    if x["Poster"] != "N/A":
     embed.set_thumbnail(url = x["Poster"])
    embed.add_field(name = "__Title__", value = x["Title"])
    embed.add_field(name = "__Released__", value = x["Released"])
    embed.add_field(name = "__Rated__", value = x["Rated"])
    embed.add_field(name = "__Runtime__", value = x["Runtime"])
    embed.add_field(name = "__Genre__", value = x["Genre"])
    embed.add_field(name = "__Director__", value = x["Director"])
    embed.add_field(name = "__Writer__", value = x["Writer"])
    embed.add_field(name = "__Actors__", value = x["Actors"])
    embed.add_field(name = "__Plot__", value = x["Plot"])
    embed.add_field(name = "__Language__", value = x["Language"])
    embed.add_field(name = "__Box Office__", value = x['BoxOffice'])
    embed.add_field(name = "__Awards__", value = x['Awards'])
    embed.add_field(name = "__Production__", value = x["Production"])
    embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
    embed.add_field(name = "__Type__", value = x["Type"])
    embed.set_footer(text = "Information from the OMDB API")
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()       
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color=0Xf9fcfc)
            embed.set_image(url=res['message'])
            embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)	

		
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await ctx.send(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await ctx.edit(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await ctx.edit(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await ctx.edit(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await ctx.edit(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await ctx.edit(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await ctx.edit(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await ctx.edit(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await ctx.edit(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await ctx.edit(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await ctx.edit(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await ctx.edit_(x,'``Injecting virus....\``')
    await ctx.delete(x)
    await ctx.delete(ctx)
        
    if user:
        await ctx.send('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await ctx.send(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await ctx.send('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await ctx.send(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
			
		
	
@client.command(pass_context=True, no_pm=True, aliases=["Bird"])
async def bird(ctx):
    try:
        url = "http://shibe.online/api/birds?count=1&urls=true&httpsUrls=false"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Bird {}".format(ctx.message.author.name),)
        embed.set_image(url = data[0])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    except:
        x = await ctx.send("Sorry, there was an error with the **bird** command")
        await asyncio.sleep(5)
        await x.delete()

	
@client.command(pass_context=True, no_pm=True, aliases=["Dog"])
async def dog(ctx):
    try:
        url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Dog {}".format(ctx.message.author.name),)
        embed.set_image(url = data[0])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    except:
        x = await ctx.send("Sorry, there was an error with the **dog** command")
        await asyncio.sleep(5)
        await x.delete()


@client.command(pass_context=True, no_pm=True, aliases=["Cat"])
async def cat(ctx):
    try:
        url = "http://shibe.online/api/cats?count=1&urls=true&httpsUrls=false"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Cat {}".format(ctx.message.author.name),)
        embed.set_image(url = data[0])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    except:
        x = await ctx.send("Sorry, there was an error with the **cat** command")
        await asyncio.sleep(5)
        await x.delete()
	

@client.command(pass_context=True, no_pm=True, aliases=["Fox"])
async def fox(ctx):
    try:
        url = "https://randomfox.ca/floof"
        response = requests.get(url)
        data = json.loads(response.text)
        embed=discord.Embed(color=0Xf9fcfc)
        embed.set_author(name =  "Here's Your Fox {}".format(ctx.message.author.name),)
        embed.set_image(url = data["image"])
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    except:
        x = await ctx.send("Sorry, there was an error with the **fox** command")
        await asyncio.sleep(5)
        await x.delete()
	

@client.command(pass_context=True)
async def animeshow(ctx, *, name:str = None):
    api_address = f"https://kitsu.io/api/edge/anime?filter[text]={name}"
    data = requests.get(api_address).json()
    url = data['data'][0]['links']['self']
    data2 = requests.get(url).json()
    end_date = data2['data']['attributes']['endDate']
    synopsis = data2['data']['attributes']['synopsis']
    if len(synopsis) > 1024:
        synopsis = "Oh no! The length of synopsis is very large, I can't print it here"
    else:
        synopsis = synopsis
    if end_date == None:
        end_date = "Not finished yet"
    else:
        end_date = end_date
    ytlink = data2['data']['attributes']['youtubeVideoId']
    await ctx.trigger_typing()
    embed = discord.Embed(title="Here's the anime show that you've searched for...", color=0XFF69BF)
    embed.add_field(name="Name", value=f"{data2['data']['attributes']['titles']['en'] } ({data2['data']['attributes']['titles']['ja_jp']})")
    embed.add_field(name="Synopsis", value=synopsis)
    embed.add_field(name="Average Rating", value=data2['data']['attributes']['averageRating'])
    embed.add_field(name="Start Date", value=data2['data']['attributes']['startDate'])
    embed.add_field(name="End Date", value=end_date)
    embed.add_field(name="Age Rating", value=data2['data']['attributes']['ageRating'])
    embed.add_field(name="Age Rating Guide", value=data2['data']['attributes']['ageRatingGuide'])
    embed.add_field(name="Type of Media", value=data2['data']['attributes']['subtype'])
    embed.add_field(name="Status", value=data2['data']['attributes']['status'])
    embed.set_thumbnail(url=data2['data']['attributes']['posterImage']['original'])
    embed.add_field(name="Episode Count", value=data2['data']['attributes']['episodeCount'])
    embed.add_field(name="Episode Length", value=data2['data']['attributes']['episodeLength'])
    embed.add_field(name="Youtube link", value=f"[Click here for trailer](https://www.youtube.com/watch?v={ytlink})")
    embed.add_field(name="NSFW", value=data2['data']['attributes']['nsfw'])
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested By | {ctx.author.name}")
    await ctx.send(embed=embed)	
	
	
	
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def spam(ctx, count: int, *, SecretCocoSpam: str):
        await ctx.message.delete()
        for i in range(count):
            await asyncio.sleep(5.0)
            await ctx.send(SecretCocoSpam)
        else:
            return; 


#@client.command(pass_context=True)
#async def joke(ctx):
#    res = requests.get(
#            'https://icanhazdadjoke.com/',
#             headers={"Accept":"application/json"}
#             )
#    if res.status_code == requests.codes.ok:
#        await ctx.send(str(res.json()['joke']))
#    else:
#        await ctx.send('oops!I ran out of jokes')

@client.command(pass_context=True,)
async def joke(ctx):
    x = await ctx.send("CRY N____ is thinking of a joke.")
    await asyncio.sleep(1)
    await x.edit(content="CRY N____ is thinking of a joke..")
    await asyncio.sleep(1)
    await x.edit(content="CRY N____ is thinking of a joke...")
    await asyncio.sleep(1)
    await x.edit(content="CRY N____ is thinking of a joke....")
    await asyncio.sleep(1)
    await x.edit(content="CRY N____ is thinking of a joke.....")
    await asyncio.sleep(1)
    res = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
    if res.status_code == requests.codes.ok:
        await x.edit(content=str(res.json()['joke']))
    else:
        await x.edit(context="oops!I ran out of jokes...")    
		    
		    
@client.command(pass_context=True)
async def lyrics(ctx, *, track:str = None):
    address = f"https://some-random-api.ml/lyrics?title={track}"
    data = requests.get(address).json()
    if 'error' in data:
        await ctx.send(f"**{data['error']}**")
    else:
        lyrics = data['lyrics']
        if len(lyrics) < 2048:
            for chunk in [lyrics[i:i+2000] for i in range(0, len(lyrics), 2000)]:
                embed = discord.Embed(title=data['author'], description=f"{chunk} \n [Source website]({data['links']['genius']})", color=0XFF69BF)
                embed.set_author(name=data['title'], url=data['thumbnail']['genius'])
                embed.set_thumbnail(url=data['thumbnail']['genius'])
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(f"**{ctx.author.name},** The lyrics of **{data['author']} - {data['title']}** is sent to your DM please check your DM's...")
                await ctx.author.send(embed=embed)
        
        else:
            await ctx.send(f"**{ctx.author.name},** The lyrics of **{data['author']} - {data['title']}** is sent to your DM please check your DM's...")
            for chunk in [lyrics[i:i+2000] for i in range(0, len(lyrics), 2000)]:
                await ctx.author.send(chunk)           


@client.command(pass_context=True, aliases=["t"])
async def talk(ctx, message: str = None,):
    if message == None:
        await ctx.send("**CRY N__ can't talk to you unless you say anything to me ``>talk <message>``**")
    else:
        address = f"https://some-random-api.ml/chatbot?message={message}"
        data = requests.get(address).json()
        reply = data['response']
        await ctx.trigger_typing()
        await asyncio.sleep(1)
        await ctx.send(reply) 

			   			  
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def information(ctx):
    rule_1 = "The head honchos of the server.\n<@591996301311213598>"
    rule_2 = "The senior staff members of the server, these users solve staffs' problems, and manages the server's activities.\n<@586190462331912192>\n<@498378677512437762>"
    rule_3 = "These users keep the server safe from harm and should be the first people you message should you need help.\n<@436422568849702942>"
    rule_4 = "These users are the junior staff members, who moderate the chats and delete inappropriate messages.\nnone"
    embed = discord.Embed(title="**STAFF ROLES**", description="These people ensure that the usage of this environment reflects the guidelines as illustrated in the rules. Staff are sometimes handpicked, and sometimes there is an application process. They help to moderate and enhance the server, and always have the final decision.", color=0X333331)
    embed.add_field(name="OWNER", value=rule_1, inline=False)
    embed.add_field(name="ADMINISTRATOR", value=rule_2, inline=False)
    embed.add_field(name="SENIOR MODERATOR", value=rule_3, inline=False)
    embed.add_field(name="CHAT MODERATOR", value=rule_4, inline=False)
    await ctx.send(embed=embed)
	

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def links(ctx):
    rule_1 = "https://discord.gg/gdK3xBN"
    rule_2 = "<@602824587629297664> [click to invite](https://discordapp.com/api/oauth2/authorize?client_id=602824587629297664&permissions=130065&scope=bot)"
    rule_3 = "<@592988250591985715> [click to invite](https://discordapp.com/api/oauth2/authorize?client_id=592988250591985715&permissions=8&scope=bot)"
    embed = discord.Embed(title="**SEXTERNAL LINKS**", description="In this section, you will find some of the common links related to the server.", color=0X333331)
    embed.add_field(name="Server Invite link", value=rule_1, inline=False)
    embed.add_field(name="POKECORD GURU invite link", value=rule_2, inline=False)
    embed.add_field(name="CRY N____invite link", value=rule_3, inline=False)
    await ctx.send(embed=embed)

			   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def rules(ctx):
    rule_1 = ":fire: Follow and Respect the Rules :fire:\n:fire: Respect all members at all times.\n:fire: No spam or advertising of other Discord servers.\n:fire: No mic spam or voice channel annoyance (this goes for hopping too)\n:fire: No PM harassment (suggest you modify your privacy settings to prevent any occurrences).\n:fire: No racism or bigotry allowed.\n:fire: No begging for roles or permissions.\n:fire: No marketing, this is not the place to sell anything.\n:fire: No 'self-bots' these are quite an annoyance.\n:fire: Do not argue with members of staff, their decision is final.\n:fire: No staff impersonation\n:fire: Don't Do Dm Advertise Or You got A Permanent Ban.\n:fire: No spam  advertising of your Discord servers.\n:fire: Do not use bot commands in any other channel than #bot-spam.\n\nx-----------------------ThankYou !!! :D-----------------------x"
    embed = discord.Embed(title="SERVER RULES", description=None, color=0X333331)
    embed.add_field(name="🛡️ Have a Great Time Here in This Discord Server 🛡️", value=rule_1, inline=False)
    await ctx.send(embed=embed)
			   
		   			   
@client.command(pass_context=True, aliases=["Help"])
async def help(ctx):
    embed = discord.Embed(color=0Xf9fcfc)
    embed.set_author(name="Command prefix: >")
    embed.add_field(name="__Administrator commands__", value="`serverinfo  󠇰󠇰 :` server's information . \n`membercount  󠇰󠇰:` how many servers mamber in. \n`poll  󠇰󠇰   󠇰󠇰   󠇰󠇰󠇰󠇰 :` Polling . \n`ban  󠇰󠇰   󠇰󠇰  󠇰󠇰   :` ban the user. \n`clear  󠇰󠇰   󠇰 󠇰󠇰 󠇰󠇰 :` clear messages. \n`announce   󠇰󠇰  󠇰󠇰󠇰󠇰:` To announce the entered **#channel** n **matter** . ", inline=True)
    embed.add_field(name="__Animals commands__", value="`fox  󠇰󠇰   󠇰󠇰  󠇰󠇰   󠇰󠇰:` fox images. \n`dog   󠇰󠇰  󠇰󠇰   󠇰󠇰 󠇰󠇰 :` dog images. \n`cat   󠇰󠇰   󠇰󠇰 󠇰󠇰   󠇰󠇰:` cat images. \n`bird   󠇰󠇰   󠇰󠇰  󠇰󠇰󠇰󠇰 :` bird images. ")
    embed.add_field(name="__Info commands__", value="`botinfo   󠇰󠇰 󠇰󠇰 󠇰󠇰 :` Information about this BOT. \n`userinfo  󠇰󠇰 󠇰󠇰 󠇰󠇰 :` user's information. \n `ping  󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰  󠇰󠇰 󠇰󠇰 :` pong. \n`movie  󠇰󠇰 󠇰󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰 󠇰󠇰 󠇰󠇰:` movie name. ")
    embed.add_field(name="__Fun commands__", value="`joke   󠇰󠇰 󠇰󠇰   󠇰󠇰 󠇰󠇰 :` tell you a joke!. ")
    embed.add_field(name="__Images commands__", value="`meme   󠇰󠇰 󠇰󠇰󠇰󠇰 󠇰󠇰 󠇰󠇰  󠇰󠇰 :` meme image. \n`avatar  󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 :` Avatar. \n`marvel  󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 :` Marvel GIF. \n`joker  󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 :` Joker GIF. \n`slap  󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰󠇰󠇰  :` slap the user. \n`hug  󠇰󠇰󠇰󠇰 󠇰󠇰  󠇰󠇰󠇰󠇰  󠇰󠇰 󠇰󠇰 󠇰󠇰 :`  hug a user. \n`kiss 󠇰󠇰 󠇰󠇰  󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 󠇰󠇰 :` kiss the user. \n`lovedetect 󠇰󠇰 󠇰󠇰 :` lovedetect **user1** **user2**. \n\n__**more feautures coming soon...**__")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/592605488265428992/593310963034226693/mimikyu-2-622x350.png') 
    embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()  	
    await ctx.send(embed=embed)
	

client.run(os.getenv('TOKEN')) 
