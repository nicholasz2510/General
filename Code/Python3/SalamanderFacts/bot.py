import discord
import random

f = open("token.txt", "r")
facts_file = open("facts.txt", "r")
facts = facts_file.readlines()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        elif message.content.startswith('-fact'):
            await message.channel.send(random.choice(facts))


client = MyClient()
client.run(f.readline())
f.close()
