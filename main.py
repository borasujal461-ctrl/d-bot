import discord
import random
import asyncio
import os
from discord.ext import commands

# 1. Setup Intents (The "Ears")
intents = discord.Intents.default()
intents.message_content = True  # Crucial: Must be ON in Dev Portal too
bot = commands.Bot(command_prefix="!", intents=intents)

# 2. The Jokes
JOKES = [
    "That's what she said... and honestly, it was disappointing.",
    "I’ve seen better timing in a car crash.",
    "Is this conversation sponsored by Ambien? Because I’m falling asleep.",
    "I’d agree with you, but then we’d both be wrong.",
    "You talk a lot for someone within roasting distance."
]

# 3. The Trigger Words
TRIGGER_WORDS = ["work", "life", "dating", "hard", "problem", "bot"]

@bot.event
async def on_ready():
    print(f'✅ SUCCESS: Logged in as {bot.user.name}')
    print("Settings: 100% reply rate is ACTIVE.")

# 4. The "Ping" Command (Type !test in Discord)
@bot.command()
async def test(ctx):
    await ctx.send("I'm awake! Stop shouting.")

# 5. The Main Logic
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if a trigger word is in the message
    msg_content = message.content.lower()
    if any(word in msg_content for word in TRIGGER_WORDS):
        print(f"🎯 Trigger detected in message: {message.content}")
        
        async with message.channel.typing():
            await asyncio.sleep(1) # Fake typing for 1 second
            await message.reply(random.choice(JOKES))

    # Allow commands (!test) to work
    await bot.process_commands(message)

# 6. Start the Bot
# Ensure you have 'DISCORD_TOKEN' in Railway Variables
# Or replace os.getenv('DISCORD_TOKEN') with "YOUR_ACTUAL_TOKEN" in quotes
token = os.getenv('DISCORD_TOKEN')
if token is None:
    print("❌ ERROR: No Token found! Add DISCORD_TOKEN to Railway Variables.")
else:
    bot.run(token)
