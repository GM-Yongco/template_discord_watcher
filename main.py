# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: main file that runs the bot and appends to initialization functions
# HEADERS ================================================================

from bot_watcher import WatcherBot

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	bot:WatcherBot = WatcherBot()
	bot.functions_on_ready.append(bot.initialize_watcher)
	bot.run()