import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

#configurations
bot_token=os.getenv("ULU_BOT_TOKEN")
prefix='&'
client = commands.Bot(command_prefix=prefix)
client.remove_command("help")
current_status=discord.Status.online
current_activity=discord.Activity(type=discord.ActivityType.listening,name=" your commands :)")

@client.event
async def on_ready():
      print("Run successful. Bot is now online.")
      await client.change_presence(status=current_status,activity=current_activity)        

for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename[:-3]} loaded successfully.')

client.run(bot_token)  