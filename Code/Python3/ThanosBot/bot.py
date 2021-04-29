import discord
import random

f = open("token.txt", "r")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('-snap'):
        await message.channel.send("With all six stones I can simply snap my fingers and it'll all cease to exist. I "
                                   "call that, mercy.")
        snapped_role = discord.utils.get(message.guild.roles, name="snapped")
        num_members = message.guild.member_count
        members = message.guild.members
        for x in range(int(num_members / 2)):
            curr_member = random.choice(members)
            if curr_member.name == "ThanosBot":
                members.remove(curr_member)
                curr_member = random.choice(members)
            await curr_member.add_roles(snapped_role)
            print(curr_member.name)
            members.remove(curr_member)

    elif message.content.startswith('-pardon'):
        await message.channel.send("<@461292499290554368> has taught me the flaws in the Malthusian doctrine. Thus, "
                                   "I pardon you. All of you.")


client.run(f.readline())
f.close()
