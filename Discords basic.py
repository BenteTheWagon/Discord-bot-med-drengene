import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(Jeres egen discord bot token)



#Botten kræver at i downloader dotenv.py og discord.py
#i kan download det ved at gøre følgende: pip install -U python-dotenv og pip install -U discord.py
