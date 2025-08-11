# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from discord_class import *

import json
import requests
import asyncio
import datetime

from dotenv import load_dotenv

# ========================================================================
# NEW CLASS
# ========================================================================

class WatcherBot(DiscordBot):

	def detector(self, link:str)->bool:
		response = requests.get(link)
		data_str:str = response.content.decode("utf-8")
		data_json:json = json.loads(data_str)

		ret_val = False
		if int(data_json['current']) >= 80:
			ret_val = True

		return ret_val

	# ====================================================================

	async def bot_task_cycle(self, bot:discord.ext.commands.bot.Bot):
		interval_seconds:int = 12

		# time updates
		previous_year:int = -1
		previous_month:int = -1
		previous_week:int = -1
		previous_day:int = -1
		previous_hour:int = -1
		previous_minute:int = -1

		load_dotenv()
		LINK:str = str(os.getenv("LINK"))
		USER_01:discord.User = bot.get_user(int(os.getenv("ID_USER_01")))
		USER_02:discord.User = bot.get_user(int(os.getenv("ID_USER_02")))

		message_count:int = 0

		while(True):
			await asyncio.sleep(interval_seconds)
			time_now:datetime.datetime = datetime.datetime.now()

			# ============================================================
			# put the tasks on the given date type

			if time_now.year != previous_year:
				previous_year = time_now.year
			if time_now.month != previous_month:
				previous_month = time_now.month
			if time_now.isocalendar()[1] != previous_week:
				previous_week = time_now.isocalendar()[1]
			if time_now.day != previous_day:
				previous_day = time_now.day
			if time_now.hour != previous_hour:
				previous_hour = time_now.hour
			if time_now.minute != previous_minute:
				previous_minute = time_now.minute

			# ============================================================
			# every cycle type shi

			message:str = ""
			message_cmd:str = ""
			if self.detector(LINK) and (message_count < 10):
				message += "TIME TO GO MOTHER FUCKER"
				message += f"\nENROLLMENT TIME"
				try:
					await USER_01.send(f"```{message}```")
					await USER_02.send(f"```{message}```")
					message_count += 1
				except Exception as e:
					await self.LOG_CHANNEL.send(f"```{e}```")
				message_cmd = "ITS TIME"
			else:
				response = requests.get(LINK)
				data_str:str = response.content.decode("utf-8")
				data_json:json = json.loads(data_str)

				message += "its not yet time, we must be patient"
				message += "\n"
				message += json.dumps(data_json, indent=4)
				await self.LOG_CHANNEL.send(f"```{message}```")
				message_cmd = "its not time"
			print(message_cmd)

	# ====================================================================

	async def async_wrapper(self)->None:
		bot_log:asyncio.Task = asyncio.create_task(
			self.bot_task_cycle(self.bot)
		)
		await asyncio.gather(bot_log)
	
# ========================================================================
# TEST
# ========================================================================

if __name__ == '__main__':
	bot:WatcherBot = WatcherBot()
	bot.functions_on_ready.append(bot.async_wrapper)
	bot.run()