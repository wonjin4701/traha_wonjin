

import discord
 

token = "NzE3MzAxMjMxMjIzMzA4MzI5.XtYU2Q.qYKV5ncEpOHscTd3-U0ZqVD7Kus"
client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("테스트중"))
  print("원진#7917") 
  print(client.user.name) 
  print(client.user.id) 
   
@client.event
async def on_message(message):
 
  if message.content.startswith('/인증'): 
    author = message.guild.get_member(int(message.author.id))
    role = discord.utils.get(message.guild.roles, name="TEST") 
    await author.add_roles(role)
    await message.channel.send(embed=embed)


embed=discord.Embed(title="𝗩 𝙁𝙞𝙫𝙚𝙈 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮", description="인증이 완료되었습니다 :laughing:", color=0x00ff56)







  

client.run(token)

