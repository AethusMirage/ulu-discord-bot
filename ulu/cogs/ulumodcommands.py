import discord
from discord.ext import commands

class ulumodcommands(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self,ctx,channelid:int,*,msg):
        channel=self.client.get_channel(channelid)
        await channel.send(msg)
        await ctx.message.delete()

    
    @commands.command(aliases=["delete","purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=1):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} messages successfully cleared!', delete_after=3)        

def setup(client):
        client.add_cog(ulumodcommands(client))        