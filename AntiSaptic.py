import discord

client = discord.Client()

hello_world = ["hi", "привет", "саламайкум", "шалом", "hello"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg in hello_world:
        await message.channel.send('привет {0.author}'.format(message))

 @client.event
async def forward(message):

        await message.channel.send(' {0.author}: написал: {0.content}'.format(message))
client.run('ODEzNzMzMzE1OTI0MzI4NDg4.YDTmNA.vtn8tfxLPLnBeM5zY1iyO1kORGw')





 

