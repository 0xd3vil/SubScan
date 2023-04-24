import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('domain')
args = parser.parse_args()

domain = args.domain

url = f"https://crt.sh/?q=%25.{domain}&output=json"

try:
    response = requests.get(url)
    if response.ok:
        data = json.loads(response.text)
        subdomains = set()
        for entry in data:
            subdomains.add(entry['name_value'])
        print(f"{len(subdomains)} subdomains found:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print(f"Failed to retrieve subdomains: {response.status_code} - {response.reason}")
except Exception as e:
    print(f"An error occurred while retrieving subdomains: {e}")
