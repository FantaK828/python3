import discord


client = discord.Client()




@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    pass

@client.event
async def on_message(message):
      print(message.content)

@client.event
async def on_message(message):
    if message.content.startswith("!add!"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.add()







client.run("")