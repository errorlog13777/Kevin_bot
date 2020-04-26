import discord
from discord.ext import commands  # 從 discord.ext 導入 commands 模組

bot = commands.Bot(command_prefix='!!')  # 將 Bot 實體存放到 bot 中, 也就是說 bot 會代表這隻機器人
                                         # 裡面通常會存放一個 command_prefix 作為 argument, 代表呼叫機器人前需要 + 的 prefix(前綴)

@bot.event  # "@" 表示函數修飾符(decorator), 代表在其下面的函數會作為參數傳遞至 bot.event 中(python 中函數可以直接傳遞), 等價於 bot.event(on_ready)
async def on_ready():
    print(">> Bot is online <<")

bot.run("")   # arg 為 discord bot token