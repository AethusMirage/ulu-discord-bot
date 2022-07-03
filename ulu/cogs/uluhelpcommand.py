import discord
from discord.ext import commands

class uluhelpcommand(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases=["ulu"])
    async def info(self,ctx) :
        infoembed=discord.Embed(
                title = "Bot Info",
                description = "I'm a variety purpose bot created by Aethus. I'm currently under test run phase and I will soon be made available on being your personal trustworthy companion! :)",
                colour = discord.Colour.from_rgb(3, 186, 252)
        )
        infoembed.set_footer(text="Created by Aethus.")

        infoembed.add_field(name="Coding Language",value="Python",inline=False)
        infoembed.add_field(name="Creator",value="Aethus",inline=False)
        infoembed.add_field(name="Github Link",value="insert link here",inline=False)
        infoembed.add_field(name="Tip",value="Type '&help' to get list of available commands!",inline=False)

        await ctx.send(embed=infoembed)

    @commands.command()
    async def feedback(self,ctx):
        feedbackembed=discord.Embed(
            title = "Feedback",
            description = "How was your experience using Ulu? Did you like it? Were there any errors that annoyed you? Think you have a brilliant idea on how to make Ulu better than its creator? Feel free to write out your thoughts via Google Form by clicking the text highlighted in blue above.",
            #url = "Insert link here",
            colour = discord.Colour.from_rgb(3, 186, 252)
        )

        await ctx.send(embed=feedbackembed)    

    @commands.command()
    async def help(self,ctx,commandchoice="help"):     
        helpembed=discord.Embed(
                title = "Help",
                description = "Here below are the list of available commands.\nType &help [command name] to know more details about a specific command such as its function and ways to execute it!",
                colour = discord.Colour.from_rgb(3, 186, 252)
        )
        helpembed.add_field(name="Prefix",value="&\n",inline=False)
        helpembed.add_field(name="General Commands",value="info, feedback, ping, remind, coinflip, funfact, rollnumber, hello",inline=False)
        helpembed.add_field(name="Moderation Commands",value="say, clear",inline=False)
        helpembed.add_field(name="Music Commands",value="Coming Soon!",inline=False)
        helpembed.add_field(name="Mystery Commands",value="mystery",inline=False)

        infohelpembed=discord.Embed(
            title= "Info",
            description = "Display the bot info and link to its source code on Github.",
            colour = discord.Colour.from_rgb(3, 186, 252)

        )
        infohelpembed.add_field(name="Aliases",value="ulu",inline=False)
        infohelpembed.add_field(name="How to use",value="&info",inline=False)
        infohelpembed.add_field(name="Special permission required?",value="No",inline=False)

        feedbackhelpembed=discord.Embed(
            title= "Feedback",
            description = "Obtain URL to send feedbacks regarding Ulu's performance.",
            colour = discord.Colour.from_rgb(3, 186, 252)

        )
        feedbackhelpembed.add_field(name="How to use",value="&feedback",inline=False)
        feedbackhelpembed.add_field(name="Special permission required?",value="No",inline=False)

        pinghelpembed=discord.Embed(
            title= "Ping",
            description = "Display the latency rate between the client and the bot server.",
            colour = discord.Colour.from_rgb(3, 186, 252)

        )
        pinghelpembed.add_field(name="How to use",value="&ping",inline=False)
        pinghelpembed.add_field(name="Special permission required?",value="No",inline=False)

        remindhelpembed=discord.Embed(
            title= "Remind",
            description = "Setup a reminder that will alert the user after a specified amount of time.",
            colour = discord.Colour.from_rgb(3, 186, 252)

        )
        remindhelpembed.add_field(name="Aliases",value="setreminder, remindme",inline=False)
        remindhelpembed.add_field(name="How to use",value="&remind (hours) (minutes) (seconds) (reminder context [Optional])",inline=False)
        remindhelpembed.add_field(name="Special permission required?",value="No",inline=False)

        coinfliphelpembed=discord.Embed(
            title= "Coinflip",
            description = "Take a guess at the result of flipping a coin and reveal the result.",
            colour = discord.Colour.from_rgb(3, 186, 252)

        )
        coinfliphelpembed.add_field(name="Aliases",value="cf, coin",inline=False)
        coinfliphelpembed.add_field(name="How to use",value="&coinflip (h/t)",inline=False)
        coinfliphelpembed.add_field(name="Special permission required?",value="No",inline=False)

        

        commandlist = {"help":helpembed, "info":infohelpembed, "feedback":feedbackhelpembed, "ping":pinghelpembed, "remind":remindhelpembed, "coinflip":coinfliphelpembed, }

        await ctx.send(embed=commandlist[commandchoice]) 

def setup(client):
    client.add_cog(uluhelpcommand(client))