import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is connected")


client.run("MTA2NzU4MTA3Mjk3MzUxNjg1MQ.GyIoUO.QP1hiXf0wBlwmFPeQ3yN15Y-BLOImYeH0TP5js")







        






