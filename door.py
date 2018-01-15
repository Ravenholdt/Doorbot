#! python3

import discord
from discord.ext import commands
import asyncio

import time

import config
prefix = 'None'

bot = commands.Bot(command_prefix=prefix, description='Test Bot, Please Ignore')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print('------')

	setStatus = 'Öppet'
	status = 'Error'

	while True:
		if not status == setStatus:
			status = setStatus
			await bot.change_presence(game=discord.Game(name=str(status)))
			#await bot.say("I am now playing " + status + ".")
		time.sleep(10)


		if setStatus == 'Öppet':
			setStatus = 'Stängt'
		else:
			setStatus = 'Öppet'


if __name__ == "__main__":

	bot.run(config.discordtoken)