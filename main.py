from os import system
from imp import reload
system('cls')
import discord 
import asyncio 
from source import add_message
from source import config
import pytz, datetime
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!!", intents=intents)

@client.event
async def on_ready():
    system('cls')
    print("Uiwang-si BOT | 의왕시 봇이 준비 되었습니다")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("의왕시 관리"))

@client.event
async def on_message(message):
    if message.author.bot:
        return None 
    if message.content.startswith("!!속강이 소고기 리로드"):
        if message.author.id == 0 or message.author.id == 0 or message.author.id == 0:
            reload(add_message)
            reload(config)
            await message.reply(embed=discord.Embed(title="Uiwang Admin Bot Moduel Reload System", description="✅ 모든 모듈을 모두 다시 시작했습니다"))
    elif message.content.startswith("##정리"):
        system('cls')
    else:
        await add_message.go_message(client, message)



    if message.content.startswith ("!공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            embed = discord.Embed(title="**Uiwang :: 공지 **", description="공지사항 내용은 항상 확인해주세요!\n```{}```\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="의왕시ㆍ담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            await message.channel.send ("@everyone", embed=embed)
 
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다 지속적으로 관리자 명령어를 사용할시 제제당하실수있습니다.".format(message.author.mention))



    if message.content == "!사전예약":
        await message.channel.send("{} 님 DM확인 부탁드립니다.".format(message.author.mention))
        await message.author.send("{} **님사전예약 완료되셨습니다! 사전예약은 한번만 가능하며, 지속적인 사전예약이 불가능합니다.**".format(message.author.mention))
        role = discord.utils.get(message.guild.roles, name = '💎ㆍ사전예약')
        await message.author.add_roles(role)



    if message.content.startswith ("!청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="의왕시", icon_url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))


####################### RP , Non-RP , Bad-RP 알려주는 기능 #################################
    
    if message.content == "!알피":
        await message.channel.send("{} **유저님 안녕하세요! 늅도봇입니당! RP의 대해서 물어보셨군요! 친절하게 알려드릴게요! 'RP'란 RolePlaying의 줄임말로써 현실에서 역할을 부여받고 살듯이 서버라는 공간에서 각자의 역할을 부여받으면서 살아가는것을 RP라고 말합니다! 즉, 현실에서 가능한것을 말하는거죠! 예시로는 밥먹기 , 택시기사하기 , 배달하기 등이 있답니다!**".format(message.author.mention))

    if message.content == "!배드알피":
        await message.channel.send("{} **유저님 안녕하세요! 늅도봇입니당! Bad-RP의 대해서 물어보셨군요! 친절하게 알려드릴게요! 'Bad-RP'란 현실에서 가능하나, 무언가 모순됬거나, 잘못된행동을 말합니다! 예시로는 죄없는 시민을 총으로 죽이던가 , 볼링 , 범퍼 등 있답니다!**".format(message.author.mention))

    if message.content == "!논알피":
        await message.channel.send("{} **유저님  안녕하세요! 늅도봇입니당! Non-RP의 대해서 물어보셨군요! 친절하게 알려드릴게요! 'Non-RP'란 현실에서 완.전.히 불가능한것을 말합니다! 예시로는 하늘을 날거나 , 무적이 된다거나 , 죽었을때 말한다거나 , 죽었을때 방탄복을 착용하는 것 등이 있습니당!**".format(message.author.mention))

    if message.content == "!파워게이밍":
        await message.channel.send("{} **유저님  안녕하세요! 늅도봇입니당! 파워게이밍의 대해서 물어보셨군요! 친절하게 알려드릴게요! '파워게이밍'이란 /me 명령어를이용해 현실성없는명령어를 입력하는 행위를 말합니다! 예시로는 /me 자동차를 한손으로 번쩍든다 , /me 초사이아인으로 변신해 에너지파를 발사한다 등이 있습니당!**".format(message.author.mention))

    if message.content == "!메타게이밍":
        await message.channel.send("{} **유저님  안녕하세요! 늅도봇입니당! 메타게이밍의 대해서 물어보셨군요! 친절하게 알려드릴게요! '메타게이밍'이란 IC 상에서 /b 명령어없이 ㅋㅋ,ㅎㅎ,ㅈㅅ,ㄱㅊ 이러한 초성을 하용하는 행위를 뜻합니다!**".format(message.author.mention))

################## 서버온 ###################
    if message.content == "!서버온":
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            embed = discord.Embed(title="서버 ON", color=0x3aff00)
            embed.add_field(name="> 의왕시가 ONLINE 되었습니다.\n", value="        ", inline=False) # 안내 문구
            embed.add_field(name="> 아래 주소로 접속이 가능합니다!", value="> 접속주소 : https://www.roblox.com/games/15469754878/Gyeonggi-do-Uiwang", inline=False) # 안내 문구
            embed.set_footer(text="Uiwang-siㆍ")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            await message.channel.send ("@everyone", embed=embed)
             
        if i is False:
            await message.channel.send("{}, **당신은 관리자가 아닙니다. 지속적으로 관리진명령어를 사용할시 제제받으실수 있습니다.**".format(message.author.mention))
    
    if message.content == "!서버리붓":
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            embed = discord.Embed(title="서버 REBOOT", color=0xff0000)
            embed.add_field(name="> 의왕시가 REBOOT 중입니다.", value="        ", inline=False) # 안내 문구
            embed.add_field(name="> ONLINE 공지가 올라 올때까지 기다려주세요!", value="        ", inline=False) # 안내 문구
            embed.set_footer(text="Uiwang-siㆍ")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            await message.channel.send ("@everyone", embed=embed)
             
        if i is False:
            await message.channel.send("{}, **당신은 관리자가 아닙니다. 지속적으로 관리진명령어를 사용할시 제제받으실수 있습니다.**".format(message.author.mention))
    
    if message.content == "!서버점검":
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            embed = discord.Embed(title="서버 CHECK", color=0xeaff00)
            embed.add_field(name="> 의왕시가 점검중입니다.", value="        ", inline=False) # 안내 문구
            embed.add_field(name="> 서버점검 완료 전까지는 접속을 금지합니다.", value="        ", inline=False) # 안내 문구
            embed.set_footer(text="Uiwang-siㆍ")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            await message.channel.send ("@everyone", embed=embed)
             
        if i is False:
            await message.channel.send("{}, **당신은 관리자가 아닙니다. 지속적으로 관리진명령어를 사용할시 제제받으실수 있습니다.**".format(message.author.mention))

    if message.content == "!서버오프":
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            embed = discord.Embed(title="서버 OFF", color=0xeaff00)
            embed.add_field(name="> 의왕시가 OFFLINE 되었습니다.", value="        ", inline=False) # 안내 문구
            embed.add_field(name="> ONLINE 공지가 올라 올때까지 기다려주세요!", value="        ", inline=False) # 안내 문구
            embed.set_footer(text="Uiwang-siㆍ")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1076414596723773480/1077914833162338335/-001_13.png")
            await message.channel.send ("@everyone", embed=embed)
             
        if i is False:
            await message.channel.send("{}, **당신은 관리자가 아닙니다. 지속적으로 관리진명령어를 사용할시 제제받으실수 있습니다.**".format(message.author.mention))

    ######################################################################################################################################################

@client.event
async def on_member_join(member):
           embed = discord.Embed(title="**의왕시 입장로그**",description=f"{member.mention} 님께서 의왕시에 입장하셨습니다.",color = 0x000000)
           await member.guild.get_channel(1177555243874136124).send(embed=embed)
           await member.send("**__의왕시에 오신것을 환영합니다!__**")
           await member.edit(nick="고유번호ㆍ{}ㆍ취업준비생".format(member.display_name))


client.run(config.config("token"))
