import discord
from discord.ext import commands
import datetime
import requests
from urllib import parse, request
import re
import os
import time
import requests, json
from colorama import Fore, init
import os
from os import system
import pytz
from discord.ext.commands import has_permissions, CheckFailure, CommandNotFound
bot = commands.Bot(command_prefix='?', description="Suzuya | SearchEngine")

bot.remove_command("help")

ROLEIDCLIENT = METTRE UN ID DE ROLE (pour avoir acces a la commande search)
ROLEOWNERID = METTRE UN ID DE ROLE (pour les owners)
ROLEBLACKLISTUSER = METTRE UN ID DE ROLE (pour gerer les blacklists)







#--COMMANDS--#
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    print(f"PONG {latency}ms")
    
    await ctx.send(f'pong: {latency}ms')






#BLLLLLALCCCCCKKKKKK LLLLLIIIIIISSTTTTTTTTTT#




blacklistuserfile = "blacklistuser"
blacklistuserfileread = open(f"{blacklistuserfile}.txt", "r")
content = blacklistuserfileread.read()
blacklistuserlist = content.split("\n")
blacklistuserfileread.close()




@bot.command()
async def bl(ctx):
    embed = discord.Embed(colour= discord.Colour.red())

    embed.set_author(name="Blacklist  ⬛")
    embed.add_field(name="BlackList", value="\n`?listbl`")
    embed.add_field(name="Add BlackList", value="\n`?addbl pseudo`")
    embed.add_field(name="Remove BlackList", value="\n`?rmbl pseudo`")

    await ctx.send(embed=embed)
    print(f"Help blacklist:  {ctx.author.name} | {ctx.author.id}")
    ##savelogs(f"Help blacklist:  {ctx.author.name} | {ctx.author.id}")

@bot.command() 
@commands.has_role(ROLEBLACKLISTUSER)
async def listbl(ctx):
    listbl = ['']
    f = open(f"{blacklistuserfile}.txt", "r")
    for i in f:
        #await ctx.send(f"`{i}`")
        listbl.append(i)
    f.close()
    listbla = ''.join(listbl)
    embed = discord.Embed(colour= discord.Colour.red())
    #embed.set_author(name=u"\U0001F575" f" - List of Blacklisted:")
    if listbla != "":
        embed.add_field(name=u"\U0001F575" + " - List of Blacklisted:", value=f"`{listbla}`")
        await ctx.send(embed=embed)
    else:
        embed.add_field(name=u"\U0001F575" + " - List of Blacklisted:", value=f"`Aucun utilisateur présent.`")
        await ctx.send(embed=embed)
    print(f"List blacklist: by {ctx.author.name} | {ctx.author.id}.")
    ##savelogs(f"List blacklist: by {ctx.author.name} | {ctx.author.id}.")
@listbl.error
async def listbl_error(ctx, error):
    embed = discord.Embed(colour= discord.Colour.red())
    embed.set_author(name= u"\U0000274c" + f" - You have not permission for this commands")
    await ctx.send(embed=embed)


@bot.command() 
@commands.has_role(ROLEBLACKLISTUSER)
async def addbl(ctx, *, message):
    f = open(f"{blacklistuserfile}.txt", "a")
    f.write(f"{message}\n")
    f.close()
    embed = discord.Embed(colour= discord.Colour.red())
    #embed.set_author(name=u"\U0001F575" f" - List of Blacklisted:")
    embed.add_field(name=u"\U0001F575" + " - Add of Blacklisted:", value=f"`{message}`")
    await ctx.send(embed=embed)
    print(f"Add blacklist:  {message} by {ctx.author.name} | {ctx.author.id}.")
    #savelogs(f"Add blacklist:  {message} by {ctx.author.name} | {ctx.author.id}.")
@addbl.error
async def addbl_error(ctx, error):
    embed = discord.Embed(colour= discord.Colour.red())
    embed.set_author(name= u"\U0000274c" + f" - You have not permission for this commands")
    await ctx.send(embed=embed)


