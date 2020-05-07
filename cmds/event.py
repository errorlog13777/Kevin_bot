import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding="utf8") as jfile:  # jfile 如同 input file stream(ifstream)
    jdata = json.load(jfile)  # json.load() 讀取 file stream 內容並將其設給 jdata
    
class Event(Cog_Extension):
    @commands.Cog.listener()  # 這裡是 commands.command 的原因其雖然繼承了 commands.Cog, 但是所使用到的"功能不同", 這裡用到的是監聽, commands.command 用到的是指令
    async def on_member_join(self, member):   # 這裡的參數不用加 self 是因為其不在 class 內
        print(f'{member} join!')    # python 3.6 above, fstring, {} 放變數
        channel = self.bot.get_channel(jdata['Welcome_channel'])
        await channel.send(f'{member.mention} 大家都是我兄弟！') # 由於此功能以協程寫成, 所以使用時需要先加上 await

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave!')
        channel = self.bot.get_channel(jdata['Leave_channel'])
        await channel.send(f'{member.mention} 我把你當兄弟，偶爾開我玩笑，大家嘻嘻哈哈帶個氣氛我不會生氣 但我還是有個界線的，每個人都有。')

    @commands.Cog.listener()
    async def on_message(self, msg):  # 關鍵字觸發事件 (使用者每次輸入都會觸發這個事件)
        keyword = ['apple', 'pen', 'pie', 'abc']
        if msg.content in keyword and msg.author != self.bot.user:  # self.bot.user = 機器人本身
            await msg.channel.send('apple')  # 在 msg 所在頻道發送

        keyword2 = ["Kevin", "kevin", "裝熟", "社交大師", "重考", "綠帽", "綠扁帽大將軍", "阿兵哥", "1-1", "猴子屁股臉", "綠頭", "張凱文"]
        if msg.content in keyword2 and msg.author != self.bot.user:  # self.bot.user = 機器人本身
            await msg.channel.send('？')

        keyword3 = ["數C", "統測"]
        if msg.content in keyword3 and msg.author != self.bot.user:
            await msg.channel.send('統測可不可以快點來\n已經沒什麼好讀的\n第一科考數理特別愉快\n')
            await msg.channel.send("~~第一科考數理特別愉快~~\n我錯了當我沒說\n考完完全沒有如釋重負的感覺...")

        keyword4 = ["微積分"]
        if msg.content in keyword4 and msg.author != self.bot.user:
            await msg.channel.send("用大學微積分的公式\n\n  來解高中職微積分\n\n               愉悅")

        if msg.content == "張育誠":
            await msg.channel.send("好熟悉的名字...")


def setup(bot):
    bot.add_cog(Event(bot))