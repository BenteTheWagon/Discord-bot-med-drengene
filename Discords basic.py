import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
#here i imported every .py library that i am using to code this bot.

Client = discord.Client()
client = commands.Bot(command_prefix = "!!")


chat_filter = ["FUCK", "DICK", "SUCK", "DIE", "BITCH", "FAGGOT", "NIGGER", "SPASTIK", "HORE", "MONGOLOID", "GAY", "LESBIAN", "DEGENERET", "BØSSE", "NEGER", "GRIMME", "KLAMME", "TYKKE", "AUTIST"]
bypass_list = [285061528355471372]

'''
@client.event(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await Client.delete_messages(messages)
    await Client.say('messages deleted.')
'''



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!cmd for commands'))
    print("Bot is Ready!")
#this makes sure that the bot is running, and it will print out ("Bot is ready") in the console, so you know if it'sready or not


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    sentdex_guild = client.get_guild(625613082999390208)
#this gets the servers guild (basically data from the server)

    if "!members" == message.content.lower():
        await message.channel.send(f"There are currently**\n{sentdex_guild.member_count}** members on this discord server!")
    if message.content.lower().startswith("!twitch"):
        await message.channel.send("https://www.twitch.tv/razeonic_")
    if message.content.lower().startswith("!uwu"):
        await message.channel.send("UwU Dwaddy")
    if message.content.lower().startswith("neger"):
        await message.channel.send("Hov.. mener du traditionelle slaver? :thinking:")
    elif message.content.lower().startswith("tak"):
        await message.channel.send("Det var så lidt... UwU")
    if message.content.lower().startswith("denni"):
        await message.channel.send("Mener du Homo denni?")


    if "!cmd" == message.content.lower():
        await message.channel.send(f"These are the current **Commands** that are available.\n **!members** (Gives you the current user count of your discord server)\n **!allmembers** (Gives you a more specific member count)\n **!twitch** (Announces the given twitch channel)")
#This does so if a user types ("!twitch") the bot will respond with the given twitch channel

    elif "!allmembers" == message.content.lower():
            online = 0
            idle = 0
            offline = 0

            for m in sentdex_guild.members:
                if str(m.status) == "online":
                    online += 1
                if str(m.status) == "offline":
                    offline += 1
                else:
                    idle += 1

            await message.channel.send(f"There are currently --->\n**{online}** Online members\n**{offline}** Offline members\n**{idle}** Idle/busy members")

    await client.process_commands(message)
#This is ("!allmembers") and ("!members") it'sprints out the number of members/people there are on the given server






client.run("token")
#This is the bots token, you get this from the discord development page (your bots developer page)
