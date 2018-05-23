# HA17. Delay Error
#Add one line for 1 second delay in any code and handle any exception generated

import time
try:
	time.sleep(5)
	print([2**x for x in range(10)])
except Exception as e:
	print(e)