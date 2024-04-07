import discord
import os
import asyncio
import json
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def update_status():
    while True:
        try:
            # Starting with a static message to ensure functionality
            status_message = "BTC: $10000"
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_message))
            print(f"Status updated to: {status_message}")
            await asyncio.sleep(300)  # Wait for 5 minutes before updating again
        except Exception as e:
            print(f"An error occurred: {e}")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(update_status())

client.run(os.getenv('BTC_TOKEN'))
