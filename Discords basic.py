import os

import discord
from dotenv import load_dotenv


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("MzM1ODQ0MDI5Njc1NzMyOTkz.XhWNyQ.nJ7vkZ7DRezynNr7tlAV3R_vikM")



#Botten kræver at i downloader dotenv.py og discord.py
#i kan download det ved at gøre følgende: pip install -U python-dotenv og pip install -U discord.py
