import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print(f"Logged into discord api as: {client.user}") # logged into discord api as: user#0001
