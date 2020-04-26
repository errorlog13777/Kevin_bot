import discord
from discord.ext import commands  # 從 discord.ext 導入 commands 模組

bot = commands.Bot(command_prefix='!!')  # 將 Bot 實體存放到 bot 中, 也就是說 bot 會代表這隻機器人
                                         # 裡面通常會存放一個 command_prefix 作為 argument, 代表呼叫機器人前需要 + 的 prefix(前綴)

@bot.event  # "@" 表示函數修飾符(decorator), 代表在其下面的函數會作為參數傳遞至 bot.event 中(python 中函數可以直接傳遞), 等價於 on_ready = bot.event(on_ready), 所以 on_ready() 會被修改
async def on_ready():               # https://blog.techbridge.cc/2018/06/15/python-decorator-%E5%85%A5%E9%96%80%E6%95%99%E5%AD%B8/
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(703898937806946324)
    await channel.send(f'{member.mention} 大家都是我兄弟！') # 由於此功能以協程寫成, 所以使用時需要先加上 await

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(703898997726773268)
    await channel.send(f'{member.mention} 我把你當兄弟，偶爾開我玩笑，大家嘻嘻哈哈帶個氣氛我不會生氣 但我還是有個界線的，每個人都有。')

# ctx = context(上下文)
# A:嗨 (上文), 上文包含右側屬性：(使用者, user-id, 所在伺服器, 所在頻道), ctx 則包含了這些屬性, 所以無須像 on_member_join 一樣需要再獲取 channel-id
# B:安安 (下文)
@bot.command()
async def ping(ctx):  # 當使用者打下 `ping` 就會自動傳入 ctx 參數，其包含使用者的相關屬性
    #member = discord.Member
    #channel = bot.get_channel(703896647293206582)
    #await channel.send(f'{ctx.message.author}')
    await ctx.send(ctx.message.author.mention + f'{round(bot.latency * 1000)} (ms)')  # latency = 延遲(秒), round() 將小數點後四捨五入

@bot.command()
async def 專題(ctx):
    await ctx.send(ctx.message.author.mention + '我欠你很多人情')    
bot.run("NzAzMjI0OTM3NzQ5NDEzODg4.XqVLAw.Eh5JcfZnn54iooMvUqFMIe8bIMQ")  # arg 為 discord bot token
