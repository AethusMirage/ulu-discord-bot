import discord
import random
from asyncio import sleep
from discord.ext import commands
from uludatabase import uludatabase

class ulucommands(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.database= uludatabase()
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')

    @commands.command(aliases=["setreminder","remindme"])
    async def remind(self, ctx,hrs:int,mins:int,secs:int,*,msg="be happy :)"):
        if ((hrs>=0 and mins>=0) and secs>=0) and (mins<60 and secs<60):
                    
                if hrs==0 and mins==0 :
                    await ctx.send(f'I will remind you to {msg} after {secs} second(s), {ctx.author.mention}!')

                elif hrs==0 and secs==0 :
                    await ctx.send(f'I will remind you to {msg} after {mins} minute(s), {ctx.author.mention}!')       

                elif mins==0 and secs==0 :
                    await ctx.send(f'I will remind you to {msg} after {hrs} hour(s), {ctx.author.mention}!')        

                elif hrs==0 :
                    await ctx.send(f'I will remind you to {msg} after {mins} minute(s) {secs} second(s), {ctx.author.mention}!') 

                elif mins==0 :
                    await ctx.send(f'I will remind you to {msg} after {hrs} hours(s) {secs} second(s), {ctx.author.mention}!')

                elif secs==0:
                    await ctx.send(f'I will remind you to {msg} after {hrs} hours(s) {mins} minute(s), {ctx.author.mention}!')

                time=(hrs*3600)+(mins*60)+secs
                await sleep(time)
                await ctx.send(f'Hey {ctx.author.mention}, remember to {msg}')

        elif (hrs<0 or mins<0) or secs<0 :
                await ctx.send("Input value cannot be negative!")

        else :      
            await ctx.send("The value for minutes and seconds must be less than 60!")

    @commands.command(aliases=["cf","coin"])
    async def coinflip(self,ctx,guess:str):
        if guess=="h" or guess=="t":
                coin=["h","t"]
                await ctx.send("Flipping a coin...", delete_after=3)
                await sleep(3)
                result=random.choice(coin)
                if guess==result and result=="h":
                    await ctx.send("Yay! It's heads! :partying_face:")

                elif guess==result and result=="t":
                    await ctx.send("Yay! It's tails! :partying_face:")

                elif guess!=result and result=="h":
                    await ctx.send("Sorry, it's heads ;-;")

                else:
                    await ctx.send("Sorry, it's tails ;-;")            

        else:
                await ctx.send("Guess must be either h (for heads) or t (for tails)!")
    
    @commands.command(aliases=["ff","fact"])
    async def funfact(self,ctx):
        msg=random.choice(self.database.funfact)
        await ctx.send("Searching for a fun fact for you ;)...", delete_after=3)
        await sleep(3)
        async with ctx.typing():
                await ctx.send(f'I found one for you! {ctx.author.mention}\nDid you know {msg}')
   

    @commands.command(aliases=["roll","randomnumber","number"])
    async def rollnumber(self,ctx,num1:int,num2:int):
        await ctx.send("Rolling your number...",delete_after=3)
        await sleep(3)
        result=random.randint(num1,num2)
        await ctx.send(f'Ta-da! You rolled a {result}! {ctx.author.mention}')

    
    @commands.command(aliases=["hi","hey","summon"])
    async def hello(self,ctx):
        msg=random.choice(self.database.helloresponse)
        async with ctx.typing():
            await ctx.send(f'{msg} {ctx.author.mention}')

    @commands.command()
    async def mystery(self,ctx):
        mysteryembed=discord.Embed(
            title = "Go ahead and click this to find out what this does :smirk:",
            url="https://youtu.be/dQw4w9WgXcQ",
            colour = discord.Colour.from_rgb(3, 186, 252)
        )

        await ctx.send(embed=mysteryembed)
        await sleep(10)
        await ctx.send(f'Did you like that? :face_with_hand_over_mouth:{ctx.author.mention}')

    

def setup(client):
        client.add_cog(ulucommands(client))