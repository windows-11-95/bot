import discord
from discord.ext import commands
from discord.ui import Button, View 
import logging 
import os 
from dotenv import load_dotenv 
import urllib.request

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Test network connection
req = urllib.request.Request(
    "https://discord.com/",
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    urllib.request.urlopen(req, timeout=5)
    print("🌐 Network connection SUCCESSFUL")
except Exception as e:
    print(f"❌ Network BLOCKED: {e}") 
    exit(1)

try:
    response = urllib.request.urlopen("https://discord.com", timeout=5)
    print("✅ Python can reach Discord!", response.status)
except Exception as e:
    print("❌ Python blocked:", e)
  

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event 
async def on_ready():
    print(f'✅ {bot.user} connected successfully!')

@bot.command(name='setup_verification')
async def verification_panel(ctx):
    embed = discord.Embed(
        title='Minecraft Account Linking',
        description="Click below to verify",
    )
    
    button = Button(
        label='✅ Link Account',
        style=discord.ButtonStyle.url,
        url='https://example.com/verification'  # ADD YOUR ACTUAL URL HERE
    )
    
    view = View()
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

# Run the bot
if __name__ == '__main__':
    if TOKEN:
        bot.run(TOKEN)
    else:
        logging.error("❌ Missing Discord token! Add it to .env file")

        print(f"TOKEN: {token}")
