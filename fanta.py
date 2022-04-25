import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
      print(message.content)

@client.event
async def on_message(message):
    pass

@client.event
async def on_message(message):
    print(message.content)

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_member_join(member):
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(959367147723829299)
    general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

client.run("OTU5MzYwNDIwNzEwMzI2Mjky.YkawBA.b786XyJVPySCRREZtHwD3Hf5Cbg")
      
