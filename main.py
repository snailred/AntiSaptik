import discord
from discord.ext import commands
import json
import datetime
from encoderrr import Message, MyEncoder

data = {"вау": []}

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_message(message):
    split_message = message.content.split()
    if len(split_message) == 0:
        return None
    msg = Message(message.author, message.content)
    data["харча"].append(msg)
    await bot.process_commands(message)

@bot.event
async def on_disconnect():
    time = datetime.datetime.now()
    print('bydlo disconnect at {}'.format(time))
    with open('musor.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, cls=MyEncoder, indent=4, ensure_ascii=False)

@bot.command(name='андрей')

@commands.is_owner()
async def bot_shutdown(ctx):
    await ctx.bot.logout()

bot = discord.сlient()

hello_world = ["hi", "привет", "саламайкум", "шалом", "hello"]


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    if msg in hello_world:
        await message.channel.send('привет {0.author}'.format(message))


bot.run('ODEzNzMzMzE1OTI0MzI4NDg4.YDTmNA.vtn8tfxLPLnBeM5zY1iyO1kORGw')
