from datetime import datetime
import pytz

file = '1541962108935000000_167_838.h5'
cern_time=pytz.timezone('Europe/Zurich')
unix_time=float(file[:18])/100000000
utc=datetime.utcfromtimestamp(unix_time)
print("Time UTC is",utc)
cern=pytz.utc.localize(utc).astimezone(cern_time)
print("Time in Switzerland/CERN is",cern)
