import discord
from discord.ext import commands
import datetime
import os
from dotenv import load_dotenv

# Load environment variables (Safety first: keeps secrets out of GitHub)
load_dotenv()

# --- CONFIGURATION ---
# Retrieve Token from system or .env file
TOKEN = os.getenv('DISCORD_TOKEN') 
# Ensure this ID is set in your .env file
LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID'))

# List of prohibited words (Blacklist)
BANNED_WORDS = ["scam", "virus", "idiot", "badword", "fraud"] 

# Permissions (Intents) required to read messages and manage members
intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'🛡️  Security System Online as {bot.user}')

# --- AUTO-MODERATION SYSTEM ---
@bot.event
async def on_message(message):
    # Prevent the bot from triggering itself
    if message.author == bot.user:
        return

    content = message.content.lower()
    
    # Scan for banned words
    for word in BANNED_WORDS:
        if word in content:
            try:
                await message.delete() # Delete the toxic message
                await message.channel.send(f"{message.author.mention} That word is not allowed here! 🚫", delete_after=5)
                
                # Send evidence to the private Audit Log channel
                log_channel = bot.get_channel(LOG_CHANNEL_ID)
                if log_channel:
                    embed = discord.Embed(title="🚨 Moderation Alert", color=discord.Color.red())
                    embed.add_field(name="User", value=message.author.name, inline=True)
                    embed.add_field(name="Message Content", value=message.content, inline=True)
                    embed.set_footer(text=f"Time: {datetime.datetime.now()}")
                    await log_channel.send(embed=embed)
            except Exception as e:
                print(f"Error during moderation: {e}")
            return # Exit to prevent processing further commands

    # Important: Process commands only if no banned words were found
    await bot.process_commands(message)

# --- KICK COMMAND (Admin Only) ---
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'👢 User {member.name} has been kicked. Reason: {reason}')
    except Exception as e:
        await ctx.send(f"Could not kick user. Error: {e}")

# Error Handling: Missing Permissions
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("⛔ You do not have permission to use this command.")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("ERROR: DISCORD_TOKEN not found in environment variables.")