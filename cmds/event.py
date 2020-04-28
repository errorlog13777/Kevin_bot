import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding="utf8") as jfile:  # jfile 如同 input file stream(ifstream)
    jdata = json.load(jfile)  # json.load() 讀取 file stream 內容並將其設給 jdata
    
class Event(Cog_Extension):
    @commands.Cog.listener()  # 這裡不用變成 commands.command 的原因就是因為其沒有繼承 commands.Cog
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
        keyword2 = ["Kevin", "裝熟", "社交大師", "重考", "綠帽", "綠扁帽大將軍", "阿兵哥", "1-1", "猴子屁股臉"]
        for key in keyword2:
            if key in msg.content:
                await msg.channel.send('有人提到我嗎？')


def setup(bot):
    bot.add_cog(Event(bot))