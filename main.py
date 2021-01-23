import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from os import listdir
from dotenv import load_dotenv
load_dotenv()


TOKEN = (os.getenv('DISCORD_TOKEN'))
PREFIX = "~"

intents = discord.Intents.default()
intents.members = True

bot = Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("guilds:")
    for guild in bot.guilds:
        print(f"\t{guild.name}")

    cogs = [f[:-3] for f in listdir() if "cog" == f[-6:-3]]

    print("Cogs:")
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"\t{cog}")
        except Exception as e:
            print(f"Failed to load cog: {cog[:-4]}")
            print(f"{type(e).__name__}: {e}") 

@bot.command()
async def load (ctx, cog):
    cog_mod = cog
    if cog_mod in bot.extensions:
        bot.unload_extension(cog_mod)
    bot.load_extension(cog_mod)
    print(ctx, f"{cog} loaded")

bot.run(TOKEN)