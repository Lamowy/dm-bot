import asyncio
import math
import os
import discord
import time
import random
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta, timezone

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='w?', intents=intents)

@bot.command('informacja')
async def cmd(ctx, *args):
    if not ctx.author.guild_permissions.manage_guild:
        await ctx.reply("You're not supposted to use this command.")
        return
    guild = ctx.author.guild
    members = guild.members
    i = 0
    j = 0
    m = 0
    l = 0
    start = time.time()
    list = []
    with open('member.txt', 'r') as f:
        for li in f.readlines():
            list.append(int(li.strip()))
    memb = []
    bb = 0
    for member in members:
        if member.id in list:
            print("Member count: " + str(bb))
            bb += 1
            continue
        else:
            memb.append(member)

    bb = 0
    for mem in memb:
        if mem.bot:
            continue
        try:
            await mem.send(' '.join(args).replace("%nl%", "\n").replace("%n", "\n").replace("%s", " ") + f'\n {random.randint(1, 999999999999999)}')
            i += 1
            with open('member.txt', 'a') as f:
                f.write(str(mem.id) + "\n")
            print(i)
        except discord.Forbidden as e:
            print(str(e))
            j += 1
            continue
        
                
        l -= 1
        end = time.time()
        m = end - start
        if i % 10 == 0:
            await ctx.reply(f'[PRZYPOMNIENIE] {i} wiadomości, {j} niewysłanych wiadomości. ({int(m)}s)')
        if i % 50 == 0:
            await asyncio.sleep(60)
        if i % 400 == 0:
            break
        await asyncio.sleep(1)
    end = time.time()
    m = end - start

    await ctx.reply(f'Udało się wysłać wiadomość: \"{" ".join(args)}\" {i} użytkownikom serwera, {j} niewysłanych wiadomości. ({int(m)}s)')

bot.run('YOUR_TOKEN')
