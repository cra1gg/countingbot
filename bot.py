# bot.py
import os
import random
import discord
import asyncio
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    messages = await message.channel.history(limit=5).flatten()
    for p in range(len(messages)):
        if messages[p].author == client.user:
            await messages[p].delete()
    messages = await message.channel.history(limit=5).flatten()
    try:
        first = int(messages[0].content)
        second = int(messages[1].content)
        if (int(messages[0].content) != (int(messages[1].content) + 1)):
            await messages[0].delete()
            sent = await message.channel.send("This channel is for counting only. You entered " + messages[0].content + ". The previous number was " + messages[1].content)
            await asyncio.sleep(3) 
            await sent.delete()
        if (messages[0].author == messages[1].author):
            await messages[0].delete()
            sent = await message.channel.send("Please only enter one number at a time")
            await asyncio.sleep(3) 
            await sent.delete()
    except:
        await messages[0].delete()
        sent = await message.channel.send("This channel is for counting only. You entered " + messages[0].content + ". The previous number was " + messages[1].content)
        await asyncio.sleep(3) 
        await sent.delete()

keep_alive()
client.run(TOKEN)