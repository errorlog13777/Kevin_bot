import discord
import json
import datetime
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding="utf8") as jfile:  # jfile 如同 input file stream(ifstream)
    jdata = json.load(jfile)    # json.load() 讀取 file stream 內容並將其設給 jdata

class Main(Cog_Extension):  # Main 繼承 commands.Cog 裡面的所有屬性、功能
    
    # ctx = context(上下文)
    # A:嗨 (上文), 上文包含右側屬性：(使用者, user-id, 所在伺服器, 所在頻道), ctx 則包含了這些屬性, 所以無須像 on_member_join 一樣需要再獲取 channel-id
    # B:安安 (下文)
    @commands.command() # 從 bot.command 改成 commands.command 是因為我們繼承了 commands.Cog (classes.py)
    async def ping(self, ctx):  # 當使用者打下 `ping` 就會自動傳入 ctx 參數，其包含使用者的相關屬性
        #member = discord.Member
        #channel = bot.get_channel(703896647293206582)
        #await channel.send(f'{ctx.message.author}')
        await ctx.send(ctx.message.author.mention + f'{round(self.bot.latency * 1000)} (ms)')  # latency = 延遲(秒), round() 將小數點後四捨五入

    @commands.command()
    async def hi(self, ctx):
        await ctx.send(ctx.message.author.mention + f' 哈囉，你好這裡是台灣，我是台灣人 Kevin 張凱文，下面這個人是我的女朋友陳鮭魚')
        await ctx.send(jdata['salmon'])

    @commands.command()
    async def em(self, ctx):    # embed 生成器 https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(title="Kevin Bot", url="https://www.instagram.com/ke_.y.c/", description="Just a Kevin Bot", color=0x00ff40, timestamp=datetime.datetime.now() - datetime.timedelta(hours = 8))
        embed.set_author(name="Kevin fans", url="https://www.instagram.com/ke_.y.c/")
        embed.set_thumbnail(url="https://scontent-frt3-2.cdninstagram.com/v/t51.2885-19/91286268_679708962764318_6840888535994597376_n.jpg?_nc_ht=scontent-frt3-2.cdninstagram.com&_nc_ohc=fIe4jC20CCEAX_2IZG1&oh=86441324bde90181657aadbd83680dc2&oe=5ED2922F")
        embed.add_field(name="website", value="https://www.instagram.com/ke_.y.c/", inline=False)
        embed.set_footer(text="高科電神張凱文")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *, msg):  # 刪除使用者訊息，由機器人複誦 (* 代表在此之後的參數不論有多少都會作為 msg 的 argument, msg 為使用者訊息參數)
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def purge(self, ctx, num: int):  # num : int 的意思代表先註解 argument 的資料型態
        await ctx.channel.purge(limit = num + 1)    # +1 的作用為多刪除打指令的訊息

def setup(bot):             # 機器人執行時會自動呼叫 setup, bot 為 bot.py 內的實體 bot
    bot.add_cog(Main(bot))  # bot.add_cog() 呼叫 main.py 的 Main 並傳入參數 bot