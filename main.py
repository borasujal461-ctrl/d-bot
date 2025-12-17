import discord
import random
import asyncio
import os
from discord.ext import commands

# 1. SETUP INTENTS 
# Make sure "Message Content Intent" is ON in the Discord Developer Portal
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

JOKES = [
    "That's what she said... and honestly, it was disappointing.",
    "I’ve seen better timing in a car crash.",
    "Is this conversation sponsored by Ambien? Because I’m falling asleep.",
    "I’d agree with you, but then we’d both be wrong and probably arrested.",
    "You talk a lot for someone within roasting distance."
]

TRIGGER_WORDS = ["work", "life", "dating", "hard", "problem"]

@bot.event
async def on_ready():
    # This will show up in your Railway Logs when it finally works
    print(f'Logged in as {bot.user.name} - Ready to ruin the mood.')

@bot.event
async def on_message(message):
    # Don't let the bot reply to itself
    if message.author == bot.user:
        return

    # 10% chance to reply to trigger words to keep it random
    if any(word in message.content.lower() for word in TRIGGER_WORDS):
        if random.random() < 0.10: 
            async with message.channel.typing():
                await asyncio.sleep(2)
                await message.reply(random.choice(JOKES))

    await bot.process_commands(message)

# 2. THE SECRET FIX
# This line looks for the 'DISCORD_TOKEN' you added in Railway's Variables tab
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
