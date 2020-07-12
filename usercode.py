"""
This is how the user would use our apilib.
Enables them to interact with the REST api and our application.
The server of course must be up and running.
"""

import apilib


payload = {"args": ["leo", "lo"]}

apilib.checkserver()
apilib.configure(payload)

