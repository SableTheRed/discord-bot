import discord
from discord.ext import commands
from settings import token

client = commands.Bot()

@client.event
async def on_ready():
    print(f"Logged into discord api as: {client.user}") # logged into discord api as: user#0001

@client.slash_command()
async def ping(ctx):
    await ctx.respond("Pong")





client.run(token)
