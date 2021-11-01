import requests
import sys
import re
import subprocess

# Change this:
discord_role_id = "827339782199836682"

args = sys.argv[1:]

url = args[0]

split_ip = args[1].split(".")
ip = f"{split_ip[0]}.{split_ip[1]}.\*\*\*.\*\*\*"

hostname = subprocess.check_output(["hostname"]).decode().splitlines()[0]
username = subprocess.check_output(["whoami"]).decode().splitlines()[0]

country_data_url = f"https://ipwhois.app/json/{args[1]}"
country_data = requests.get(country_data_url).json()

country = ""
country_code = ""

print(country_data)

if "country" in country_data:
    country = country_data["country"]
else:
    country = f"Unknown"

if "country_code" in country_data:
    code = country_data["country_code"]
    country_code = f"flag_{code.lower()}"
else:
    country_code = f"pirate_flag"

payload = {
    "content": f"<@&{discord_role_id}> :shield: New logon to `{username}@{hostname}` in :{country_code}: {country} ({ip})"
}

x = requests.post(url, json=payload)