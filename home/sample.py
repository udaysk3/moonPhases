import requests

req = requests.get("https://api.farmsense.net/v1/moonphases/?d=1642346172")

phase = req.json()[0]["Phase"]
illumination = req.json()[0]['Illumination'] * 100

print(phase, illumination)