@bot.command() 
@commands.has_role(ROLEBLACKLISTUSER)
async def rmbl(ctx, *, message):
    f = open(f"{blacklistuserfile}.txt", "r")
    lines = f.readlines()
    f.close()

    f = open(f"{blacklistuserfile}.txt", "w")
    for line in lines:
        # readlines() includes a newline character
        if line.strip("\n") != message:
            f.write(line)

    f.close()
    embed = discord.Embed(colour= discord.Colour.red())
    embed.add_field(name=u"\U0001F575" + " - Remove of Blacklisted:", value=f"`{message}`")
    await ctx.send(embed=embed)
    print(f"Remove blacklist:  {message} by {ctx.author.name} | {ctx.author.id}.")
    #savelogs(f"Remove blacklist:  {message} by {ctx.author.name} | {ctx.author.id}.")
@rmbl.error
async def rmbl_error(ctx, error):
    embed = discord.Embed(colour= discord.Colour.red())
    embed.set_author(name= u"\U0000274c" + f" - You have not permission for this commands")
    await ctx.send(embed=embed)
    





@bot.command() 
async def example(ctx, *, message): 
    for i in blacklistuserlist:
        if i not in message: 
            #await ctx.send(f"good :flushed: {message}")  
            apa = "apa"
            print(apa)
            continue
        else: 
            await ctx.send(f"blacklist :flushed: {message}") 
            break

#STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPPPPPPPPPPPPP##

#--SQKLDJLQSKJDLKQSJDKLQ--#

def check_blacklist(argument):
    blacklist = open(f'{blacklistuserfile}.txt', 'r')
    bl_user = blacklist.read().split('\n')
    for i in bl_user:
        if i == argument:
            return "BLACKLIST"
    return "WHITELIST"


