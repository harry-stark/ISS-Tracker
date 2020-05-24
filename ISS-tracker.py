

import urllib.request, urllib.error, urllib.parse
import json
import time

req = urllib.request.Request("https://api.wheretheiss.at/v1/satellites/25544")
response = urllib.request.urlopen(req)

obj = json.loads(response.read())
z=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(obj['timestamp']))
print("At Time ",z," ISS bearings are:")
for a,b in obj.items():
     print(a,":",b)

