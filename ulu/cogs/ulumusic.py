import discord
from discord.ext import commands

class ulumusic(commands.Cog):

    def __init__(self,client):
        self.client = client

def setup(client):
    client.add_cog(ulumusic(client))    