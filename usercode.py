"""
This is how the user would use our apilib.
Enables them to interact with the REST api and our application.
The server of course must be up and running.
"""
import time
start_time = time.time()

import apilib


payload = {"args": ["leo", "lo"]}

apilib.checkserver()
apilib.configure(payload)

print("--- %s seconds ---" % (time.time() - start_time))

