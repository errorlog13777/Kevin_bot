import discord
import json, asyncio
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
        
        keyword2 = ["Kevin", "kevin", "裝熟", "社交大師", "重考", "綠帽", "綠扁帽大將軍", "阿兵哥", "1-1", "猴子屁股臉", "綠頭", "張凱文", "restart"]
        # if msg.content in keyword2 and msg.author != self.bot.user:  # 這樣寫法錯誤的地方在於邏輯錯誤，如果 msg.content 在 keryword2 中，這就代表 msg.content 必須完全符合 keyword2 的任一單詞，而非 keyword2 的任一單詞符合 msg.content 的內容
        # if keyword2 in msg.content and msg.author != self.bot.user:  # 這樣寫法錯誤的地方在於 keyword2 是一個 list 而非一個 string, 因為類型不匹配，自然無法比較
        if msg.author != self.bot.user:
            for key in keyword2:  # key 為一個 string 對象
                if key in msg.content:  # 如果 key 的內容在 msg.content 中
                    await msg.channel.send('？')
                    break                  # 避免重複發話
        
        keyword3 = ["數C", "統測"]
        if msg.author != self.bot.user:
            for key in keyword3:
                if key in msg.content:
                    await msg.channel.send('統測可不可以快點來\n已經沒什麼好讀的\n考數理特別快樂\n')
                    await asyncio.sleep(10)  # 單位(s)
                    await msg.channel.send("~~考數理特別快樂~~\n當我沒說\n台科掰掰\n我就賭大家都不會\n完全沒有\n如釋重負的感覺")
                    break                   # 避免重複發話

        keyword4 = ["微積分"]
        # if msg.content in keyword4 and msg.author != self.bot.user:
        if msg.author != self.bot.user:
            for key in keyword4:
                if key in msg.content:
                    await msg.channel.send("用大學微積分的公式\n\n  來解高中職微積分\n\n               愉悅")

        if msg.content == "張育誠":
            await msg.channel.send("好熟悉的名字...?")

def setup(bot):
    bot.add_cog(Event(bot))