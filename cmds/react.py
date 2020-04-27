import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding="utf8") as jfile:  # jfile 如同 input file stream(ifstream)
    jdata = json.load(jfile)    # json.load() 讀取 file stream 內容並將其設給 jdata

class React(Cog_Extension):
    @commands.command()
    async def 專題(self, ctx):
        await ctx.send(ctx.message.author.mention + ' 我欠你很多人情')

    @commands.command()
    async def pic1(self, ctx):  # 讀取本機圖片
        pic = discord.File(jdata['pic'][0])  # 用 discord.File() 將其轉換成 discord 可讀取的"檔案"
        await ctx.send(ctx.message.author.mention)
        await ctx.send(file=pic) # file=pic 讓 discord 知道這是一個檔案

    @commands.command()
    async def ran_pic(self, ctx):     # 隨機本機圖片
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(ctx.message.author.mention)
        await ctx.send(file = pic)

    @commands.command()
    async def ran_web_pic(self, ctx): # 隨機網路圖片
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)  # 因為網址不是檔案，所以不需要先轉換成 discord 能讀取的格式

def setup(bot):             # 機器人執行時會自動呼叫 setup, bot 為 bot.py 內的實體 bot
    bot.add_cog(React(bot))  # bot.add_cog() 呼叫 main.py 的 Main 並傳入參數 bot