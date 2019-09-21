#IMPORT
import discord
from auth import *
from miscfunctions import *
from dice import *

#BOT ASSIGNMENT

bot = discord.Client()

#BOT FUNCTIONS

@bot.event
async def on_ready():
    print("Logged in.")

@bot.event
async def on_message(message):
    #COMMANDS

    #Help
    if message.content.lower().startswith(commands.get('halp')):
        helpmsg = open_file('help_file', "r").read()
        print("Help")
        await bot.send_message(message.channel, helpmsg)

    #Dice roller
    if commands.get('diceroll') in message.content.lower():
        print("Dice roll")
        await bot.send_message(message.channel, roll(message.content))

    #Magic conch
    if message.content.lower().startswith(commands.get('yesorno')):
        print("Yes-no")
        await bot.send_message(message.channel, "{}".format(get_random_choice('magic8')))

if __name__ == "__main__":
    bot.run(get_id('bot', 'run'))

print("File is opened")
