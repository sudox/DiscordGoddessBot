import discord
import asyncio
import datetime
import subprocess
import random

client = discord.Client()

@client.event
async def on_ready():
    print('I\'m here')

@client.event
async def on_message(message):
    if message.content.lower().startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.lower().startswith('!sleep'):
        await client.send_message(message.channel, 'Going to sleep...')
        await asyncio.sleep(float(message.content[message.content.find('(')+1:message.content.find(')')]))
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.lower().startswith('!echo'):
        await client.send_message(message.channel, message.content[6:])
        await client.delete_message(message)

    elif message.content.lower().startswith('!do you love me'):
        await client.send_message(message.channel, 'No')

    elif message.content.lower().startswith('!delete'):
        await client.delete_message(message)

    elif message.content.lower().startswith('!pray'):
        await client.send_message(message.channel, str(subprocess.Popen("fortune", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')))

    elif message.content.lower().startswith('!character'):
        await client.send_message(message.channel, 'STR: ' + str(random.randint(4, 18)) + '\nCON: ' + str(random.randint(4,18)) + '\nDEX: ' + str(random.randint(4,18)) + '\nINT: ' + str(random.randint(4,18)) + '\nWIS: ' + str(random.randint(4,18)) + '\nCHA: ' + str(random.randint(4,18)))

client.run('MzI2NDE5NTY2ODkwODQ0MTYy.DCmifA.VDn19q6vu9mTzkL6bv34JUjfbeg')
