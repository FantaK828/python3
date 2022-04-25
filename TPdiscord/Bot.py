from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()


bot.run("OTYwMTg4NjQ3ODgwMTUxMTgz.YkmzXQ.ijHJcmHInsqEAta7CFuUTrphlUQ")