def get_files(search_path):
    for (dirpath, _, filenames) in os.walk(search_path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def savelogs(goodlogs):
    
    t = time.localtime()
    current_time = time.strftime("%A_%d_%B_%Y", t)
    f = open(f"{current_time}.log", "a")




    paris = pytz.timezone('Europe/Paris')
    datetime_paris = datetime.now(paris)
    temptime = datetime_paris.strftime("%H:%M:%S")

    f.write(f"{temptime} - {goodlogs}")
    f.close










@bot.command()
@commands.has_role(ROLEIDCLIENT)
async def search(ctx, *, message):
    cd = check_blacklist(message)
    if cd != "BLACKLIST":

        numberis = 0
        list_files = get_files('database')
        list_line = ['']
        emoji = discord.utils.get(bot.emojis, name='ld')
        amessage = await ctx.send(f"wait {str(emoji)}")


        if len(message) >= 2:
            for filename in list_files:
                numberis = numberis + 1
                gr = filename.split("\\")
                nameoffiledir = gr[1]
                nameoffile = nameoffiledir.split(".")[0]

                file = open(f"database/{nameoffiledir}", "r", encoding="utf8", errors='ignore')
                line_count = 0
                for line in file:
                    if line != "\n":
                        line_count += 1
                        if message in line:
                            #print(line)^
                            for words in [f'{message}']:
                                if re.search(r'\b' + words + r'\b', line):
                                    embed = discord.Embed(colour= discord.Colour.red())
                                    
                                    embed.set_author(name="search  👨‍💻")
                                    embed.add_field(name=f"{nameoffile}", value=f"`{line}`")

                                    await ctx.send(embed=embed)

                                    text = "Résultats: "

                                    list_line.append(text)
                file.close()

                grrsqlkdjqlsd = ' '.join(list_line)
            if len(grrsqlkdjqlsd) < 1999 :
                if 2 < len(grrsqlkdjqlsd):
                    await amessage.edit(content=f"```{grrsqlkdjqlsd}```")
                else:
                    await amessage.edit(content="I find nothing")
            else:
                await amessage.edit(content=f"TROP GRO WSH {len(grrsqlkdjqlsd)}")


        else:
            await ctx.send(f"Trop petit essaye a partire de 5 (recommandé) : {len(message)}")
        print(f"Suzugras of {message} by {ctx.author.name} | {ctx.author.id}.")
        #savelogs(f"PwndMC of {message} by {ctx.author.name} | {ctx.author.id}.")
    else:
        embed = discord.Embed(colour= discord.Colour.red())
        embed.set_author(name= u"\U0000274c" + f" - {message} is blacklist " + u"\U0001F575")
        await ctx.send(embed=embed)
        print(f"search Commands: by {ctx.author.name} | {ctx.author.id}.")
@search.error
async def search_error(ctx, error):
    embed = discord.Embed(colour= discord.Colour.red())
    embed.set_author(name= u"\U0000274c" + f" - {error}")
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(colour= discord.Colour.red())

    embed.set_author(name="Help 🆘")
    embed.add_field(name="search", value="`?search <Pseudo>`")
    embed.add_field(name="Blacklist", value="`?bl`")
    embed.add_field(name="Ping", value="`.ping`")
    embed.add_field(name="History", value="`?history <Pseudo>`")
    await ctx.send(embed=embed)
    print(f"Help Commands: by {ctx.author.name} | {ctx.author.id}.")
    #savelogs(f"Help Commands: by {ctx.author.name} | {ctx.author.id}.")


@bot.command()
async def history(ctx, *, message):
    
    findemsg = ['']
    pseudousername = ['']
    pseu = 0
    code = requests.get("https://api.ashcon.app/mojang/v2/user/" + message).status_code #Request name data
    if code == 200:
        resp = requests.get("https://api.ashcon.app/mojang/v2/user/" + message)
        data = json.loads(resp.text)
        pseudogood = f"[+] Pseudo: " + data["username"] 
        #findemsg.append(pseudogood)
        uuidmc = "[+] UUID: " + data["uuid"]
        #findemsg.append(uuidmc)
        if data["created_at"] == None:
            createdat = f"\n[-] Created the: Not found"
            msgcrea = "Not found"
        else:
            createat = f"\n[*] Created the: " + data["created_at"] + "\n[+] Name History: \n"
            msgcrea = f'{data["created_at"]}'
        for username in data["username_history"]: #Get username history
            pseu = pseu + 1
            try:
                chang = username["changed_at"].replace('T', ' at ').replace('.000Z', '')
                logsusername = f'   =>  [{pseu}] {username["username"]} (Changed {chang})'
                pseudousername.append(logsusername)
            except:
                chang = data["created_at"]
                logsusername = f'   =>  [{pseu}] {username["username"]} (Frist Name)'
                pseudousername.append(logsusername)

    pseudousernames = '\n'.join(pseudousername)
    embed = discord.Embed(colour= discord.Colour.red(), description=f"**History: **`{pseudousernames}`")
    embed.set_author(name=f"{pseudogood}")
    uuidmin = data["uuid"]
    embed.add_field(name=f"UUID: ", value=f"`{uuidmin}`")
    embed.add_field(name=f"Created the:", value=f"`{msgcrea}`")
    #embed.add_field(name=f"History", value=f"`{pseudousernames}`", inline=False)
    await ctx.send(embed=embed)
    print(f"History of:  {message} by {ctx.author.name} | {ctx.author.id}.")
    #savelogs(f"History of:  {message} by {ctx.author.name} | {ctx.author.id}.")
@history.error
async def history_error(ctx, error):
    embed = discord.Embed(colour= discord.Colour.red())
    embed.set_author(name= u"\U0000274c" + f" - Enter a good pseudo/uuid mc.")
    await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    
    os.system("cls")
    activitybot = activity=discord.Activity(type=discord.ActivityType.listening, name="Suzuya Le Best")
    await bot.change_presence(status=discord.Status.idle, activity=activitybot)
    system("mode 65, 30")
    system(f"title [ PANEL OF {bot.user.name} ]")
    print(f"Connected to Bot: {bot.user.name}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Currently in: {len(bot.guilds)} server(s)!")
    print(f"Latency : {round(bot.latency * 1000)} ms")
    time.sleep(5)
    t = time.localtime()
    current_time = time.strftime("%A_%d_%B_%Y", t)
    print("\n\nLOGS","-"*25, f"{current_time}.txt", "-"*6)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        pass


bot.run('OTc2OTEyMTM0Mjk2NDU3MjU2.GLAj8x.IZ08zpFXuUv75yC-R04WflNULIvL3Q-QgKGuhk')
