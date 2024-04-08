import discord
import os
import asyncio
import json
import runpy
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

intents = discord.Intents.default()

# Initialize four separate bot clients
btc_bot = discord.Client(intents=intents)
eth_bot = discord.Client(intents=intents)
shiba_bot = discord.Client(intents=intents)
ltc_bot = discord.Client(intents=intents)

def run_json_reader():
    runpy.run_path('coingecko/api.py')

def json_read(file_name):
    run_json_reader()
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

def format_price(price):
    if 'e' in f"{price}":
        return f"{price:.10f}"
    else:
        return str(price)

async def update_status(bot, crypto_name, crypto_token, status_type):
    while True:
        try:
            data = json_read('coingecko/cryptocurrency_prices.json')
            raw_price = data[crypto_name]['usd']
            formatted_price = format_price(raw_price)
            status_message = f"${formatted_price}"
            await bot.change_presence(activity=discord.Activity(type=status_type, name=status_message))
            print(f"{crypto_name.upper()} status updated to: {status_message}")
            await asyncio.sleep(120)  # Update every 2 minutes
        except Exception as e:
            print(f"An error occurred for {crypto_name}: {e}")

@btc_bot.event
async def on_ready():
    print(f'{btc_bot.user} has connected to Discord!')
    btc_bot.loop.create_task(update_status(btc_bot, 'bitcoin', os.getenv('BTC_TOKEN'), discord.ActivityType.watching))

@eth_bot.event
async def on_ready():
    print(f'{eth_bot.user} has connected to Discord!')
    eth_bot.loop.create_task(update_status(eth_bot, 'ethereum', os.getenv('ETH_TOKEN'), discord.ActivityType.watching))

@shiba_bot.event
async def on_ready():
    print(f'{shiba_bot.user} has connected to Discord!')
    shiba_bot.loop.create_task(update_status(shiba_bot, 'shiba-inu', os.getenv('SHB_TOKEN'), discord.ActivityType.watching))

@ltc_bot.event
async def on_ready():
    print(f'{ltc_bot.user} has connected to Discord!')
    ltc_bot.loop.create_task(update_status(ltc_bot, 'litecoin', os.getenv('LTC_TOKEN'), discord.ActivityType.watching))

async def main():
    await asyncio.gather(
        btc_bot.start(os.getenv('BTC_TOKEN')),
        eth_bot.start(os.getenv('ETH_TOKEN')),
        shiba_bot.start(os.getenv('SHB_TOKEN')),
        ltc_bot.start(os.getenv('LTC_TOKEN')),
    )

if __name__ == '__main__':
    asyncio.run(main())
