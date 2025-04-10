import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from bot.ocr import process_image  # Use real OCR logic

# Load environment
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
WATCH_CHANNEL_ID = os.getenv("WATCH_CHANNEL_ID")
if WATCH_CHANNEL_ID:
    WATCH_CHANNEL_ID = int(WATCH_CHANNEL_ID)
else:
    WATCH_CHANNEL_ID = 0

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id == WATCH_CHANNEL_ID and message.attachments:
        await process_image(bot, message)
    await bot.process_commands(message)

bot.run(TOKEN)
