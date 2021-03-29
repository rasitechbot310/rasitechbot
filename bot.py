import random
import sys
import time
import urllib, json
while True:
url = "https://api.telegram.org/bot1490602279:AAFJxEVNiSXDns5m8qFAhtPxz-B3hOLIx3E/sendMessage?chat_id=@RasiTechBotLogs&text=halo"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
time.sleep(0.05)
