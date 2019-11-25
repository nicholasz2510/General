import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "stupid" in [x.lower() for x in message.content.split()]:
        await message.channel.send()

client.run('NTk2MDcxNzM3MDQ5NzQzNDQy.XR0NKA.32ecA4XJsMEaUJUBt0o__H2RszY')
