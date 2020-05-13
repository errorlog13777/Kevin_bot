import discord
import random
import json
from discord.ext import commands
from selenium import webdriver
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding="utf8") as jfile:  # jfile 如同 input file stream(ifstream)
    jdata = json.load(jfile)    # json.load() 讀取 file stream 內容並將其設給 jdata

class React(Cog_Extension):
    @commands.command() # 從 bot.command 改成 commands.command 是因為我們繼承了 commands.Cog (classes.py)
    async def 專題(self, ctx):
        await ctx.send(ctx.message.author.mention + ' 我欠你很多人情')
    
    @commands.command()
    async def 重考(self, ctx):
        await ctx.send(ctx.message.author.mention + '\n重考從來就不是什麼童話故事\n從來就不會有什麼⋯\n無悔的努力 甜蜜的成功\n一切就只是一場賭注罷了\n而且這一次 我又輸慘了\n果然最後還是打臉了自己\n.\n早就已經忘記自己在追求什麼了\n我現在只想要⋯\n有一刻身心是自由的\n哪怕只有一瞬間\n能夠讓我暫時卸下肩膀上的疼痛\n能夠讓我暫時停住胸口上的悶痛\n能夠讓我不用\n為了什麼該死的人生成就\n不斷的被夢想追殺\n能夠讓我不用\n為了保護那微小的希望\n免於被現實扼殺\n早就忘記了什麼是玩樂\n犧牲了太多 快樂早已負債\n抱歉我那麼消極\n但我真的好累⋯⋯\nAccept reality\nChange reality\nKilled by reality')
    
    @commands.command()
    async def 大學(self, ctx):
        await ctx.send(ctx.message.author.mention + '\n好想快樂的上大學\n到底該飄向何方')

    """
    # 不便使用
    @commands.command()
    async def pic1(self, ctx):  # 讀取本機圖片
        pic = discord.File(jdata['pic'][0])  # 用 discord.File() 將其轉換成 discord 可讀取的"檔案"
        await ctx.send(ctx.message.author.mention)
        await ctx.send(file=pic) # file=pic 讓 discord 知道這是一個檔案
    """
    """
    # 理由同上
    @commands.command()
    async def ran_pic(self, ctx):     # 隨機本機圖片
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(ctx.message.author.mention)
        await ctx.send(file = pic)
    """

    @commands.command()
    async def ran_web_pic(self, ctx): # 隨機網路圖片
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)  # 因為網址不是檔案，所以不需要先轉換成 discord 能讀取的格式

    @commands.command()
    async def test_com(self, ctx):
        await ctx.send("Here’s an example of ~~crossed out~~ text")
def setup(bot):             # 機器人執行時會自動呼叫 setup, bot 為 bot.py 內的實體 bot
    bot.add_cog(React(bot))  # bot.add_cog() 呼叫 main.py 的 Main 並傳入參數 bot