import discord
from discord.ext import commands
from settings import token

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print(f"Logged into discord api as: {client.user}") # logged into discord api as: user#0001

@client.command()
async def ping(ctx): # ctx stands for context
    await ctx.send("Pong")





client.run(token)
