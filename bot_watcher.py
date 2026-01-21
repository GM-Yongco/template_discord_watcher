# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: watching for changes in web scraping or api and pinging users that want it
# ========================================================================

import inspect
import asyncio
import datetime
from dotenv import load_dotenv

from discord_class import *

from detector_hermes import DetectorHermes

# ========================================================================
# NEW CLASS
# ========================================================================

class WatcherBot(DiscordBot):
		
	async def notify(
			self, 
			message:str = "" 
		) -> None:	
		if message == "" or message == None:
			return None
		try:
			await self.USER_01.send(f"```{message}```")
			# await self.USER_02.send(f"```{message}```")
		except Exception as e:
			await self.LOG_CHANNEL.send(f"```{e}```")

	async def execute_list(self, function_list:List[Callable]):
		for function in function_list:
			try:
				print(f"executing_function - {'START':8} : {function.__name__}")
				if inspect.iscoroutinefunction(function):
					await function()
				else:
					function()
				print(f"executing_function - {'SUCCESS':8} : {function.__name__}")
			except Exception as e:
				print(f"executing_function - {'ERROR':8} : {function.__name__}\n\t{e}")


	# ====================================================================

	async def bot_task_cycle(self):
		interval_seconds:int = 12

		# time updates
		previous_year:int = -1
		previous_month:int = -1
		previous_week:int = -1
		previous_day:int = -1
		previous_hour:int = -1
		previous_minute:int = -1

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
				await self.execute_list(self.functions_on_week)
			if time_now.day != previous_day:
				previous_day = time_now.day
				await self.execute_list(self.functions_on_day)
			if time_now.hour != previous_hour:
				previous_hour = time_now.hour
				await self.execute_list(self.functions_on_hour)
			if time_now.minute != previous_minute:
				previous_minute = time_now.minute
				await self.execute_list(self.functions_on_minute)			
			await self.execute_list(self.functions_on_cycle)

	# ====================================================================

	async def async_wrapper(self)->None:
		bot_log:asyncio.Task = asyncio.create_task(
			self.bot_task_cycle()
		)
		await asyncio.gather(bot_log)
	
	# ====================================================================


	async def initialize_watcher(self) -> None:
		print(f"initializing_watcher - {'START':8}")
					

		# initialized notif
		load_dotenv()
		self.USER_01:discord.User = self.bot.get_user(int(os.getenv("ID_USER_01")))
		self.USER_02:discord.User = self.bot.get_user(int(os.getenv("ID_USER_02")))

		self.functions_on_week:List[Callable] = []
		self.functions_on_day:List[Callable] = []
		self.functions_on_hour:List[Callable] = []
		self.functions_on_minute:List[Callable] = []
		self.functions_on_cycle:List[Callable] = []

		# async def notif_test():
		# 	await self.notify("test-kill yourself")
		# self.functions_on_cycle.append(notif_test)

		async def detector_hermes_function():
			detector_hermes_class:DetectorHermes = DetectorHermes()
			await self.notify(detector_hermes_class.hermes_detector())
		self.functions_on_cycle.append(detector_hermes_function)

		await self.async_wrapper()


# ========================================================================
# TEST
# ========================================================================

if __name__ == '__main__':
	bot:WatcherBot = WatcherBot()
	bot.functions_on_ready.append(bot.initialize_watcher)
	bot.run()