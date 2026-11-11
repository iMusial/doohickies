import requests
import json

response = requests.get('https://ipecho.io/my')
ipDict = json.loads(response.content)

print("ip: " + ipDict['ip'])
print("internet service provider: " + ipDict['isp'])
print("city: " + ipDict['city'])
print("region: " + ipDict['region'])
print("country: " + ipDict['country'])
print("latitude: " + ipDict['latitude'])
print("longitude: " + ipDict['longitude'])
