# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: watching for changes in the hermes enrollment queue
# ========================================================================
# HEADERS
# ========================================================================

import json
import requests

# ========================================================================
# FUNCTIONS MISC
# ========================================================================
class DetectorHermes():
	LINK_HERMES:str = "https://hermes.dcism.org/queue/BSCS/number/current"
	LIMIT:int = 50
	success_count:int = 0

	def hermes_detector(self)->str:
		response = requests.get(self.LINK_HERMES)
		data_str:str = response.content.decode("utf-8")
		data_json:json = json.loads(data_str)
		current:int = int(data_json['current'])

		ret_val:str = ""
		if current >= self.LIMIT:
			ret_val = "ENROLLMENT TIME"

		return ret_val
