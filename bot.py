import discord
from discord.ext import commands  # 從 discord.ext 導入 commands 模組
import json  # 導入 json mod (設定檔使用 .json file)
import random
import os

with open('setting.json', 'r', encoding="utf8") as jfile:  # jfile 如同 input file stream(ifstream)
    jdata = json.load(jfile)    # json.load() 讀取 file stream 內容並將其設給 jdata

bot = commands.Bot(command_prefix='!!')  # 將 Bot 實體存放到 bot 中, 也就是說 bot 會代表這隻機器人
                                         # 裡面通常會存放一個 command_prefix 作為 argument, 代表呼叫機器人前需要 + 的 prefix(前綴)

@bot.event  # "@" 表示函數修飾符(decorator), 代表在其下面的函數(on_ready)會作為參數傳遞至 bot.event 中(python 中函數可以直接傳遞), 等價於 on_ready = bot.event(on_ready), 所以 on_ready() 會被修改, 此時 on_ready 不能算是一個 function, 而是 bot_event(on_ready) 的 return val
async def on_ready():               # https://blog.techbridge.cc/2018/06/15/python-decorator-%E5%85%A5%E9%96%80%E6%95%99%E5%AD%B8/
    print(">> Bot is online <<")    # https://www.hansshih.com/post/85896158975/%E8%90%AC%E6%83%A1%E7%9A%84-python-decorator-%E7%A9%B6%E7%AB%9F%E6%98%AF%E4%BB%80%E9%BA%BC

@bot.event  # 這裡不用變成 commands.command 的原因就是因為其沒有繼承 commands.Cog
async def on_member_join(member):   # 這裡的參數不用加 self 是因為其不在 class 內
    print(f'{member} join!')    # python 3.6 above, fstring, {} 放變數
    channel = bot.get_channel(jdata['Welcome_channel'])
    await channel.send(f'{member.mention} 大家都是我兄弟！') # 由於此功能以協程寫成, 所以使用時需要先加上 await

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(jdata['Leave_channel'])
    await channel.send(f'{member.mention} 我把你當兄弟，偶爾開我玩笑，大家嘻嘻哈哈帶個氣氛我不會生氣 但我還是有個界線的，每個人都有。')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):  # 檔案名稱結尾為 .py
        bot.load_extension(f'cmds.{filename[:-3]}')  # ori: main.py, [:-3]: main
# http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html
# 若檔案是直接執行(透過命令列)，__name__ 的值會是 __main__; 如果是被作為 module import 的 python script __name__ 的值會是 python script 檔案名稱
# 用 __name__ 可以分辨程式是被當成 module import 的還是被直接執行的
# 直接執行會跑完腳本所有內容，當成模組只會用到被呼叫的部分(內容)       
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])  # arg 為 discord bot token
