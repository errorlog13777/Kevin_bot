import discord
import json, asyncio, datetime
from discord.ext import commands
from core.classes import Cog_Extension

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # super 表示父類別, 這邊因為 __init__ 與 classes.py 的重複定義，所以會導致 classes.py 的定義被取代，所以需要透過 super() 的方式將 classes.py 的屬性(功能)導入
        
        self.counter = 0
        # ctrl + k + c, ctrl + k + u
        # async def interval():       # 不是 discord 內部功能，所以無需加入裝飾器
        #     await self.bot.wait_until_ready()  # 等到機器人準備就緒才開始執行指令
        #     self.channel = self.bot.get_channel(706451165386244147)
        #     while not self.bot.is_closed():  # 當機器人沒有被關閉時(若 bot 一直在線上)
        #         await self.channel.send("Hi! 我是 Kevin Zhang! 請輸入 \"!!help\" 來更了解我 :)\n\n")
        #         await asyncio.sleep(500)  # 單位(s)
        
        # self.bot.loop.create_task(interval())  # 創建一個背景作業的 task, 用 bot 方法 loop 創建一個 task 也就是我們設定的 interval
        
        async def time_task():       # 不是 discord 內部功能，所以無需加入裝飾器
            await self.bot.wait_until_ready()  # 等到機器人準備就緒才開始執行指令
            self.channel = self.bot.get_channel(706451165386244147)
            while not self.bot.is_closed():  # 當機器人沒有被關閉時(若 bot 一直在線上)
                now_time = datetime.datetime.now().strftime('%H%M')  # H = hour, M = min, m = month
                # now_time = now_time - datetime.timedelta(hours = 8)
                await self.channel.send(now_time)
                with open('setting.json', 'r', encoding='utf8') as jfile:   # r = read
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    self.counter = 1
                    await self.channel.send('OWOW time\'s up! ')
                    # await asyncio.sleep(3)  # 不加間格時間有可能導致 discord bot 來不及準備好 (on_ready()), 因為執行條件是只要機器人不為關閉(while not self.bot)
                else:
                    await asyncio.sleep(3)  # 不加間格時間有可能導致 discord bot 來不及準備好 (on_ready())
                    # break # 跳出去之後需要重新使其開始執行
        self.bg_task = self.bot.loop.create_task(time_task())
        
        # self.bot.loop.create_task(interval())  # 創建一個背景作業的 task, 用 bot 方法 loop 創建一個 task 也就是我們設定的 interval

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)  # 由於在 class 內是以物件導向，所以 self.channel 是一個物件, 不會像區域變數一樣離開 field 後就結束
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json', 'r', encoding='utf8') as jfile:   # r = read
            jdata = json.load(jfile)
            jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:   # w = write
            json.dump(jdata, jfile, indent=4)   # indent = 縮排

def setup(bot):
    bot.add_cog(Task(bot))
