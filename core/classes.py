import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot):    # python class 內功能一定要放 self 參數(類似 cpp this), bot 則作為傳入用參數
        self.bot = bot  # self.bot = bot.py 內的 bot