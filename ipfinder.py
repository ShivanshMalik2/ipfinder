import requests

response = requests.get("https://ipinfo.io/ip")

reso = response.content

print(f"your ip: {reso}")
