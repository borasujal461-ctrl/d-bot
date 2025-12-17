import discord
import random
import asyncio
from discord.ext import commands

# Standard setup
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

# A list of "interjections" - keep these as edgy as your server allows
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
    print(f'Logged in as {bot.user.name} - Ready to ruin the mood.')

@bot.event
async def on_message(message):
    # Don't let the bot talk to itself
    if message.author == bot.user:
        return

    # Random chance (e.g., 10%) to interject if a trigger word is found
    if any(word in message.content.lower() for word in TRIGGER_WORDS):
        if random.random() < 0.10: 
            # Add a small delay so it feels like the bot is 'typing' a comeback
            async with message.channel.typing():
                await asyncio.sleep(2)
                await message.reply(random.choice(JOKES))

    await bot.process_commands(message)

bot.run('MTQ1MDY5NjY0MTAyNjk4NjE2Nw.GdbES4.bgwE5z4e4Xlx3KZiDZS6mrT2--1g-NgFuifYWw')
